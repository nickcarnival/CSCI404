#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import sys
from MaxConnect4Game import *

def oneMoveGame(currentGame):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print('BOARD FULL\n\nGame Over!\n') 
        sys.exit(0)
        currentGame.aiPlay(0) # Make a move (only random is implemented)
    
    print('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()

def interactiveGame(currentGame, first, outFile):
    # TODO: Implement these steps

    while currentGame.pieceCount != 42:
        # 1. If computer-next, goto 2
        if first == 'computer-next':
            # 2. Print the current board state and score. if the board is full,  exit.
            currentGame.printGameBoard()
            # 3. Choose and make the next move.
            currentGame.aiPlay(0)
            # 4. Save the current board state in a file called computer.txt (in same format as input file).
            currentGame.printGameBoardToFile("computer")
            first = 'player-next'
        # 1. else goto 5
        elif first == 'player-next':
            # 5. Print the current board state and score. If the board is full, exit
            # 6. Ask the human user to make a move (make sure that the move is valid, otherwise repeat request to the user).
            # 7. Save the current board state in a file called human.txt (in same format as input file).
            # 8. goto 2
            currentGame.printGameBoardToFile()

        # TODO: check if this is valid
        userChoice = int(input("Which column would you like to place your piece in? \n")) - 1 
        currentGame.playPiece(userChoice)
        first = 'computer-next'
    
    print('BOARD FULL\n\nGame Over!\n') 
    sys.exit(0)

def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print('\nMaxConnect-4 game\n')
    print('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        firstPlayer = argv[3]
        outFile = open("computer.txt", "w")

        interactiveGame(currentGame, firstPlayer, outFile) 

        close(outFile)
    elif game_mode == 'one-move':
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile= open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)
