import PyQt5.QtCore
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QGridLayout,QLabel

from qtile import QTile
from tile import Tile
from board import Direction
from game import Game

class QGameBoard(QWidget):
    def __init__(self,parent = None):
        # super(QGameBoard,self).__init__()
        QWidget.__init__(self, parent = parent)
        self.resize(QSize(1000, 1000))

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.game = Game(4)

        # self.boardLayout = QGridLayout()
        # self.tiles = [[None for x in range(self.game.board.dimension)] for y in range(self.game.board.dimension)]
        # for i in range(self.game.board.dimension):
        #     for j in range(self.game.board.dimension):
        #         self.tiles[i][j] = QTile(self.game.board.board[i][j])
        #         self.boardLayout.addWidget(self.tiles[i][j], i, j)
        #         self.tiles[i][j].draw()
        #
        # self.mainLayout.insertLayout(0, self.boardLayout)
        self.drawBoard()

        self.score = QLabel("SCORE: " + str(self.game.score))
        # score.setStyleSheet("QLabel { color: rgb(0,0,0); font: 16pt; }")
        self.score.setFixedHeight(50)
        self.mainLayout.insertWidget(1,self.score, 0, Qt.AlignRight)
        self.setStyleSheet("QGameBoard { background-color: rgb(187,173,160) }")
        self.setFocusPolicy(Qt.StrongFocus)

    def keyPressEvent(self, e):
        # print( e.key() )
        if e.key() in ( Qt.Key_W, Qt.Key_Up):
            # print("Up")
            self.game.move(Direction.UP)
            self.score.setText("SCORE: " + str(self.game.score))
            self.drawBoard()
        elif e.key() in (Qt.Key_S, Qt.Key_Down):
            # print("Down")
            self.game.move(Direction.DOWN)

        elif e.key() in (Qt.Key_D, Qt.Key_Right):
            # print("Right")
            self.game.move(Direction.RIGHT)
        elif e.key() in (Qt.Key_A, Qt.Key_Left):
            # print("Left")
            self.game.move(Direction.LEFT)

        e.accept()

    def drawBoard(self):
        self.boardLayout = QGridLayout()
        self.tiles = [[None for x in range(self.game.board.dimension)] for y in range(self.game.board.dimension)]
        for i in range(self.game.board.dimension):
            for j in range(self.game.board.dimension):
                self.tiles[i][j] = QTile(self.game.board.board[i][j])
                self.boardLayout.addWidget(self.tiles[i][j], i, j)
                self.tiles[i][j].draw()

        self.mainLayout.insertLayout(0, self.boardLayout)
