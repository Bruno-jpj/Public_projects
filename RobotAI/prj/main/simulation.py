import pygame as pg
import random as r
import numpy as np
import os

MAP_ROBOT_PATH = r'/home/userbruno/Scrivania/github/Public_projects/RobotAI/prj/main/map.txt'

from CONST import UNKNOWN, FREE, OBSTACLE, BLOCK_SIZE, ROBOT, SPEED, BLACK, BLUE, WHITE, RED, GREEN

import map_logic as ml

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

class Simulation:
    def __init__(self, w = 640, h = 480):
        self.w = w
        self.h = h

        # valori: ((x, y) :  status)
        # creata la mappa dove per ogni cordinata (x, y) = UNKNOWN
        self.robot_map = ml.create_map(self.w, self.h)

        self.num_obs = r.randint(1, 20) 

        self.tot_trophies = 0

        self.display = pg.display.set_mode((self.w, self.h))

        self.clock = pg.time.Clock()
        self.reset()
    # serve solo quando si inizia una nuova simulazione
    def reset(self):
        self.direction = Direction.RIGHT

        self.robot = point(self.w//2, self.h//2)

        self.score = 0

        self.trophie = None

        self.status = None # free, unknown, obstacle

        self.obstacles = []

        self.place_trohpie()
        self.place_obstacles()

        self.frame_iteration = 0 # action counter
        self.frame_since_trophie = 0
    #
    def place_trohpie(self):
        # range x: (0, 620) y: (0, 460)
        x = r.randint(0, (self.w-BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = r.randint(0, (self.h-BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

        trophie = point(x, y)

        if trophie == self.robot or trophie in self.obstacles:
            return self.place_trohpie()
        
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
        
        old_position = self.robot # saved old position - which is temporary new_position of move() func

        new_position = self.move(action) 

        self.reward = 0
       

        # max_movement_with_no_trophie => 10 * (640 / 20) + (480 / 20) = 10 * (32 + 24) = 560
        max_frames_no_trophie = 10 * ((self.w // BLOCK_SIZE) + (self.h // BLOCK_SIZE))

        if self.is_collision(new_position):
            self.reward = -10
            self.score -= 1
            self.frame_since_trophie += 1
            self.robot_map[self.robot] = OBSTACLE

        else:
            if self.robot_map[new_position] == UNKNOWN:
                self.reward = +2
                self.frame_since_trophie -= 0.5           

            self.robot = new_position
            self.robot_map[self.robot] = FREE
        
        if self.frame_since_trophie > max_frames_no_trophie:
            self.reward = -2
            self.score -= 0.5
        
        if self.robot == self.trophie:
            self.score += 1
            self.tot_trophies += 1
            self.reward = +20
            self.frame_since_trophie = 0
            self.place_trohpie()
            self.frame_iteration = 0
        else:
            self.frame_since_trophie += 1

        self.update_ui()
        self.clock.tick(SPEED)

        return self.reward, self.score
    #
    def is_collision(self, pt = None):
        if pt is None:
            pt = self.robot
        
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        
        if pt in self.obstacles:
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
            new_dir = movement[next_index]
        else:
            new_dir = self.direction
        
        self.direction = new_dir

        next_x = self.robot.x
        next_y = self.robot.y

        if self.direction == Direction.RIGHT:
            next_x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            next_x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            next_y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            next_y -= BLOCK_SIZE

        # limiti della mappa
        # min confronta x con limite massimo, max confronta x con limite minimo
        # in questo modo x, y compreso tra 0 e w-BLOCK_SIZE / h-BLOCK_SIZE; evita che il robot esce dallo schermo

        next_x = max(0, min(self.w - BLOCK_SIZE, next_x))
        next_y = max(0, min(self.h - BLOCK_SIZE, next_y))

        new_position = point(next_x, next_y)

        return new_position
            