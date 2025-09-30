import torch
import random
import numpy as np

import matplotlib
matplotlib.use("Qt5Agg")  # oppure "Qt5Agg" se hai PyQt5 installato
import matplotlib.pyplot as plt

from collections import deque
from simulation import Simulation, Direction, point
from model import Linear_QNet, QTrainer

import map_logic as ml

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.002

class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 80  # fattore esplorazione
        self.gamma = 0.9  # fattore sconto
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = Linear_QNet(11, 512, 3)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)

    def get_state(self, game):
        head = game.robot

        point_l = point(head.x - 20, head.y)
        point_r = point(head.x + 20, head.y)
        point_u = point(head.x, head.y - 20)
        point_d = point(head.x, head.y + 20)

        dir_l = game.direction == Direction.LEFT
        dir_r = game.direction == Direction.RIGHT
        dir_u = game.direction == Direction.UP
        dir_d = game.direction == Direction.DOWN

        state = [
            # pericolo davanti
            (dir_r and game.is_collision(point_r)) or 
            (dir_l and game.is_collision(point_l)) or 
            (dir_u and game.is_collision(point_u)) or 
            (dir_d and game.is_collision(point_d)),

            # pericolo a destra
            (dir_u and game.is_collision(point_r)) or 
            (dir_d and game.is_collision(point_l)) or 
            (dir_l and game.is_collision(point_u)) or 
            (dir_r and game.is_collision(point_d)),

            # pericolo a sinistra
            (dir_d and game.is_collision(point_r)) or 
            (dir_u and game.is_collision(point_l)) or 
            (dir_r and game.is_collision(point_u)) or 
            (dir_l and game.is_collision(point_d)),

            # direzione attuale
            dir_l,
            dir_r,
            dir_u,
            dir_d,

            # posizione trofeo
            game.trophie.x < game.robot.x, 
            game.trophie.x > game.robot.x, 
            game.trophie.y < game.robot.y, 
            game.trophie.y > game.robot.y  
        ]

        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state):
        self.memory.append((state, action, reward, next_state))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory
        
        states, actions, rewards, next_states = zip(*mini_sample)

        self.trainer.train_step(states, actions, rewards, next_states)

    def train_short_memory(self, state, action, reward, next_state):
        self.trainer.train_step(state, action, reward, next_state)

    def get_action(self, state):

        self.epsilon = max(5, 80 - self.n_games // 2)  # esplorazione decrescente
        final_move = [0, 0, 0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 2)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1
        return final_move

def train():
    agent = Agent()
    game = Simulation()

    record = 0
    total_reward = 0

    plt.ion()
    fig, ax = plt.subplots()
    plt.show(block = False)

    while True:
        # stato attuale
        state_old = agent.get_state(game)

        # azione
        final_move = agent.get_action(state_old)

        # esegui azione
        reward, score = game.step(final_move)

        # aggiorna la mappa (stesso grafico)
        ml.draw_map(game.robot_map, ax, game.w, game.h)
        plt.pause(0.1)

        # nuovo stato
        state_new = agent.get_state(game)

        # allenamento memoria breve
        agent.train_short_memory(state_old, final_move, reward, state_new)

        # salva esperienza
        agent.remember(state_old, final_move, reward, state_new)

        # allenamento memoria lunga periodico
        agent.train_long_memory()

        # aggiorna record se serve
        if score > record:
            record = score
            agent.model.save()

        total_reward += reward
        agent.n_games += 1

        # stampa log
        print(f"Movement: {agent.n_games}, Score: {score}, Tot Trophies: {game.tot_trophies}, Reward: {reward}, Total Reward: {total_reward}, Loss: {agent.trainer.train_step(state_old, final_move, reward, state_new)}")
#

if __name__ == "__main__":
    train()
