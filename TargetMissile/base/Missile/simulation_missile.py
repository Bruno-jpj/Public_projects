from General.settings import MISSILE_COLOR, MISSILE_STATUS
from collections import namedtuple
from enum import Enum

import random as r
import os

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

class MissileSimulation:
    def __init__(self):
        self.missile = None
    #
