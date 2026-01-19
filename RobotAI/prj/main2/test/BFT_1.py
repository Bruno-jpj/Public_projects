from queue import Queue
import random as r

class Bft:
    def __init__(self, h=20, w=20):
        self.h = h
        self.w = w

        self.queue = Queue()
        self.visited = set()

        # Dizionario: nodo → nodo precedente
        self.parent = {}

        self.StartPoint = (0, 0)
        self.EndPoint = (5, 7)

        self.ObstaclesList: list = []
    #
    def get_neighbors(self, node):
        """
        Restituisce i vicini validi del nodo (x, y)
        """
        x, y = node
        neighbors = []

        moves = [(1,0), (-1,0), (0,1), (0,-1)]
        # moves = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.w and 0 <= ny < self.h:
                neighbors.append((nx, ny))

        return neighbors
    #
    def search(self):
        """
        BFS con EndPoint
        """
        self.queue.put(self.StartPoint)
        self.visited.add(self.StartPoint)

        # Il nodo di partenza non ha genitore
        self.parent[self.StartPoint] = None

        while not self.queue.empty():
            current = self.queue.get()

            # Se ho raggiunto l'EndPoint, posso fermarmi
            if current == self.EndPoint:
                return self.reconstruct_path()

            for neighbor in self.get_neighbors(current):
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    self.parent[neighbor] = current
                    self.queue.put(neighbor)

        # EndPoint non raggiungibile
        return None
    #
    def insertObstacles(self):
        obj = 10
        for _ in range(obj):
            x = r.randint(1, 20)
            y = r.randint(1, 20)
            #
            self.ObstaclesList.append((x,y))
            #
        return self.ObstaclesList
    #
    def checkPath(self):
        setObstacles = set(self.ObstaclesList)

        for tupla in self.fPath:
            if tupla in setObstacles:
                return f"Obstacle in the path [{tupla}]"
        return f"No Obstacles in the path"
    #
    def reconstruct_path(self):
        """
        Ricostruisce il percorso minimo usando parent
        """
        path = []
        current = self.EndPoint

        while current is not None:
            path.append(current)
            current = self.parent[current]

        # Il percorso va dall'EndPoint allo Start → lo invertiamo
        path.reverse()

        self.fPath = path.copy() # copy of the path

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

print(bft.insertObstacles())
print(bft.checkPath())

for x,y in path:
    print(f"X: [{x}] | Y:[{y}]")