import PyQt5.QtCore
from PyQt5.QtCore import QSize,Qt,pyqtSignal
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QGridLayout,QLabel,QHBoxLayout,QPushButton
from PyQt5.QtGui import QImage,QPainter

import time

import cv2
import qimage2ndarray
import numpy as np

from qtile import QTile
from tile import Tile
from board import Direction
from game import Game

class QGameBoard(QWidget):
    def __init__(self,parent = None):
        QWidget.__init__(self, parent = parent)

        # This defines a signal called 'drawBoard'
        # drawBoardSlot = pyqtSignal(name='drawBoard')

        # Init Game
        self.game = Game(4)

        # Create the layouts
        # Overall layout with title and score
        self.mainLayout = QVBoxLayout()
        # Game Grid
        self.boardLayout = QGridLayout()
        self.mainLayout.addLayout(self.boardLayout)


        self.endHorizontalLayout = QHBoxLayout()

        # Create score layout and populate main layout at the bottom
        self.score = QLabel("SCORE: " + str(self.game.score))
        self.score.setStyleSheet("QLabel { color: rgb(0,0,0); font: 16pt; }")
        self.score.setFixedHeight(50)
        self.score.setAlignment(Qt.AlignCenter)

        self.aiButton = QPushButton("&Start AI")
        self.aiButton.clicked.connect(self.ai)

        self.resetButton = QPushButton("&Reset Game")
        self.resetButton.clicked.connect(self.reset)

        self.endHorizontalLayout.addWidget(self.aiButton)
        self.endHorizontalLayout.addWidget(self.resetButton)
        self.endHorizontalLayout.addWidget(self.score)


        # self.mainLayout.insertWidget(1,self.score, 0, Qt.AlignRight)
        self.mainLayout.addLayout(self.endHorizontalLayout)

        self.setStyleSheet("QGameBoard { background-color: rgb(255,255,255) }")
        self.setFocusPolicy(Qt.StrongFocus)

        self.setLayout(self.mainLayout)


        self.drawBoard()

    def ai(self):
        # while True:
        self.game.move(Direction.UP)
        # time.sleep(1)
        self.drawBoard()

    def reset(self):
        self.game.restart()
        self.drawBoard()

    def keyPressEvent(self, e):
        # print( e.key() )
        if e.key() in ( Qt.Key_W, Qt.Key_Up):
            # print("Up")
            self.game.move(Direction.UP)

        elif e.key() in (Qt.Key_S, Qt.Key_Down):
            # print("Down")
            self.game.move(Direction.DOWN)

        elif e.key() in (Qt.Key_D, Qt.Key_Right):
            # print("Right")
            self.game.move(Direction.RIGHT)
        elif e.key() in (Qt.Key_A, Qt.Key_Left):
            # print("Left")
            self.game.move(Direction.LEFT)

        self.drawBoard()
        e.accept()


    def grab_screen(self,driver = None):
        img = QImage( self.size(),QImage.Format_ARGB32 );
        painter = QPainter(img)
        self.render(painter);

        image = self.process_img(img)
        del painter
        return image

    def process_img(self,image1):
        img = qimage2ndarray.rgb_view(image1)
        # print(type(img))
        # print(img.dtype)
        # print(img.shape)
        vis2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(vis2, (0,0), fx = .5, fy = .5) # resale image dimensions
        image = cv2.Canny(image, threshold1 = 50, threshold2 = 200) #apply the canny edge detection
        cv2.imshow('ImageWindow', image)
        cv2.waitKey()
        return image

    def drawBoard(self):
        self.clearLayout(self.boardLayout)
        self.boardLayout = QGridLayout()
        self.tiles = [[Tile(0) for x in range(self.game.board.dimension)] for y in range(self.game.board.dimension)]

        for i in range(self.game.board.dimension):
            for j in range(self.game.board.dimension):
                # print("drawBoard ",i ,j)
                # self.tiles[i][j] = None
                self.tiles[i][j] = QTile(self.game.board.board[i][j])
                self.boardLayout.addWidget(self.tiles[i][j], i, j)
                self.tiles[i][j].draw()

        self.mainLayout.insertLayout(0, self.boardLayout)

        self.score.setText("SCORE: " + str(self.game.score))


    def clearLayout(self,layout):
        if layout != None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clearLayout(child.layout())
