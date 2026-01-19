import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt

import numpy as np

from settings import X, Y, Z, W, H, TARGET_COLOR, MISSILE_COLOR, STEP_SIZE
from settings import TargetStartPos as TSP, MissileStartPos as MSP

class Map:
    def __init__(self):
        self.fig = None
        self.ax = None

        self.target = None
        self.missile = None
        #
    def DrawMap(self) -> None:
        # plot the window size & map
        self.fig = plt.figure(figsize=(W,H))
        self.ax = self.fig.add_subplot(111, projection="3d")

        self.SetupAxes()
        #self.DrawGrid()
        self.DrawTarget()
        self.DrawMissile()

        # show the plot
        plt.show()
    #
    def SetupAxes(self):
        # set title
        self.ax.set_title("Target-Missile Simulation")
        
        # set name of the axes
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
        
        # set min/max axes
        self.ax.set_xlim(0, X)
        self.ax.set_ylim(0, Y)
        self.ax.set_zlim(0, Z)

        # np.arange -> create an array (start, stop - 1, step)
        ticks = np.arange(0, X + STEP_SIZE, STEP_SIZE)
        self.ax.set_xticks(ticks)
        self.ax.set_yticks(ticks)
        self.ax.set_zticks(ticks)
    #
    def DrawGrid(self):
        pass
    #
    def DrawTarget(self):
        x, y, z = TSP.X_target.value, TSP.Y_target.value, TSP.Z_target.value
        
        self.target = self.ax.scatter(
            x, y, z,
            c=TARGET_COLOR,
            s=120,
            label="Target"
        )
    #
    def DrawMissile(self):
        x, y, z = MSP.X_missile.value, MSP.Y_missile.value, MSP.Z_missile.value

        self.missile = self.ax.scatter(
            x, y, z, 
            c=MISSILE_COLOR,
            s=120,
            label="Missile"
        )
    #
def run():
    map = Map()

    map.DrawMap()
#
if __name__ == "__main__":
    run()
