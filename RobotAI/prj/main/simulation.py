import pygame as pg
import random as r
import numpy as no

# special type of tuple, can access element by position or name
from collections import namedtuple
from enum import Enum

pg.init()
font = pg.font.Font(None, 25)

class Direction(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3
#

point = namedtuple('Point', 'x, y')

# colors
WHITE = (255, 255, 255) # text
BLACK = (0, 0, 0) # background
RED = (200, 0, 0) # obstacle
GREEN = (0, 128, 0) # trophie
BLUE = (0, 0, 255) # robot body

# specs
BLOCK_SIZE = 20
SPEED = 40

class Simulation:
    def __init__(self, w = 640, h = 480, num_obs = 0):
        self.w = w
        self.h = h

        num_obs = r.randint(1, 20)
        self.num_obs = num_obs

        self.display = pg.display.set_mode((self.w, self.h))

        self.clock = pg.time.Clock()
        self.reset()
    #
    def reset(self):
        self.direction = Direction.RIGHT

        self.robot = point(self.w/2, self.h/2)

        self.score = 0
        self.trophie = None
        self.obstacles = []

        self.place_trohpie()
        self.place_obstacles()

        self.frame_iteration = 0 # action counter
    #
    def place_trohpie(self):
        # range x: (0, 620) y: (0, 460)
        x = r.randint(0, (self.w-BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = r.randint(0, (self.h-BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

        trophie = point(x, y)

        if trophie == self.robot or trophie in self.obstacles:
            return self.place_obstacles()
        
        self.trophie = trophie
    # 
    def place_obstacles(self):
        # clear list
        self.obstacles.clear()

        for _ in range(self.num_obs):
            x = r.randint(0, (self.w-BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            y = r.randint(0, (self.h-BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

            # create tuple obj of obstacles
            pt = point(x, y)

            if pt != self.robot and pt != self.trophie:
                # insert obj in the obstacles list
                self.obstacles.append(pt)
    #
    def step(self, action):
        self.frame_iteration += 1

        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                quit()
        
        self.move(action)

        reward = 0
        # frame limit
        max_frame = 100 * (self.w // BLOCK_SIZE) * (self.h // BLOCK_SIZE)

        if self.is_collision() or self.frame_iteration > max_frame:
            reward = -10
            return reward, self.score
        
        if self.robot == self.trophie:
            self.score += 1
            reward = +10
            self.place_trohpie()
            # self.frame_iteration = 0
        
        self.update_ui()
        self.clock.tick(SPEED)

        return reward, self.score
    #
    def is_collision(self, pt = None):
        if pt is None:
            pt = self.robot
        
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt < 0:
            return True
        
        if pt == self.robot:
            return True
        
        return False
    #
    def update_ui(self):

        # fill display with black
        self.display.fill(BLACK)

        # draw trophies
        pg.draw.rect(self.display, GREEN, pg.Rect(self.trophie.x, self.trophie.y, BLOCK_SIZE, BLOCK_SIZE))

        # draw obstacles
        for obstacle in self.obstacles:
            pg.draw.rect(self.display, RED, pg.Rect(obstacle.x , obstacle.y, BLOCK_SIZE, BLOCK_SIZE))

        # draw robot
        pg.draw.rect(self.display, BLUE, pg.rect(self.robot.x, self.robot.y, BLOCK_SIZE, BLOCK_SIZE))

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
    #
