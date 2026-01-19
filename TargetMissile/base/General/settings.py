from enum import Enum

# Map
X, Y, Z = 3000, 3000, 3000

# Colors
TEXT_COLOR = "white" 
BACKGROUND_COLOR = "black" 
MISSILE_COLOR = "red" 
TARGET_COLOR = "blue"


# Specs
STEP_SIZE = 100 # step of the map, distance measure 1:10m -> 1000m
TARGET_SPEED = 40 # 400 m/s
MISSILE_SPEED = 55 # 550 m/s

class TargetStartPos(Enum):
    X_target = 200,
    Y_target = 200,
    Z_target = 200,
class MissileStartPos(Enum):
    X_missile = 0,
    Y_missile = 0,
    Z_missile = 0,

# Status
GROUND = 0
FREE_SPACE_STATUS = 1
UNKNOWN_SPACE_STATUS = 2
class TARGET_STATUS(Enum):
    Alive = 0
    Destroyed = 1
class MISSILE_STATUS(Enum):
    Hit = 0,
    Miss = 1


# AppName
APP_NAME = "TargetMissile-Simulation"

# Dimension
W, H = 1920, 1080