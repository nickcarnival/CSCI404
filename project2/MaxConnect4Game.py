#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Vassilis Athitsos
# Written to be Python 2.4 compatible 
# edited by Nicholas Carnival to be
# Python 3 compatible

from copy import deepcopy

class MaxConnect4Game:
    def __init__(self):
        self.gameBoard = [[0 for i in range(7)] for j in range(6)]
        self.currentTurn = 1
        self.player1Score = 0
        self.player2Score = 0
        self.computerTurn = 0
        self.humanTurn = 0
        self.pieceCount = 0
        self.gameFile = None
        self.humanFile = None
        self.computerFile = None
        self.outFile = None
        self.previousColumn= None

    def evaluate(self, board):
        if self.currentTurn == 2:
            other = 1
            connect4 = self.player2Score - self.player1Score
        elif self.currentTurn == 1:
            other = 2
            connect4 = self.player1Score - self.player2Score
        # Count progress for threes and twos
        connect2 = self.possibleOutcomes(board, self.currentTurn, 2) - self.possibleOutcomes(board, other, 2)
        connect3 = self.possibleOutcomes(board, self.currentTurn, 3) - self.possibleOutcomes(board, other, 3)

        return (connect4 * 8 + connect3 * 4 + connect2 * 2)

    def almostConnected(self, row, col, state, length):
        grandTotal = 0
        count = 0
        # count all the almost complete verticals 
        for i in range(row, 6):
            if state[i][col] == state[row][col]: count += 1
            else: break

        if count >= length: grandTotal += 1

        # count all the almost complete horizontals
        count = 0
        for j in range(col, 7):
            if state[row][j] == state[row][col]: count += 1
            else: break

        if count >= length: grandTotal += 1

        # count all the almost complete diagonals
        total = 0
        count = 0
        tempCol = col
        for i in range(row, 6):
            if tempCol > 6: break
            elif state[i][tempCol] == state[row][col]: count += 1
            else: break
            tempCol += 1  

        if count >= length: total += 1

        # check for diagonals with negative slope
        count = 0
        tempCol = col
        for i in range(row, -1, -1):
            if tempCol > 6: break
            elif state[i][tempCol] == state[row][col]: count += 1
            else: break
            tempCol += 1  # increment column when row is incremented

        if count >= length: total += 1

        grandTotal += total
        return grandTotal

    def possibleOutcomes(self, state, other, length):
        count = 0
        # for each coin currently in the board
        for i in range(6):  # for each row
            for j in range(7):  # for each column of that row
                if state[i][j] == other:
                    sum = self.almostConnected(i, j, state, length)
        return count

    def checkPieceCount(self):
        count = 0
        for row in self.gameBoard:
            for piece in row:
                if piece: count += 1
        return count

    # Output current game status to console
    def printGameBoard(self):
        print(' -----------------')
        for i in range(6):
            print(' |', end=" ")
            for j in range(7):
                print('%d' % self.gameBoard[i][j], end=" "),
            print('| ')
        print(' -----------------')

    def printGameBoardToFile(self, name):
        if name == "computer":
            self.computerFile = open("./outputs/computer.txt", "w")
            for row in self.gameBoard:
                self.computerFile.write(''.join(str(col) for col in row) + '\r\n')
            self.computerFile.write('%s\r\n' % str(self.currentTurn))
            self.computerFile.close()
        elif name == "human":
            self.humanFile = open("./outputs/human.txt", "w")
            for row in self.gameBoard:
                self.humanFile.write(''.join(str(col) for col in row) + '\r\n')
            self.humanFile.write('%s\r\n' % str(self.currentTurn))
            self.humanFile.close()
        else:
            for row in self.gameBoard:
                self.outFile.write(''.join(str(col) for col in row) + '\r\n')
            self.outFile.write('%s\r\n' % str(self.currentTurn))

    # Place the current player's piece in the requested column
    def playPiece(self, column):
        #print column
        if not self.gameBoard[0][column]:
            for i in range(5, -1, -1):
                if not self.gameBoard[i][column]:
                    self.gameBoard[i][column] = self.currentTurn
                    self.pieceCount += 1
                    return 1
        return 0

    def checkPiece(self, column, other):
        if not self.gameBoard[0][column]:
            for i in range(5, -1, -1):
                if not self.gameBoard[i][column]:
                    self.gameBoard[i][column] = other
                    self.pieceCount += 1
                    return 1
        return 0


    # has the ai use minimax with depth and ab pruning to choose its next move
    def aiPlay(self, depth):
        column = self.depthABMiniMax(depth)
        self.previousColumn = column
        result = self.playPiece(column)

        if self.currentTurn == 1: self.currentTurn = 2
        elif self.currentTurn == 2: self.currentTurn = 1

    #Minimax implementation with both Alpha-Beta Pruning and Depth Limit
    def depthABMiniMax(self, maxDepth):
        tempBoard = deepcopy(self.gameBoard)
        allValues = {}

        for i in range(7):
            if self.playPiece(i):
                if self.pieceCount == 42 or maxDepth == 0:
                    self.gameBoard = deepcopy(tempBoard)
                    return i
                else:
                    value = self.minValue(self.gameBoard, float('-inf'), float('inf'), maxDepth - 1)
                    allValues[i] = value
                    self.gameBoard = deepcopy(tempBoard)
                    
        bestVal = max([i for i in allValues.values()])

        # find the move associated with the bestVal
        for i in range(7):
            if i in allValues:
                if allValues[i] == bestVal:
                    allValues.clear()
                    return i

    def minValue(self, board, alpha, beta, maxDepth):
        originalCopy = deepcopy(board)
        if self.currentTurn == 1: other = 2
        else: other = 1 
        validStates = []

        for j in range(7):
            if self.checkPiece(j, other):
                # add that piece to the game board and save it
                validStates.append(self.gameBoard)
                # remove that piece from the gameBoard
                self.gameBoard = deepcopy(originalCopy)

        if validStates == [] or maxDepth == 0:
            self.countScore()
            return self.evaluate(self.gameBoard)
        else:
            # run the maximizing algorithm on the other board states
            for state in validStates:
                self.gameBoard = deepcopy(state)
                value = min(float('inf'), self.maxValue(state, alpha, beta, maxDepth - 1))

                if value <= alpha: return value

                beta = min(beta, value)
            return value

    def maxValue(self, gameBoard, alpha, beta, maxDepth):
        originalCopy = deepcopy(gameBoard)
        v = -float('inf')
        validStates = []
        for j in range(7):
            if self.playPiece(j):
                validStates.append(self.gameBoard)
                self.gameBoard = deepcopy(originalCopy)

        if validStates == [] or maxDepth == 0:
            self.countScore()
            return self.evaluate(self.gameBoard)
        else:
            for state in validStates:

                self.gameBoard = deepcopy(state)
                value = max(float('-inf'), self.minValue(state, alpha, beta, maxDepth - 1))

                if value >= beta: return value

                alpha = max(alpha, value)

            return value

    # Calculate the number of 4-in-a-row each player has
    def countScore(self):
        self.player1Score = 0
        self.player2Score = 0

        # Check horizontally
        for row in self.gameBoard:
            # Check player 1
            if row[0:4] == [1]*4:
                self.player1Score += 1
            if row[1:5] == [1]*4:
                self.player1Score += 1
            if row[2:6] == [1]*4:
                self.player1Score += 1
            if row[3:7] == [1]*4:
                self.player1Score += 1
            # Check player 2
            if row[0:4] == [2]*4:
                self.player2Score += 1
            if row[1:5] == [2]*4:
                self.player2Score += 1
            if row[2:6] == [2]*4:
                self.player2Score += 1
            if row[3:7] == [2]*4:
                self.player2Score += 1

        # Check vertically
        for j in range(7):
            # Check player 1
            if (self.gameBoard[0][j] == 1 and self.gameBoard[1][j] == 1 and
                   self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][j] == 1 and self.gameBoard[2][j] == 1 and
                   self.gameBoard[3][j] == 1 and self.gameBoard[4][j] == 1):
                self.player1Score += 1
            if (self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1 and
                   self.gameBoard[4][j] == 1 and self.gameBoard[5][j] == 1):
                self.player1Score += 1
            # Check player 2
            if (self.gameBoard[0][j] == 2 and self.gameBoard[1][j] == 2 and
                   self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][j] == 2 and self.gameBoard[2][j] == 2 and
                   self.gameBoard[3][j] == 2 and self.gameBoard[4][j] == 2):
                self.player2Score += 1
            if (self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2 and
                   self.gameBoard[4][j] == 2 and self.gameBoard[5][j] == 2):
                self.player2Score += 1

        # Check diagonally

        # Check player 1
        if (self.gameBoard[2][0] == 1 and self.gameBoard[3][1] == 1 and
               self.gameBoard[4][2] == 1 and self.gameBoard[5][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][0] == 1 and self.gameBoard[2][1] == 1 and
               self.gameBoard[3][2] == 1 and self.gameBoard[4][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][1] == 1 and self.gameBoard[3][2] == 1 and
               self.gameBoard[4][3] == 1 and self.gameBoard[5][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][0] == 1 and self.gameBoard[1][1] == 1 and
               self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][1] == 1 and self.gameBoard[2][2] == 1 and
               self.gameBoard[3][3] == 1 and self.gameBoard[4][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1 and
               self.gameBoard[4][4] == 1 and self.gameBoard[5][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][1] == 1 and self.gameBoard[1][2] == 1 and
               self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][2] == 1 and self.gameBoard[2][3] == 1 and
               self.gameBoard[3][4] == 1 and self.gameBoard[4][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1 and
               self.gameBoard[4][5] == 1 and self.gameBoard[5][6] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][2] == 1 and self.gameBoard[1][3] == 1 and
               self.gameBoard[2][4] == 1 and self.gameBoard[3][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][3] == 1 and self.gameBoard[2][4] == 1 and
               self.gameBoard[3][5] == 1 and self.gameBoard[4][6] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][3] == 1 and self.gameBoard[1][4] == 1 and
               self.gameBoard[2][5] == 1 and self.gameBoard[3][6] == 1):
            self.player1Score += 1

        if (self.gameBoard[0][3] == 1 and self.gameBoard[1][2] == 1 and
               self.gameBoard[2][1] == 1 and self.gameBoard[3][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][4] == 1 and self.gameBoard[1][3] == 1 and
               self.gameBoard[2][2] == 1 and self.gameBoard[3][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][3] == 1 and self.gameBoard[2][2] == 1 and
               self.gameBoard[3][1] == 1 and self.gameBoard[4][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][5] == 1 and self.gameBoard[1][4] == 1 and
               self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][4] == 1 and self.gameBoard[2][3] == 1 and
               self.gameBoard[3][2] == 1 and self.gameBoard[4][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1 and
               self.gameBoard[4][1] == 1 and self.gameBoard[5][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][6] == 1 and self.gameBoard[1][5] == 1 and
               self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][5] == 1 and self.gameBoard[2][4] == 1 and
               self.gameBoard[3][3] == 1 and self.gameBoard[4][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1 and
               self.gameBoard[4][2] == 1 and self.gameBoard[5][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][6] == 1 and self.gameBoard[2][5] == 1 and
               self.gameBoard[3][4] == 1 and self.gameBoard[4][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][5] == 1 and self.gameBoard[3][4] == 1 and
               self.gameBoard[4][3] == 1 and self.gameBoard[5][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][6] == 1 and self.gameBoard[3][5] == 1 and
               self.gameBoard[4][4] == 1 and self.gameBoard[5][3] == 1):
            self.player1Score += 1

        # Check player 2
        if (self.gameBoard[2][0] == 2 and self.gameBoard[3][1] == 2 and
               self.gameBoard[4][2] == 2 and self.gameBoard[5][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][0] == 2 and self.gameBoard[2][1] == 2 and
               self.gameBoard[3][2] == 2 and self.gameBoard[4][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][1] == 2 and self.gameBoard[3][2] == 2 and
               self.gameBoard[4][3] == 2 and self.gameBoard[5][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][0] == 2 and self.gameBoard[1][1] == 2 and
               self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][1] == 2 and self.gameBoard[2][2] == 2 and
               self.gameBoard[3][3] == 2 and self.gameBoard[4][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2 and
               self.gameBoard[4][4] == 2 and self.gameBoard[5][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][1] == 2 and self.gameBoard[1][2] == 2 and
               self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][2] == 2 and self.gameBoard[2][3] == 2 and
               self.gameBoard[3][4] == 2 and self.gameBoard[4][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2 and
               self.gameBoard[4][5] == 2 and self.gameBoard[5][6] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][2] == 2 and self.gameBoard[1][3] == 2 and
               self.gameBoard[2][4] == 2 and self.gameBoard[3][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][3] == 2 and self.gameBoard[2][4] == 2 and
               self.gameBoard[3][5] == 2 and self.gameBoard[4][6] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][3] == 2 and self.gameBoard[1][4] == 2 and
               self.gameBoard[2][5] == 2 and self.gameBoard[3][6] == 2):
            self.player2Score += 1

        if (self.gameBoard[0][3] == 2 and self.gameBoard[1][2] == 2 and
               self.gameBoard[2][1] == 2 and self.gameBoard[3][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][4] == 2 and self.gameBoard[1][3] == 2 and
               self.gameBoard[2][2] == 2 and self.gameBoard[3][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][3] == 2 and self.gameBoard[2][2] == 2 and
               self.gameBoard[3][1] == 2 and self.gameBoard[4][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][5] == 2 and self.gameBoard[1][4] == 2 and
               self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][4] == 2 and self.gameBoard[2][3] == 2 and
               self.gameBoard[3][2] == 2 and self.gameBoard[4][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2 and
               self.gameBoard[4][1] == 2 and self.gameBoard[5][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][6] == 2 and self.gameBoard[1][5] == 2 and
               self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][5] == 2 and self.gameBoard[2][4] == 2 and
               self.gameBoard[3][3] == 2 and self.gameBoard[4][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2 and
               self.gameBoard[4][2] == 2 and self.gameBoard[5][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][6] == 2 and self.gameBoard[2][5] == 2 and
               self.gameBoard[3][4] == 2 and self.gameBoard[4][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][5] == 2 and self.gameBoard[3][4] == 2 and
               self.gameBoard[4][3] == 2 and self.gameBoard[5][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][6] == 2 and self.gameBoard[3][5] == 2 and
               self.gameBoard[4][4] == 2 and self.gameBoard[5][3] == 2):
            self.player2Score += 1
