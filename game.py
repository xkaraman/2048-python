import cv2
from board import Board
from board import Direction

class Game:
    def __init__(self , dimension = 4):
        self.score = 0
        self.board = Board(dimension)
        self.restart()

    def restart(self):
        self.board.reset()
        self.gameOver = False
        self.score = 0

    def move(self, direction ):
        # print("Game " + str(direction))
        self.board.move(direction)
       #  update score
        if (self.board.tileCollisionLastRound == True):
            self.score += self.board.pointsScoredLastRound;

         # if there is no more move possible, then it's game over
        if ( not self.board.movePossible()):
            self.gameOver = True
            print("Game Over")
