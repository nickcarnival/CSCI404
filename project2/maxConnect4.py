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

    currentGame.aiPlay(0) 
    
    print('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile("out")

def validateInput(userInput):
    try:
        userIntput = int(userInput)
    except ValueError:
        print("Not a valid number.")
        return -1
    return 0

def interactiveGame(currentGame, first):

    while currentGame.pieceCount != 42:

        # Step 2 
        currentGame.printGameBoard()

        # Step 1
        if first == 'computer-next':
            # Step 3 
            currentGame.aiPlay(0)
            # 4. Save the current board state in a file called computer.txt (in same format as input file).
            currentGame.computerFile = open("./outputs/computer.txt", "w")
            currentGame.printGameBoardToFile("computer")
            currentGame.computerFile.close()
            first = 'player-next'
        # Step 1
        elif first == 'player-next':
            #goto 5
            # 8. goto 2
            # Step 6
            userChoice = input("Which column would you like to place your piece in? \n") 
            while validateInput(userChoice) != 0:
                userChoice = input("Which column would you like to place your piece in? \n") 
            
            cannotPlayPiece = currentGame.playPiece(int(userChoice) - 1)
            while cannotPlayPiece:
                print("The column you selected in not valid.")
                newChoice = input("Which column would you like to place your piece in? \n") 
                # if valid choice
                if not validateInput(newChoice):
                    cannotPlayPiece = currentGame.playPiece(int(newChoice) - 1)

            # Step 7: save the current state
            currentGame.humanFile = open("./outputs/human.txt", "w")
            currentGame.printGameBoardToFile("human")
            currentGame.humanFile.close()

            # Step 8
            first = 'computer-next'

        currentGame.changeTurn()
    currentGame.clean()


    
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

        interactiveGame(currentGame, firstPlayer) 
    elif game_mode == 'one-move':
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.outFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)