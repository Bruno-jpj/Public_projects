import numpy as np
import matplotlib.pyplot as plt

# const cells
ROBOT = 2  # orange
OCCUPIED = -1  # red
FREE = 0  # green
UNKNOWN = 1  # gray

# const robot
ROBOT_X, ROBOT_Y, ROBOT_Z = 1, 1, 1
START_POINT = (0, 0, 0)

# create map3D known cause Obj Robot
def create_map3D(start_pos):
    mappa = {}
    # la grandezza del robot è definita solo nella posizione iniziale
    mappa[start_pos] = ROBOT 
    return mappa

# create example-test obj
def create_obstacle(mappa):
    # esempio: blocco alcune celle centrali
    for x in range(2, 4):
        for y in range(2, 4):
            for z in range(1, 3):
                mappa[(x, y, z)] = OCCUPIED

# update map and robot position
def update_map(mappa, old_pos, new_pos):
    # libera vecchia cella
    if old_pos in mappa and mappa[old_pos] != OCCUPIED:
        mappa[old_pos] = FREE
    
    # controlla se nuova posizione è occupata
    if new_pos in mappa and mappa[new_pos] == OCCUPIED:
        print("Collisione!")
        return old_pos
    
    # aggiorna nuova posizione
    mappa[new_pos] = ROBOT
    return new_pos

# draw map
# disegno mappe infinite (mostro solo celle conosciute)
def draw_map(mappa, ax, fig, robot_pos, view_range=5):
    
    #Disegna solo una finestra centrata sul robot di lato view_range*2+1.
    # view_range = distanza di vista

    #(x, y, z)
    rx, ry, rz = robot_pos
    min_x, max_x = rx - view_range, rx + view_range
    min_y, max_y = ry - view_range, ry + view_range
    min_z, max_z = rz - view_range, rz + view_range

    size_x = max_x - min_x + 1
    size_y = max_y - min_y + 1
    size_z = max_z - min_z + 1

    voxels = np.zeros((size_x, size_y, size_z), dtype=bool)
    colors = np.empty(voxels.shape, dtype=object)

    for (x, y, z), status in mappa.items():
        if min_x <= x <= max_x and min_y <= y <= max_y and min_z <= z <= max_z:
            ix, iy, iz = x - min_x, y - min_y, z - min_z
            voxels[ix, iy, iz] = True
            if status == OCCUPIED:
                colors[ix, iy, iz] = "red"
            elif status == ROBOT:
                colors[ix, iy, iz] = "orange"
            elif status == FREE:
                colors[ix, iy, iz] = "green"

    ax.clear()
    ax.voxels(voxels, facecolors=colors, edgecolor="k")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Simulazione robot 3D")
    ax.set_xlim(0, size_x)
    ax.set_ylim(0, size_y)
    ax.set_zlim(0, size_z)
    fig.canvas.draw_idle() # aggiorna il plot
    fig.canvas.flush_events() # pulisce il plot
#
def readMap(mappa):
    coordinatelist = []
    for coordinates in mappa:
        coordinatelist.append(coordinates)
    print(f"{coordinatelist} \n")
#
def main():
    global robot_pos, mappa, ax  # rendi globali per callback

    # posizione iniziale del robot
    robot_pos = START_POINT
    mappa = create_map3D(START_POINT)
    create_obstacle(mappa)

    # definizione movimenti
    moves = {
        "1": (0, 1, 0),   # avanti
        "2": (0, -1, 0),  # indietro
        "3": (-1, 0, 0),  # sinistra
        "4": (1, 0, 0),   # destra
        "5": (0, 0, 1),   # su
        "6": (0, 0, -1)   # giù
    }

    # setup matplotlib interattivo
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    draw_map(mappa, ax, fig, robot_pos)  # passa robot_pos

    # callback pressione tasti
    def on_key(event):
        global robot_pos
        if event.key == "q":
            plt.close(fig)
        elif event.key in moves:
            dx, dy, dz = moves[event.key]
            new_pos = (robot_pos[0] + dx, robot_pos[1] + dy, robot_pos[2] + dz)
            robot_pos = update_map(mappa, robot_pos, new_pos)
            draw_map(mappa, ax, fig, robot_pos)  # passa robot_pos

    fig.canvas.mpl_connect("key_press_event", on_key)
    plt.show()

    # loop principale per tenere viva la finestra
    while plt.fignum_exists(fig.number):
        plt.pause(0.3)

if __name__ == "__main__":
    main()