from queue import Queue

class Bft:
    def __init__(self, RobotPos, TargetPos, Obstacles: list):
        self.queue = Queue()
        self.visited = set()
        
        # dict: node -> node before
        self.parent_node = {}      

        self.StartPoint =  RobotPos
        self.TargetPoint = TargetPos

        # obstacles list passed by the simulation.py
        self.obstacle_list = Obstacles

        self.ObsWeight: int = 50
        self.Weight: int = 1

        self.moves = [
            (1,0), # dx
            (-1,0), # sx
            (0,1), # up
            (0,-1), #down
            '''
            Diagonal Movement
            (1,1), # dx - up
            (1,-1), # dx - down
            (-1,1), # sx - up
            (-1,-1) # sx - down
            '''
        ]
    #
    def search(self):
        totWeight, lastWeight = 0, 0

        # insert start-point in the queue
        self.queue.put(self.StartPoint)

        # start-point is visited
        self.visited.add(self.StartPoint)

        # start-point has no parent node
        self.parent_node[self.StartPoint] = None

        # until queue is not empty
        while not self.queue.empty():

            # get First In node as current
            current = self.queue.get()

            # if current is the target, reconstruct the path
            if current == self.TargetPoint:
                self.buildPath()

            # check every node near the current node
            for neighbor in self.getNeighbors(current):

                lastWeight = totWeight

                if neighbor in self.obstacle_list:
                    totWeight += self.ObsWeight

                # check if current node is visited
                if neighbor not in self.visited and totWeight - lastWeight < 1:
                    totWeight += self.Weight

                    # add current in visited
                    self.visited.add(neighbor)

                    # connect current as parent to his neighbors
                    self.parent_node[neighbor] = current

                    # add current in the queue
                    self.queue.put(neighbor)

        # Target-Point can't be reached
        return None
    #
    def getNeighbors(self, node: tuple):

        # break down the current node tuple (x, y) into two separate values
        # 1° case => x, y = (0, 0)
        x, y = node

        # neighbors list
        neighbors: list = []

        # cycle for every pair of (x,y) tuple in self.moves
        for dir_x, dir_y in self.moves:
            
            # calculate new node coordinates
            node_x, node_y = x + dir_x, y + dir_y

            # append node (x,y) pos as tuple
            neighbors.append((node_x, node_y))

            #TODO: need to add a check for the node (x,y) pos [inside/outside] the map
            '''
            if 0 <= node_x < self.w and 0 <= node_y < self.h:
                neighbors.append((node_x, node_y))
            '''

        # return all the neighbors
        return neighbors
    #
    def buildPath(self): # build the path using the parent_node dict
        path = []

        current = self.TargetPoint

        # build the path starting from the end to the start
        while current is not None:

            # append node (x,y) pos from the end_point
            path.append(current)

            # next_current = last - 1 node
            current = self.parent_node[current]
        
        # now the path goes from start to end
        path.reverse()

        return path
#