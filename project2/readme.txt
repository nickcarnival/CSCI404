1. Name and CSM ID of the student
Nicholas Carnival: 10798955
2. What programming language and what version of the compiler are used.
Python3 will not work with Python2
3. How the code is structred.
The maxConnect4.py has minor changes to the starter code so that includes the required functionality. 
The algorithms and funcitonality is all in MaxConnect4Game.py. maxConnect4Game.aiPlay() holds the initialization
functionality of the minimax algorithm. It calls depthABMiniMax() which finds the best possible value at the given depth.
It does this through the minValue and maxValue functions. These functions find all the valid game states and run the
minimax algorithm on each of these states. maxValue is where the evaluate function gets called from. The evaluate funcitonality
is my utility function. This function checks all of the almost complete connect 4's in the area and applies scalar weight
to them. This is how the ai is determining where to go. It tries to pursue routes that are already almost complete.
4. How to run the code, including very specific instruction, if compilation is needed. The output files computer.txt, and human.txt are located in the outputs directory.
Any specified output given during One-Move mode will not be in the outputs directory. 
python3 ./maxConnect4.py interactive [inputfile] [computer-next/player-next] [depth]
python3 ./maxConnect4.py one-move [inputfile] [outputfile] [depth]

run.sh has all of the test inputs that you gave us. It can be run by typing:

Interactive Mode:
./run.sh i 
One-Move Mode:
./run.sh o 