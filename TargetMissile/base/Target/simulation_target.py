from General.settings import (
    TARGET_START_POS, # target start position: dict
    TARGET_COLOR, # target color: str
    TARGET_STATUS, # target status: dict {alive: 0, destroyed: 1}
    TARGET_SPEED,
    GROUND,
    FREE_SPACE_STATUS,
    UNKNOWN_SPACE_STATUS,
    X, Y, Z # simulation limits
)
from collections import namedtuple
from enum import Enum
from General.map import Map
from General.controller import Controller

import random as r
import numpy as np
import os
import time 

class Direction(Enum):
    RIGHT = 0
    LEFT = 1
    #
    UP = 2
    DOWN = 3
    #
    FORWARD = 4
    BACK = 5
#

Point = namedtuple('Target', 'x, y, z')

class TargetSimulation:
    def __init__(self):

        self.MapIstance = Map()
        self.controller = Controller()

        # 1. Target Info

        # unpack dict position
        self.x, self.y, self.z = TARGET_START_POS.values()

        # set target position
        self.target = Point(self.x, self.y, self.z)

        # set start direction 
        self.direction = None

        # live-time - living time of the target in seconds
        self.live_time = None

        # 2. Simulation Info

        # simulation score
        self.score = 0

        # target status (alive / destroyed)
        self.status = None

        # simulation reward - more time alive more reward
        self.reward = 0

        self.frame_iteration = 0
    #
    def RewardStep(self, action):

        # set old position
        old_position = self.target

        # set new position
        new_position = self.MoveTarget(action)

        #
        if self.GroundHit(new_position):
            self.reward = -2
            self.score -= 1
            self.MapIstance.map[self.target] = GROUND
        else:
            if self.MapIstance.map[new_position] == UNKNOWN_SPACE_STATUS:
                self.reward = +1
                self.score += 0.5
            #
            self.reward = +2
            self.score += 1
            self.target = new_position # update target position
            self.MapIstance.map[self.target] = FREE_SPACE_STATUS
        #
        if self.frame_iteration in range(0, 30):
            self.reward = +0.5
            self.score += 0.5
        elif self.frame_iteration in range(30, 60):
            self.reward = +1
            self.score += 1
        elif self.frame_iteration > 60:
            self.reward = + 2
            self.score += 2
        else:
            self.reward = 0
            self.score = 0
        #
        self.frame_iteration += 1
        #
        return self.reward, self.score
    #
    def MoveTarget(self, action):
        movement = [Direction.RIGHT, Direction.LEFT, Direction.DOWN, Direction.UP, Direction.FORWARD, Direction.BACK]
        index = movement.index(self.direction)
        #
        if np.array_equal(action, [1,0,0]):
            pass # x axis
        elif np.array_equal(action, [0,1,0]):
            pass # y axis
        elif np.array_equal(action, [0,0,1]):
            pass # z axis
        else:
            new_direction = self.direction # keep last direction
        #
        self.direction = new_direction # update the direction
        next_x, next_y, next_z = self.target.x, self.target.y, self.target.z
        #
        if self.direction == Direction.FORWARD:
            next_x += TARGET_SPEED
        elif self.direction == Direction.BACK:
            next_x -= TARGET_SPEED
        elif self.direction == Direction.RIGHT:
            next_y += TARGET_SPEED
        elif self.direction == Direction.LEFT:
            next_y -= TARGET_SPEED
        elif self.direction == Direction.UP:
            next_z += TARGET_SPEED
        elif self.direction == Direction.DOWN:
            next_z -= TARGET_SPEED
        #
        new_position = Point(next_x, next_y, next_z)
        return new_position
    #
    def GroundHit(self, new_position):
        if new_position.z <= 0:
            return True
        return False
    #