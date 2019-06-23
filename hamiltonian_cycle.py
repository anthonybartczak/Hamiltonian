from examples import Examples
from numpy import zeros
from os import system
from graph import Graph

# ======================================================================================================================

def dictIntoMtx(dictionary, matrix):

    for k in dictionary.keys():
        for l in dictionary.get(k):
            matrix[k][int(l)] = 1

    return matrix

# ======================================================================================================================

def checkCycle(ver_num, matrix):

    g = Graph(ver_num)
    g.graph = matrix
    g.hamCycle()

# ======================================================================================================================

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

        print(
            "Kolejne wierzchołki podawaj w formacie abc."
            + "\nWpisz koniec jeśli skończyłeś wpisywać.")

        for vertices in range(ver_num):
            while True:
                adjacent = input( "Podaj wierzchołki graniczące z wierzchołkiem " + str(vertices) + "\n")
                dict_mtx[vertices] = adjacent
                print(dict_mtx)
                break

        # konwersja słownika w macierz
        dictIntoMtx(dict_mtx, temp_mtx)

        # sprawdzenie cyklu
        checkCycle(ver_num, temp_mtx)









