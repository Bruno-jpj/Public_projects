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
    def __init__(self):
        # TODO: initialization func
        pass
    #
    def reset(self):
        # TODO: reset func in case of resetting
        pass
    #
    def place_trohpie(self):
        # TODO: place_trophie func for the score and reward
        pass
    # 
    def place_obstacles(self):
        # TODO: place_obstacles func
        pass
    #
    def step(self, action):
        # TODO: step func -> calculate reward and score
        pass
    #
    def is_collision(self, pt = None):
        # TODO: is_collision func -> check collisions
        pass
    #
    def update_ui(self):
        # TODO: update graphic UI
        pass
    #
    def move(self, action):
        # TODO: move func for moving in the space
        pass
    #
