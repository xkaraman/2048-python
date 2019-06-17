import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

EXP_MULTIPLIER = 2

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(640, 480))

        gameBoard = QGameBoard()
        self.setCentralWidget(gameBoard)

class QGameBoard(QWidget):
    def __init__(self):
        # super(QGameBoard,self).__init__()
        QWidget.__init__(self)
        self.resize(QSize(1000, 1000))

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.boardLayout = QGridLayout()
        for i in range(4):
            for j in range(4):
                tile = QTile()
                self.boardLayout.addWidget(tile, i, j)
                tile.draw()

        self.mainLayout.insertLayout(0, self.boardLayout)

        self.score = QLabel("SCORE: 1")
        # score.setStyleSheet("QLabel { color: rgb(0,0,0); font: 16pt; }")
        self.score.setFixedHeight(50)
        self.mainLayout.insertWidget(1,self.score, 0, Qt.AlignRight)

class QTile(QLabel):
        def __init__(self , text = "4"):
            QLabel.__init__(self)
            self.setAlignment(Qt.AlignCenter);
            self.text = text;

        def draw(self):
            if int(self.text) == 2:
                self.setStyleSheet("QTile { background: rgb(238,228,218); color: rgb(119,110,101); font: bold; border-radius: 10px; font: 40pt; }")
            elif int(self.text) == 4:
                self.setStyleSheet("QTile { background: rgb(0,0,0); color: rgb(119,110,101); font: bold; border-radius: 10px; font: 40pt; }")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )

# app  = QApplication([])
# board = MainWindow()
# board.show()
#
# app.exec_()
