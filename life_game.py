# NOTE: all the arguments must be given only in the order described in README.md;
# passing it in a different order causes problems.


import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# The given data is loaded and checked
M = np.load(sys.argv[1])
for i in np.nditer(M):
    if i != 0 and i != 1:
        sys.exit("Incorrect initial state matrix (parameter 1): should contain only values (0, 1)")
S = np.load(sys.argv[2])
E = np.load(sys.argv[3])
if E.ndim != 1:
    sys.exit("Invalid parameter 3: should be a vector")
for i in np.nditer(E):
    if i != 0 and i != 1:
        sys.exit("Invalid vector of evolution rules (parameter 3): should contain only values (0, 1)")
steps = int(sys.argv[4])
if steps < 0:
    sys.exit("Invalid parameter 4: the number of simulation steps should be positive")


# a function that generates successive states
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


# presenting the results in an animation using the 'FuncAnimation' function
fig, ax = plt.subplots()
mat = ax.matshow(M)
ani = animation.FuncAnimation(fig, life, frames=steps, blit=True)

# Performing the result
if len(sys.argv) == 6 and sys.argv[5] == 'yes':
    ani.save('life1.mp4')
else:
    plt.show()

