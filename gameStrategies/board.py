#board is accessed in order of board[x][y]
board = [[],[],[],[],[],[],[]]

from random import randint

availableSquares = []

class Square:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;

def generateSquares():
    for x in range(0,7):
        for y in range(0,7):
            availableSquares.append(Square(x,y))


def pickSquare():
    randIndex = randint(0,len(availableSquares))
    squareChoice = availableSquares[randIndex]
    del availableSquares[randIndex]
    return squareChoice