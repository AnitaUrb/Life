# README:
# Dane wejściowe muszą być w podane tylko w takiej kolejności:
# M - inicjalny stan macierzy stanu, S - macierz sąsiedztwa, E - wektor reguł ewolucji, steps - liczba kroków symulacji
# (tylko w takiej z uwagi na różne możliwe postaci macierzy, co robi rozpoznawanie ich (bez kolejności) bardzo
# uciążliwym). Jako output w bieżącym katalogu powstanie plik "life.mp4" i zostanie wyświetlony kawałek animacji.
# Również (jeżli możemy rozszerzyć input wskazany w zadaniu) wygodne by było pobieranie dodatkowego 4. parametru
# 'tak/nie', odpowiadającego za to, czy będzie wynik symulacji zapisany w "life.mp4" (opcja 'tak'), czy będzie
# tylko wyświetlony (opcja 'nie'); wtedy należałoby odkomentować linie 54-55 i zakomentować 57.
# materials:
# https://stackoverflow.com/questions/41827109/funcanimation-with-a-matrix
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.matshow.html


import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#pobrane parametry są wczytywane i sprawdzane (na poprawność)
M = np.load(sys.argv[1])
for i in np.nditer(M):
    if i != 0 and i != 1:
        sys.exit("Niepoprawna inicjalna macierz stanu (parametr 1): ma zawierać tylko wartości (0, 1)")
S = np.load(sys.argv[2])
E = np.load(sys.argv[3])
if E.ndim != 1:
    sys.exit("Niepoprawny parametr 3: ma być wektorem")
for i in np.nditer(E):
    if i != 0 and i != 1:
        sys.exit("Niepoprawny wektor reguł ewolucji (parametr 3): ma zawierać tylko wartości (0, 1)")
steps = int(sys.argv[4])
if steps < 0:
    sys.exit("Niepoprawny parametr 4: liczba kroków symulacji ma być dodatnia")


#funkcja generująca kolejne stany
def life(n):
    global M
    newM = M.copy()
    dim = np.shape(M)
    for i in range(1, dim[0] - 1):
        for j in range(1, dim[1] - 1):
            newM[i, j] = E[int(np.sum(M[i - 1:i + 2, j - 1:j + 2] * S))]
    mat.set_data(newM)
    M = newM
    return [mat]


#przedstawienie wyników w animacji za pomocą funkcji 'FuncAnimation'
fig, ax = plt.subplots()
mat = ax.matshow(M)
ani = animation.FuncAnimation(fig, life, frames=steps, blit=True)

# if sys.argv[5] == 'tak':
#     ani.save('life.mp4')

ani.save('life.mp4')
plt.show()
