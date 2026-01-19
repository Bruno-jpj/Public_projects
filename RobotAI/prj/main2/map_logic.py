import matplotlib.pyplot as plt
import numpy as np

from prj_settings import UNKNOWN, FREE, OBSTACLE, BLOCK_SIZE
# self.robot_map = {(x, y): UNKNOWN for x in range(0, w, BLOCK_SIZE) for y in range(0, h, BLOCK_SIZE)}

def create_map(w, h):
    map = {}

    for x in range(0, w, BLOCK_SIZE):
        for y in range(0, h, BLOCK_SIZE):
            map[(x, y)] = UNKNOWN
    
    return map
#
def draw_map(map, ax, w, h):

    # define max dimension
    maxX = w 
    maxY = h 

    grid = np.zeros((maxX, maxY), dtype=bool)


    for (x, y), status in map.items():
        i, j = x, y
        if status == OBSTACLE:
            grid[i, j] = 1
        elif status == FREE:
            grid[i, j] = 2
        # UNKNOWN resta 0

    ax.clear()
    cmap = plt.cm.get_cmap("gray", 3)  # 0=UNKNOWN,1=OBSTACLE,2=FREE
    ax.imshow(grid, cmap=cmap, origin="lower")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Mappa Movimenti Robot")
    plt.pause(0.1)
#