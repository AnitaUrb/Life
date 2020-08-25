# Game of Life

The task was to write a program enabling to simulate Conway's Game of Life based on cellular automaton. 

The rules of the game are as follows:<br />
- We consider automata with values 0 (dead cell) or 1 (living cell) in each of the cells of a rectangular matrix MxN
- We consider the Moore's neighborhood, i.e. each cell (except for the edge ones) has 8 neighbors.<br />
The rules of evolution:<br />
- If the cell is alive in step t, it remains alive in step t + 1, if it has 2 or 3 neighbors alive (otherwise it dies in step t + 1)
- if the cell is dead in step t, it remains dead in step t + 1 unless it has exactly 3 neighbors alive.<br />

In this case, the neighborhood will be represented as weight matrices, that is, square matrices of odd sizes (usually 3 × 3) 
and the rules of evolution as vectors. <br />
For example, as an example of a game of life, we can consider the neighborhood matrix:

S=np.array([[1,1,1],[1,10,1],[1,1,1]])
and write the rule of evolution as:

E= np.zeros((18,),dtype=int8)
E[3]=1
E[12]=1
E[13]=1

Then we can compute a new state value in the matrix at position M [i, j] (for all "internal" i, j) as:

N[i,j]=E[np.sum(M[i-1:i+2,j-1:j+2]*S)]
The program takes as parameters:

- the size of the state of the automaton in the form of a vector
- weight matrix in the form of a matrix to be loaded by e.g. load ()
- vector rules of evolution
- The initial state of the state matrix
- the number of simulation steps to be performed.

Then the program performs such a simulation and saves the results as animation.

More information about https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life and https://en.wikipedia.org/wiki/Cellular_automaton.
