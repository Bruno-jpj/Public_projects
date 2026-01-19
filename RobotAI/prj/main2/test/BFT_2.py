from queue import Queue
import random as r

class Bft:
    def __init__(self):
        self.h = 20
        self.w = 20

        self.visited = set()
        self.queue = Queue()

        self.parent: dict = {}

        self.StartPoint: tuple = (0,0)
        self.EndPoint: tuple = (5,7)

        self.Obstacles: list = [(4,0), (5,6), (3,1), (2,5), (4,7), (7,0), (3,3)]
        
        self.ObsWeight: int = 50
        self.Weight: int = 1

        # self.insertObstacles()
    #
    def insertObstacles(self):
        obj = 10
        for _ in range(obj):
            x = r.randint(1, 20)
            y = r.randint(1, 20)
            #
            self.Obstacles.append((x,y))
            #
        return self.Obstacles
    #
    def getNeighbors(self, node) -> list:
        x,y = node
        neighbors: list = []

        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        for dir_x, dir_y in moves:
            node_x, node_y = x + dir_x, y + dir_y
            if 0 <= node_x < self.w and 0 <= node_y < self.h:
                neighbors.append((node_x, node_y))

        return neighbors
    #
    def search(self):
        totWeight = 0
        lastWeight = 0

        self.queue.put(self.StartPoint)
        self.visited.add(self.StartPoint)
        
        self.parent[self.StartPoint] = None

        while not self.queue.empty():
            current = self.queue.get()

            if current == self.EndPoint:
                return self.buildPath()
            
            for neighbor in self.getNeighbors(current):
                lastWeight = totWeight

                if neighbor in self.Obstacles:
                    totWeight += self.ObsWeight

                if neighbor not in self.visited and totWeight - lastWeight < 1:
                    totWeight += self.Weight

                    self.visited.add(neighbor)
                    self.parent[neighbor] = current
                    self.queue.put(neighbor)

        return None
    #
    def buildPath(self):
        path = []
        current = self.EndPoint

        while current is not None:
            path.append(current)
            current = self.parent[current]

        path.reverse()

        return path
    #
# ====== ESEMPIO DI USO ======

bft = Bft()
path = bft.search()

if path:
    print("Percorso trovato:")
    print(path)
else:
    print("EndPoint non raggiungibile")
#