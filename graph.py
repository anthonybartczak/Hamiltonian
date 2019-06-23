class Graph:
    def __init__(self, vertices):

        self.graph = [[0 for column in range(vertices)]
                         for row in range(vertices)]

        self.V = vertices

    def isSafe(self, v, pos, path):

        """ Sprawdź czy dany wierzchołek jest przylegający i się nie powtórzył """

        if self.graph[path[pos-1]][v] == 0:
            return False

        for vertex in path:
            if vertex == v:
                return False

        return True

# ======================================================================================================================

    def hamCycleUtil(self, path, pos):

        """ Algorytm rozwiązujący """

        if pos == self.V:
            if self.graph[path[pos-1]][path[0]] == 1:
                return True
            else:
                return False

        for v in range(1, self.V):
            if self.isSafe(v, pos, path) is True:
                path[pos] = v

                if self.hamCycleUtil(path, pos+1) is True:
                    return True

                path[pos] = -1
        return False

# ======================================================================================================================

    def hamCycle(self):

        """ Ustaw początkowy wierzchołek jako 0. Jeśli cykl istnieje,
            ścieżka może zostać rozpoczęta od dowolnego wierchołka """

        path = [-1] * self.V
        path[0] = 0

        if self.hamCycleUtil(path, 1) is False:
            print('Ścieżka nie istnieje!\n')
            return False

        self.printSolution(path)
        return True

# ======================================================================================================================

    def printSolution(self, path):

        """ Pokaż wynik """

        print('Istnieje ścieżka:')
        for vertex in path:
            print(vertex)
        print(path[0], "\n")