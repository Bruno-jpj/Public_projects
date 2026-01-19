import numpy as np


class Controller:
    def __init__(self, target, missile):
        self.target = target
        self.missile = missile
    #
    def TargetDestroyed(self) -> bool:
        if self.missile in self.target:
            return True
        return False
    #