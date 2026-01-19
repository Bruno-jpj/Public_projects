from map import Map
from controller import Controller

from Missile.simulation_missile import MissileSimulation as ms
from Target.simulation_target import TargetSimulation as ts

class Main:
    def __init__(self):
        self.missile = ms()
        self.target = ts()

        self.controller = Controller(self.target.target, self.missile.missile)
    #