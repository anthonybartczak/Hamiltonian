from examples import Examples
from numpy import zeros
from os import system

size = (5, 5)
temp_mtx = zeros(size, dtype=int)
dict_mtx = {}

for vertices in range(5):
#pętla przechodząca przez kolumny
    while True:
        adjacent = input(
            "Podaj wierzchołki graniczące z wierzchołkiem "
            + str(vertices)
            + "\nKolejne wierzchołki podawaj w formacie abc"
            + "\nWpisz koniec jeśli skończyłeś wpisywać: ")
        dict_mtx[vertices] = adjacent
        print(dict_mtx)
        break

# ======================================================================================================================


def dictIntoMtx(dictionary, matrix):

    for k in dictionary.keys():
        for l in dictionary.get(k):
            matrix[k][int(l)] = 1

    return matrix

dictIntoMtx(dict_mtx, temp_mtx)
print(temp_mtx)










