import pygame as pg
import random as r
from enum import Enum
from collections import namedtuple
from itertools import product
import numpy as np

pg.init()
font = pg.font.SysFont(None, 25)

class Direction(Enum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3
#

point = namedtuple('Point', 'x, y')

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) # background
RED = (200, 0, 0) # obstacle
GREEN = (0, 128, 0) # trophie - for the reward
BLUE = (0, 0, 255) # robot body

# specs
BLOCK_SIZE = 20
SPEED = 40

# robot class
class Simulation:
    def __init__(self, w = 640, h = 480, n_obstacle = 20):
        self.w = w
        self.h = h
        self.n_obstacles = n_obstacle

        self.display = pg.display.set_mode((self.w, self.h))

        self.clock = pg.time.Clock()
        self.reset()
    #
    def reset(self):
        self.direction = Direction.RIGHT

        # allinea la posizione della robot alla griglia (multipli di BLOCK_SIZE)
        start_x = (self.w // (2 * BLOCK_SIZE)) * BLOCK_SIZE * 2 // 2  # semplice, ma manteniamo multiplo di BLOCK_SIZE
        start_x = (self.w // 2) // BLOCK_SIZE * BLOCK_SIZE
        start_y = (self.h // 2) // BLOCK_SIZE * BLOCK_SIZE

        # meglio: round to nearest grid cell
        self.robot = point(start_x, start_y)

        self.score = 0
        self.trophie = None
        self.obstacles = []

        self.place_trophie()
        self.place_obstacles()

        self.frame_iteration = 0
    #
    def place_trophie(self):
        x = r.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = r.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

        new_trophie = point(x, y)

        if new_trophie == self.robot or new_trophie in self.obstacles:
            return self.place_trophie()
        
        self.trophie  = new_trophie
    #
    def place_obstacles(self):
        self.obstacles.clear()
        for _ in range(self.n_obstacles):
            x = r.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            y = r.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            pt = point(x, y)
            # evita robot e trofeo
            if pt != self.robot and pt != self.trophie:
                self.obstacles.append(pt)
    #
    def step(self, action):
        self.frame_iteration += 1

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        
        self.move(action)
        
        reward = 0

        game_over = False

        # frame limit: prevenire loop infinito -> proporzionale alle celle totali
        max_frames = 100 * (self.w // BLOCK_SIZE) * (self.h // BLOCK_SIZE)
        
        if self.is_collision() or  self.frame_iteration > max_frames:
            game_over = True
            reward = -10
            return reward, game_over, self.score

        if self.robot == self.trophie:
            self.score += 1
            reward = +10
            self.place_trophie()
            self.frame_iteration = 0

        self.update_ui()
        self.clock.tick(SPEED)

        return reward, game_over, self.score            
    #
    def is_collision(self, pt = None):
        if pt is None:
            pt = self.robot

        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        
        if pt == self.robot:
            return True

        return False
    #
    def update_ui(self):
        self.display.fill(BLACK)

        # draw trophie
        pg.draw.rect(self.display, GREEN, pg.Rect(self.trophie.x, self.trophie.y, BLOCK_SIZE, BLOCK_SIZE))
        
        # draw obstacles
        for obs in self.obstacles:
            pg.draw.rect(self.display, RED, pg.Rect(obs.x, obs.y, BLOCK_SIZE, BLOCK_SIZE))

        # draw robot
        pg.draw.rect(self.display, BLUE, pg.Rect(self.robot.x, self.robot.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render(f"Score: {self.score}", True, WHITE)
        self.display.blit(text, [0, 0])
        pg.display.flip()
    #
    def move(self, action):
        movement = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        index = movement.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = movement[index] # straight
        elif np.array_equal(action, [0, 1, 0]):
            next_index = (index + 1) % 4
            new_dir = movement[next_index]
        elif np.array_equal(action, [0, 0, 1]):
            next_index = (index - 1) % 4
            new_dir = movement(next_index)
        else:
            new_dir = self.direction
        
        self.direction = new_dir

        x = self.robot.x
        y = self.robot.y

        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = point(x, y)
