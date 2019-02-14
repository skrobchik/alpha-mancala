# 7  6  5  4  3  2  1  0
# 7  8  9 10 11 12 13  0

class Node(object):
    def __init__(self, board, playerTurn):
        self.board = board
        self.playerTurn = playerTurn
        pass

    def getScore(self):
        return self.board[0] - self.board[7]

    def getValidMoves(self):
        validMoves = list()
        for i in range(0, 14):
            if(self.board[i] > 0 and i is not self.allyHole() and i is not self.enemyHole() and self.isOnMySide(i)):
                validMoves.append(i)
        return validMoves    

    def isOnMySide(self, holeIndex):
        mySideMin = 8
        mySideMax = 13
        if(not self.playerTurn):
            mySideMin -= 7
            mySideMax -= 7
        return (holeIndex in range(mySideMin, mySideMax+1))

    def isTerminal(self):
        validMoves = self.getValidMoves()
        return (len(validMoves) == 0)

    def getChildren(self):
        validMoves = self.getValidMoves()
        children = list()
        for move in validMoves:
            child = Node(self.board.copy(), self.playerTurn)
            child.makeMove(move)
            children.append(child)
        return children

    def enemyHole(self):
        if(self.playerTurn):
            return 7
        else:
            return 0
    def adjacentHole(self, holeIndex):
        adjacentMap = [0, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        return adjacentMap[holeIndex]

    def allyHole(self):
        if(self.playerTurn):
            return 0
        else:
            return 7

    def makeMove(self, holeIndex):
        pieces = self.board[holeIndex]
        self.board[holeIndex] = 0
        while(pieces > 0):
            holeIndex += 1
            if(holeIndex > 13):
                holeIndex = 0
            if(holeIndex == self.enemyHole()):
                holeIndex += 1
            self.board[holeIndex] += 1
            if(pieces == 1):
                if(holeIndex == self.allyHole()):
                    return
                if(self.board[holeIndex] == 1 and self.isOnMySide(holeIndex)): #this is not 0 because we've added a piece before, meaning that it was 0 at the start of the turn but not now
                    self.board[self.allyHole()] += self.board[self.adjacentHole(holeIndex)] + self.board[holeIndex]
                    self.board[self.adjacentHole(holeIndex)] = 0;
                    self.board[holeIndex] = 0;
                self.playerTurn = not self.playerTurn
            pieces -= 1
                    
            



