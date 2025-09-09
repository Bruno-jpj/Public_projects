import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def insert_robot(map3D, start_pos, x, y, z, status):
    for i in range(x):
        for j in range(y):
            for k in range(z):
                pos = (start_pos[0] + i, start_pos[1] + j, start_pos[2] + k)
                map3D[pos] = status
    #
    return map3D
#

def main():

    START_POS = [0, 0, 0]

    # width, height, depth
    ROBOT_X, ROBOT_Y, ROBOT_Z = 5, 5 , 7
   
    # status: 0 unknwn, 1 free, -1 occupied
    map3D = {}

    map3D = insert_robot(map3D, START_POS, ROBOT_X, ROBOT_Y, ROBOT_Z, -1)

    # find max dimensions for the grid
    max_x = max(pos[0] for pos in map3D.keys()) + 1
    max_y = max(pos[1] for pos in map3D.keys()) + 1
    max_z = max(pos[2] for pos in map3D.keys()) + 1
    
    # create a 3D grid of voxels
    voxels = np.zeros((max_x, max_y, max_z), dtype=bool)
    colors = np.empty(voxels.shape, dtype=object)

    # populate the grid
    for (x, y, z), s in map3D.items():
        voxels[x, y, z] = True
        if s == -1:   
            colors[x, y, z] = "red"
        elif s == 0:  
            colors[x, y, z] = "gray"
        elif s == 1:  
            colors[x, y, z] = "green"

    # plot the map
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.voxels(voxels, facecolors=colors, edgecolor="k")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Mappa 3D con Voxel")

    plt.show()

#

if __name__ == "__main__":
    main()