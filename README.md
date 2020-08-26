# Game of Life

The task was to write a program enabling to simulate [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) based on [cellular automaton](https://en.wikipedia.org/wiki/Cellular_automaton).

The rules of the game:<br />
- We consider automata with values 0 (dead cell) or 1 (living cell) in each of the cells of a rectangular matrix MxN
- We consider the [Moore neighborhood](https://en.wikipedia.org/wiki/Moore_neighborhood), i.e. each cell (except for the edge ones) has 8 neighbors.<br />

The rules of evolution:<br />
- If the cell is alive in step t, it remains alive in step t + 1, if it has 2 or 3 neighbors alive (otherwise it dies in step t + 1)
- if the cell is dead in step t, it remains dead in step t + 1 unless it has exactly 3 neighbors alive.<br />

In this case, the neighborhood will be represented as weight matrices, that is, square matrices of odd sizes (usually 3 × 3) 
and the rules of evolution as vectors. <br />

As an example of a game of life, we can consider the neighborhood matrix:
```
S=np.array([[1,1,1],[1,10,1],[1,1,1]])
```
and write the rule of evolution as:
```
E= np.zeros((18,),dtype=int8)
E[3]=1
E[12]=1
E[13]=1
```
Then we can compute a new state value in the matrix at position M [i, j] (for all "internal" i, j) as:
```
N[i,j]=E[np.sum(M[i-1:i+2,j-1:j+2]*S)]
```
Then the program performs such a simulation and performs the results as animation.<br />

To start the simulation: <br />

terminal:~$ *./path_to/life_game.py path_to/M path_to/S path_to/E steps_number yes_or_no*<br />

- *M* - initial state of the state matrix,
- *S* - neighborhood matrix,
- *E* - evolution vector, 
- *steps_number* - number of simulation steps,
- *yes_or_no* - additional argument responsible for whether the simulation result will be saved in "life.mp4" (option *'yes'*), or displayed only (any other option)<br />

All given files are checked for correctness, otherwise the appropriate messages are displayed.
Program uses input data in [.npy](https://numpy.org/devdocs/reference/generated/numpy.lib.format.html) format. Example input files:<br /> 
*matrix.npy (M), neighbor.npy (S), ewol.npy (E)*. Example incorrect initial state matrix: *matrice.npy*.<br />
Optimal number of steps: *30*. <br />
Example result of simulation: *life.mp4*.
