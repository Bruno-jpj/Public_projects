from queue import Queue  # Coda FIFO (First In, First Out)

class Bft:
    def __init__(self, h=20, w=20):
        # Altezza e larghezza della griglia
        self.h = h
        self.w = w

        # Coda usata dal BFS
        self.queue = Queue()

        # Set dei nodi già visitati (set è più veloce di una lista)
        self.visited = set()

        # Punto di partenza della ricerca
        self.StartPoint = (0, 0)

        # Punto di arrivo (facoltativo)
        self.EndPoint = None

    def get_neighbors(self, node):
        """
        Restituisce i vicini validi di un nodo (x, y)
        """
        x, y = node
        neighbors = []

        # Movimenti possibili: destra, sinistra, su, giù
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            # Controllo che il vicino sia dentro la griglia
            if 0 <= nx < self.w and 0 <= ny < self.h:
                neighbors.append((nx, ny))

        return neighbors

    def search(self):
        """
        Algoritmo Breadth-First Traversal
        """

        # Inserisco il punto di partenza nella coda
        self.queue.put(self.StartPoint)

        # Segno il nodo iniziale come visitato
        self.visited.add(self.StartPoint)

        # Finché la coda non è vuota
        while not self.queue.empty():

            # Estraggo il primo elemento dalla coda
            current = self.queue.get()

            # Se ho definito un EndPoint e l'ho raggiunto
            if current == self.EndPoint:
                break

            # Per ogni vicino del nodo corrente
            for neighbor in self.get_neighbors(current):

                # Se non è stato ancora visitato
                if neighbor not in self.visited:
                    # Lo marco come visitato
                    self.visited.add(neighbor)

                    # Lo aggiungo alla coda
                    self.queue.put(neighbor)

        # Restituisco tutti i nodi visitati
        return self.visited


# Creazione dell'oggetto BFT
bft = Bft()

# Avvio della ricerca
visited_nodes = bft.search()

# Stampo quanti nodi sono stati visitati
print(len(visited_nodes))