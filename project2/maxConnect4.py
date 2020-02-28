#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega
# edited by Nicholas Carnival to be
# Python 3 compatible

from MaxConnect4Game import *

import os
import sys

def oneMoveGame(currentGame, depth):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    currentGame.aiPlay(int(depth))

    print('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile("out")
    currentGame.outFile.close()

def interactiveGame(currentGame, depth, nextPlayer, inFile):

    # Step 5
    if nextPlayer == "human-next":
        while currentGame.checkPieceCount() != 42:
            try:
                userMove = int(input("Which column would you like to play your piece in? ( 1-7 )?\n "))
            except ValueError:
                print("Not a number")
                continue
            if not userMove in range(8):
                print("Invalid column number!")
                continue
            if not currentGame.playPiece(userMove - 1):
                print("This column is full!")
                continue

            if os.path.exists(inFile):
                currentGame.gameFile = open(inFile, 'r')
            else:
                sys.exit("\nError opening input file.\nCheck file name.\n")

            print("Your Move:")
            currentGame.printGameBoard()
            currentGame.printGameBoardToFile("human")
            if currentGame.checkPieceCount() != 42:
                if currentGame.currentTurn == 1: currentGame.currentTurn = 2
                elif currentGame.currentTurn == 2: currentGame.currentTurn = 1
                currentGame.aiPlay(int(depth))
                print("Computer's Move:")
                currentGame.printGameBoard()
                currentGame.printGameBoardToFile("computer")
                currentGame.countScore()
                print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    else:
        currentGame.aiPlay(int(depth))
        currentGame.printGameBoard()
        currentGame.printGameBoardToFile("computer")
        currentGame.countScore()
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        interactiveGame(currentGame, depth, "human-next", inFile)

    if currentGame.checkPieceCount() == 42:    # Is the board full already?
        print('BOARD FULL\n\nGame Over!\n')

    currentGame.countScore()

    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    
    sys.exit(0)



def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print('Four command-line arguments are needed:')
        print('Usage: \'python3 %s interactive [input_file] [computer-next/human-next] [depth]\'' % argv[0])
        print('or: \'python3 %s one-move [input_file] [output_file] [depth]\'' % argv[0])
        sys.exit(-1)

    game_mode, inFile, nextPlayer, depth = argv[1:5]

    if game_mode != 'interactive' and game_mode != 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(-1)

    currentGame = MaxConnect4Game() # Create a game

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

    print('\nWelcome to MaxConnect-4\n\n')
    input("Press ENTER to continue...")
    print(chr(27) + "[2J")
    print('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        interactiveGame(currentGame, depth, nextPlayer, inFile) 
    else:
        outFile = argv[3]
        try:
            currentGame.outFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame, depth) 

if __name__ == "__main__": main(sys.argv)
