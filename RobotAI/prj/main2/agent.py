import torch
import random
import numpy as np 

from collections import deque

from simulation import Direction, point
from model import Linear_QNet, QTrainer


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

    def get_state(self, simulation):
        head = simulation.robot

        point_l = point(head.x - 20, head.y)
        point_r = point(head.x + 20, head.y)
        point_u = point(head.x, head.y - 20)
        point_d = point(head.x, head.y + 20)

        dir_l = simulation.direction == Direction.LEFT
        dir_r = simulation.direction == Direction.RIGHT
        dir_u = simulation.direction == Direction.UP
        dir_d = simulation.direction == Direction.DOWN

        state = [
            # pericolo davanti
            (dir_r and simulation.is_collision(point_r)) or 
            (dir_l and simulation.is_collision(point_l)) or 
            (dir_u and simulation.is_collision(point_u)) or 
            (dir_d and simulation.is_collision(point_d)),

            # pericolo a destra
            (dir_u and simulation.is_collision(point_r)) or 
            (dir_d and simulation.is_collision(point_l)) or 
            (dir_l and simulation.is_collision(point_u)) or 
            (dir_r and simulation.is_collision(point_d)),

            # pericolo a sinistra
            (dir_d and simulation.is_collision(point_r)) or 
            (dir_u and simulation.is_collision(point_l)) or 
            (dir_r and simulation.is_collision(point_u)) or 
            (dir_l and simulation.is_collision(point_d)),

            # direzione attuale
            dir_l,
            dir_r,
            dir_u,
            dir_d,

            # posizione trofeo
            simulation.trophie.x < simulation.robot.x, 
            simulation.trophie.x > simulation.robot.x, 
            simulation.trophie.y < simulation.robot.y, 
            simulation.trophie.y > simulation.robot.y  
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
#
'''
def run():
    agent = Agent()
    sim = Simulation()

    agent_reward = 0
    agent_record = 0
    agent_tot_reward = 0
    agent_score = 0


    plt.ion()
    fig, ax = plt.subplots()
    plt.show(block=False) 

    while True:

        # current state
        state_old = agent.get_state(sim)

        # action
        final_move = agent.get_action(state_old)

        # execute action
        agent_reward, agent_score = sim.step(final_move)

        # update map
        ml.draw_map(sim.robot_map, ax, sim.w, sim.h)

        # new state
        state_new = agent.get_state(sim)

        # train short memory
        agent.train_short_memory(state_old, final_move, agent_reward, state_new)

        # save exp
        agent.remember(state_old, final_move, agent_reward, state_new)

        # train long memory
        agent.train_long_memory()

        # update record
        if agent_score > agent_record:
            agent_record = agent_score
            agent.model.save()

        agent_tot_reward += agent_reward
        agent.n_games += 1


        # stampa log
        print(f"Movement: {agent.n_games}, Score: {agent_score}, Tot Trophies: {sim.tot_trophies}, Reward: {agent_reward}, Total Reward: {agent_tot_reward}, Loss: {agent.trainer.train_step(state_old, final_move, agent_reward, state_new)}")
#
'''