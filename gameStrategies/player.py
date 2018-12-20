from random import randint

def genItems():
    items = ['steal', 'kill', 'aid', '0row', 'swap', 'choose square', 'block', 'reflect', '0you', 'doubleScore', 'bank']
    for i in range(25):
        items.append(200)
    for i in range(10):
        items.append(1000)
    for i in range(2):
        items.append(3000)
    items.append(5000)

    return items

class Square:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;

def generateSquares():
    availableSquares = []

    for i in range

    return availableSquares

class Player:
    positions = []

    def __init__(self):
        self.squares = [None] * (7)

    def generateChoices(self):
        availableSquares = generateSquares()
        items = genItems()
        
        for x in range(7):
            self.squares[x] = [None] * 7
            for y in range(7):
                randSquare = availableSquares.pop(randint(0,len(availableSquares)))

                self.squares[randSquare.x][randSquare.y] = items.pop(0) #since we're removing one each time and get the randomness from the position on the grid

        print(self.squares)
        
p = Player()
p.generateChoices()