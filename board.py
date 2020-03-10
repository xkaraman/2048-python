
from random import randint
from enum import Enum,auto
from copy import deepcopy
import numpy as np

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
        self.board = [[Tile(0) for x in range(self.dimension)] for y in range(self.dimension)]
        # print("init")
        # print(self.asNumpy())
        # self.board = numpy.zeros( [4,4], dtype = int)

    def reset(self):
        self.pointsScoredLastRound = 0
        self.tileCollisionLastRound = False
        self.board = [[Tile(0) for x in range(self.dimension)] for y in range(self.dimension)]
        # self.board = numpy.zeros( [4,4], dtype = int)

        start = self.freePosition();
        self.board[start[0]][start[1]] = Tile()
        # self.board[1][2] = Tile()

        start = self.freePosition();
        self.board[start[0]][start[1]] = Tile()
        # self.board[3][2] = Tile()

    def asNumpy(self):
        return np.array([[self.board[x][y].value for y in range(self.dimension)] for x in range(self.dimension)])

    def freePosition(self):
        if self.full():
            pos = (-1,-1)
        else:
            while True:
                i = randint(0, self.dimension-1)
                j = randint(0, self.dimension-1)
                if (self.board[i][j].value == 0 ):
                    pos = (i,j)
                    break
        return pos

    def move(self,direction):
        # self.board.copy(preMoveBoard)
        # preMoveBoard = Board()
        # print("Board " + str(direction))
        preMoveBoard = deepcopy(self)
        # print("old board")
        # print(preMoveBoard.asNumpy())
        self.prepareForNextMove()
        if direction == Direction.UP:
            for i in range(self.dimension):
                for j in range(self.dimension):
                    self.moveVertically(i,j,Direction.UP)


        if direction == Direction.DOWN:
            for i in reversed(range(self.dimension)):
                for j in range(self.dimension):
                    self.moveVertically(i,j,Direction.DOWN)

        if direction == Direction.RIGHT:
            for i in range(self.dimension):
                for j in reversed(range(self.dimension)):
                    self.moveHorizontally(i,j,Direction.RIGHT)

        if direction == Direction.LEFT:
            for i in range(self.dimension):
                for j in range(self.dimension):
                    self.moveHorizontally(i,j,Direction.LEFT)

        # print("new board")
        # print(self.asNumpy())

        if self.changed(preMoveBoard):
            start = self.freePosition();
            self.board[start[0]][start[1]] = Tile()

    def changed(self,previousBoard):
        if self.dimension != previousBoard.dimension:
            return False
        for i in range(self.dimension):
            for j in range(self.dimension):
                if ( ( (self.board[i][j].value == 0 and previousBoard.board[i][j].value != 0) or
                     ( self.board[i][j].value != 0 and previousBoard.board[i][j].value == 0) ) or
                 (   ( self.board[i][j].value != 0 and previousBoard.board[i][j].value != 0) and
                        self.board[i][j].value != previousBoard.board[i][j].value) ):
                    return True
        return False

    def prepareForNextMove(self):
        self.tileCollisionLastRound = False
        self.pointsScoredLastRound = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if(self.board[i][j].value != 0):
                    self.board[i][j].upgradedThisMove = False

    def full(self):
        full = True
        for i in range(self.dimension):
            for j in range(self.dimension):
                if  self.board[i][j].value == 0:
                    full = False
        return full

    def movePossible(self):
        if (self.full()):
        # check if there is still a move to do
            newBoard = deepcopy(self);
            newBoard.move(Direction.UP)
            if (self.changed(newBoard)): return True
            newBoard.move(Direction.DOWN)
            if (self.changed(newBoard)): return True
            newBoard.move(Direction.LEFT)
            if (self.changed(newBoard)): return True
            newBoard.move(Direction.RIGHT)
            if (self.changed(newBoard)): return True

            #  no possible move
            return False

        else:
            return True

    def inbounds(self,i,j):
         return (i >= 0 and j >= 0 and i < self.dimension and j < self.dimension)

    def moveVertically(self, i, j, direction):
        if self.board[i][j].value != 0:
            # print("moving:",i,j,direction)
            tileColission = False
            if(direction == Direction.UP):
                newi = i - 1
            else:
                newi = i + 1

            while (self.inbounds(newi,j) and self.board[newi][j].value == 0):
                if direction == Direction.UP:
                    newi = newi - 1
                else:
                    newi = newi + 1
            # print(newi,j)
            # print(not self.inbounds(newi,j))
            if (not self.inbounds(newi,j)):
                if (direction == Direction.UP):
                    self.board[0][j] = self.board[i][j]
                    # print(self.board[0][j].value)
                else:
                    self.board[self.dimension-1][j] = self.board[i][j]
            else:
                if (self.board[newi][j].value == self.board[i][j].value) and not self.board[newi][j].upgradedThisMove :
                    tileColission = True
                    self.handleCollision(newi,j)
                else:
                    if (direction == Direction.UP):
                        self.board[newi+1][j] = self.board[i][j]
                    else:
                        self.board[newi-1][j] = self.board[i][j]

            if ( (direction == Direction.UP and newi+1 != i) or (direction == Direction.DOWN and newi-1 != i) or tileColission ):
                self.board[i][j] = Tile(0);

            if tileColission:
                self.tileCollisionLastRound = True

    def moveHorizontally(self, i, j, direction):
        if self.board[i][j].value != 0:
            # print("moving:",i,j,direction)
            tileCollision = False
            if(direction == Direction.RIGHT):
                newj = j + 1
            else:
                newj = j - 1

            while (self.inbounds(i,newj) and self.board[i][newj].value == 0):
                if direction == Direction.RIGHT:
                    newj = newj + 1
                else:
                    newj = newj - 1

            if (not self.inbounds(i,newj)):
                if (direction == Direction.RIGHT):
                    self.board[i][self.dimension-1] = self.board[i][j]
                else:
                    self.board[i][0] = self.board[i][j]
            else:
                if (self.board[i][newj].value == self.board[i][j].value) and not self.board[i][newj].upgradedThisMove :
                    tileCollision = True
                    self.handleCollision(i,newj)
                else:
                    if (direction == Direction.RIGHT):
                        self.board[i][newj-1] = self.board[i][j]
                    else:
                        self.board[i][newj+1] = self.board[i][j]

            if ( (direction == Direction.RIGHT and newj-1 != j) or (direction == Direction.LEFT and newj+1 != j) or tileCollision ):
                self.board[i][j] = Tile(0);

            if tileCollision:
                self.tileCollisionLastRound = True

    def handleCollision(self,i,j):
        self.board[i][j].upgrade();
        self.board[i][j].upgradedThisMove = True;
        self.pointsScoredLastRound += self.board[i][j].value;
