
from random import randint
from enum import Enum,auto
from copy import copy

from tile import Tile

class Direction(Enum):
        UP = auto()
        DOWN = auto()
        LEFT = auto()
        RIGHT = auto()

class Board:
    def __init__(self, dimension = 4):
        self.pointsScoredLastRound = 0
        self.tileCollisionLastRound = False
        self.dimension = dimension
        self.board = [[None for x in range(self.dimension)] for y in range(self.dimension)]

    def reset(self):
        self.pointsScoreLastRound = 0
        self.tileCollisionLastRound = False
        self.board = [[None for x in range(self.dimension)] for y in range(self.dimension)]

        start = self.freePosition();
        self.board[start[0]][start[1]] = Tile()

        start = self.freePosition();
        self.board[start[0]][start[1]] = Tile()

    def freePosition(self):
        if self.full():
            pos = (-1,-1)
        else:
            while True:
                i = randint(0, self.dimension-1)
                j = randint(0, self.dimension-1)
                if (self.board[i][j] == None ):
                    pos = (i,j)
                    break
        return pos

    def move(self,direction):
        # self.board.copy(preMoveBoard)
        # preMoveBoard = Board()
        preMoveBoard = copy(self.board)
        self.prepareForNextMove()
        if direction == Direction.UP:
            for i in range(self.dimension):
                for j in range(self.dimension):
                    self.moveVertically(i,j,Direction.UP)

    def prepareForNextMove(self):
        self.tileCollisionLastRound = False
        self.pointsScoreLastRound = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if(self.board[i][j] != None):
                    self.board[i][j].upgradtedThisMove = False

    def full(self):
        full = True
        for i in range(self.dimension):
            for j in range(self.dimension):
                if  self.board[i][j] == None:
                    full = False
        return full

    def isTileCollisionLastRound(self):
        pass

    def movePossible(self):
        pass

    def inbounds(self,i,j):
        print(i,j)
        return (i >= 0 and j >= 0 and i < self.dimension and j < self.dimension)

    def moveVertically(self, i, j, direction):
        if self.board[i][j] != None:
            print("moving:",i,j,direction)
            tileColission = False
            if(direction == Direction.UP):
                newi = i - 1
            else:
                newi = i + 1

            while (self.inbounds(newi,j) and self.board[newi][j] == None):
                if direction == Direction.UP:
                    newi = newi - 1
                else:
                    newi = newi + 1

            if (not self.inbounds(newi,j)):
                if (dir == Direction.UP):
                    self.board[0][j] = self.board[i][j]
                else:
                    self.board[self.dimension-1][j] = self.board[i][j]
            else:
                if (self.board[newi][j].value == self.board[newi][j].value) and not self.board[newi][j].upgradedThisMove :
                    tileColission = True
                    self.handleCollision(newi,j)
                else:
                    if (direction == Direction.UP):
                        self.board[newi+1][j] = self.board[i][j]
                    else:
                        self.board[newi-1][j] = self.board[i][j]

            if ( (direction == Direction.UP and newi+1 != i) or (direction == Direction.DOWN and newi-1 != i) or tileColission ):
                self.board[i][j] = None;

            if tileColission:
                self.tileCollisionLastRound = True


    def handleCollision(self,i,j):
        self.board[i][j].upgrade();
        self.board[i][j].upgradedThisMove = True;
        self.pointsScoredLastRound += self.board[i][j].value;
