from examples import Examples
from numpy import zeros
from os import system


class Graph():
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

    def hamCycle(self):

        """ Ustaw początkowy wierzchołek jako 0. Jeśli cykl istnieje,
            ścieżka może zostać rozpoczęta od dowolnego wierchołka """

        path = [-1] * self.V
        path[0] = 0

        if self.hamCycleUtil(path, 1) is False:
            print('Solution does not exist\n')
            return False

        self.printSolution(path)
        return True

    def printSolution(self, path):

        """ Pokaż wynik """

        print('Istnieje ścieżka:')
        for vertex in path:
            print(vertex)
        print(path[0], "\n")


choice = input("Czy chcesz użyć gotowego przykładu? tak/nie: ")

if choice == "tak":

    ex_num = input("Wybierz numer przykładu ( np. e1, e2 ): ")

    if hasattr(Examples(), ex_num) is True:
        g = Graph(5)
        g.graph = getattr(Examples(), ex_num)
        g.hamCycle()
    else:
        print("Przykład niedostępny.")

elif choice == "nie":

    ver_num = input("Podaj liczbę wierzchołków: ")
    ver_num = int(ver_num)

    if ver_num == 0:
        print("Graf nie może mieć 0 wierzchołków!")

    else:
        size = (ver_num, ver_num)
        temp_mtx = zeros(size, dtype=int)
        dict_mtx = {}

        for vertices in range(ver_num):
            dict_mtx[vertices] = ''
            print(dict_mtx)

        for vertices in range(ver_num):
            loop = True
            while loop is True:
                adjacent = input(
                    "Podaj wierzchołki graniczące z wierzchołkiem "
                    + str(vertices)
                    + "\nKolejne wierzchołki podawaj rosnąco, po spacji "
                    + "\nWpisz koniec jeśli skończyłeś wpisywać: ")

                if adjacent == "koniec":
                    system("cls")
                    print("Kończę dla wierzchołka " + str(vertices) + "\n")
                    loop = False
                else:











