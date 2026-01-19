import numpy as np
import matplotlib.pyplot as plt
import random as r

# const map
MAX_X, MAX_Y, MAX_Z = 10, 10, 10
START_POINT = (2, 2, 2)

# const cell
ROBOT = 3 # orange
OCCUPIED = -1 # red
FREE = 0 # green
UNKNOWN = 1 # gray

def CreateMap(StartPos, mx, my, mz):
    map = {}
    # create the max limits for the map
    for x in range(mx):
        for y in range(my):
            for z in range(mz):
                # fill map with 'unknwon'
                map[(x,y,z)] = UNKNOWN
    # place robot on start position - inside
    map[StartPos] = ROBOT
    return map
#
def DrawMap(map, ax):

    # define max dimension
    maxX = MAX_X
    maxY = MAX_Y
    maxZ = MAX_Z

    # define the cubes
    voxels = np.zeros((maxX, maxY, maxZ), dtype=bool)
    colors = np.empty(voxels.shape, dtype=object)

    # walls (transparent gray)
    for x in range(maxX):
        for y in range(maxY):
            for z in range(maxZ):
                if (x in [0, maxX-1] or 
                    y in [0, maxY-1] or 
                    z in [0, maxZ-1]):
                    voxels[x, y, z] = True
                    #colors[x, y, z] = (0.7, 0.7, 0.7, 0.2)  # RGBA: light gray, transparent
                    colors[x, y, z] = None

    # draw map objects
    for (x, y, z), status in map.items():
        if status != UNKNOWN:
            voxels[x, y, z] = True
            if status == OCCUPIED:
                colors[x, y, z] = "red"
            elif status == ROBOT:
                colors[x, y, z] = "orange"
            elif status == FREE:
                colors[x, y, z] = "green"

    ax.clear()
    ax.voxels(voxels, facecolors=colors, edgecolor="k")

    # fix axis limits
    ax.set_xlim([0, maxX])
    ax.set_ylim([0, maxY])
    ax.set_zlim([0, maxZ])

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Simulazione robot 3D")
    plt.pause(0.1)
#
def AutoMove(map, robot_pos):
    moves = [
        (0, 1, 0),   # front y+
        (0, -1, 0),  # back y-
        (1, 0, 0),   # left x+
        (-1, 0, 0),  # right x-
        (0, 0, 1),   # up z+
        (0, 0, -1)   # down z-
    ]

    # pick a random move
    dx, dy, dz = r.choice(moves)
    new_pos = (robot_pos[0] + dx, robot_pos[1] + dy, robot_pos[2] + dz)

    # check boundaries
    if (0 < new_pos[0] < MAX_X-1 and 
        0 < new_pos[1] < MAX_Y-1 and 
        0 < new_pos[2] < MAX_Z-1):
        return new_pos
    else:
        # stay in place if move goes out of bounds
        return robot_pos
#
def UpdateMap(map, old_pos, new_pos):
    # free old cell (only if not wall)
    if old_pos in map and map[old_pos] != OCCUPIED:
        map[old_pos] = FREE

    # check collision
    if new_pos in map and map[new_pos] == OCCUPIED:
        print("Collision")
        return old_pos

    # move robot
    map[new_pos] = ROBOT
    return new_pos
#
def main():

    # robot posizione iniziale
    robot_pos = START_POINT

    # setup matplotlib interattivo
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    
    map = CreateMap(START_POINT, MAX_X, MAX_Y, MAX_Z)
    DrawMap(map, ax)

    def on_key(event):
        if event.key == "q":
            plt.close(fig)
    #
    while plt.fignum_exists(fig.number):
        new_pos = AutoMove(map, robot_pos)
        robot_pos = UpdateMap(map, robot_pos, new_pos)
        DrawMap(map, ax)
        plt.pause(0.5)  # slow down so you can see movement
    plt.show()

    while plt.fignum_exists(fig.number):
        plt.pause(0.1)
#
if __name__ == "__main__":
    main()