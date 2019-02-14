from Node import Node
import math
import sys
import time
from console.utils import cls, set_title
from console import fg, bg, fx

def stringSignOf(number):
    if(number < 0):
        return "-"
    else:
        return "+"

def pieceFormat(pieces):
    s = ""
    s = str(pieces)
    if(len(s) < 2):
        s = "0" + s
    return s

def printBoard(board):
    print("   -----\n" +
          "0 |  " + pieceFormat(board[0]) + " | 0\n" +
          "1 |" + pieceFormat(board[1]) + "|" + pieceFormat(board[13]) + "| 13\n" +
          "2 |" + pieceFormat(board[2]) + "|" + pieceFormat(board[12]) + "| 12\n" +
          "3 |" + pieceFormat(board[3]) + "|" + pieceFormat(board[11]) + "| 11\n" +
          "4 |" + pieceFormat(board[4]) + "|" + pieceFormat(board[10]) + "| 10\n" +
          "5 |" + pieceFormat(board[5]) + "|" + pieceFormat(board[9]) + "| 9\n" +
          "6 |" + pieceFormat(board[6]) + "|" + pieceFormat(board[8]) + "| 8\n" +
          "7 |  " + pieceFormat(board[7]) + " | 7\n" +
          "   -----")

def minimax(node, depth):
    if(depth == 0 or node.isTerminal()):
        return node.getScore()
    if(node.playerTurn):
        value = -(math.inf)
        for child in node.getChildren():
            value = max(value, minimax(child, depth-1))
        return value
    else:
        value = math.inf
        for child in node.getChildren():
            value = min(value, minimax(child, depth-1))
        return value

def getBestMove(node, depth):
    children = node.getChildren()
    bestChild = None
    bestChildValue = -(math.inf)
    for child in children:
        value = minimax(child, depth)
        if(value > bestChildValue):
            bestChild = child
            bestChildValue = value
    move = node.getValidMoves()[children.index(bestChild)]
    print("Minimax eval (" + stringSignOf(bestChildValue) + str(math.fabs(bestChildValue)) + "). Best move (depth=" + str(depth) + "): " + str(move))

def getTimedBestMove(node, startDepth, maxTime, maxDepth):
    startTime = time.clock()
    depth = startDepth
    bestMove = None
    while(depth <= maxDepth and (time.clock() < startTime + maxTime)):
        bestMove = getBestMove(node, depth)
        depth += 1
    return bestMove

def main():
    set_title("AlphaMancala v1.0");
    startingPosition = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
    node = Node(startingPosition, True)
    while(True):
        cls()
        printBoard(node.board)
        if(node.playerTurn):
            print("\nTurn: player")
            getTimedBestMove(node, 2, 5, 20)
        else:
            print("\nTurn: computer")
        move = input("move: ")
        move = int(move)
        node.makeMove(move)

main()