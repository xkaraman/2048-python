import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import signal

from qgameboard import QGameBoard
signal.signal(signal.SIGINT, signal.SIG_DFL)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(640, 480))

        gameBoard = QGameBoard(self)
        self.setCentralWidget(gameBoard)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
