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

    for x in range(0,7):
        for y in range(0,7):
            availableSquares.append(Square(x,y))

    return availableSquares

class Player:
    positions = []

    def __init__(self):
        self.score = 0
        self.bank = 0
        self.block = False
        self.reflect = False
        self.dead = False

        self.squares = []
        for i in range(7):
            self.squares.append([None] * 7)

    def generateChoices(self):
        availableSquares = generateSquares()
        items = genItems()
        
        for x in range(7):
            for y in range(7):
                randSquare = availableSquares.pop(randint(0,len(availableSquares) - 1))

                self.squares[randSquare.x][randSquare.y] = items.pop(0)#since we're removing one each time and get the randomness from the position on the grid

        print(self.squares)

    def steal(self):
        tempScore = self.score
        self.score = 0
        return tempScore

    def kill(self):
        self.dead = True
        self.score = 0 #powerups?

    def gift(self):
        if(self.dead):
            self.dead = False
        else:
            self.score += 1000

    def snowBall(self):
        self.score = 0
    
    def swap(self, scoreSwap):
        scoreTemp = self.score
        self.score = scoreSwap
        return scoreTemp

    def chooseNextSquare(self):
        #?????
        pass

    def gainBlock(self):
        self.block = True

    def gainReflect(self):
        self.reflect = True
    
    def resetTo0(self):
        self.score = 0
    
    def doubleScore(self):
        self.score *= 2

    def bankScore(self):
        self.bank = self.score
        self.score = 0

players = []
for i in range()
    



        
