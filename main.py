import sys
import time
# Remove Ros Conflicts
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import signal

from qgameboard import QGameBoard
from ai import AIAgent,buildmodel,trainNetwork
from game_state import GameState
from board import Direction

signal.signal(signal.SIGINT, signal.SIG_DFL)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(800, 600))


if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Create main Window
    mainWin = MainWindow()
    mainWin.show()

    # Create board object and populate main window with it
    gameboard = QGameBoard()
    mainWin.setCentralWidget(gameboard)

    # while True:
    #     gameboard.game.move(Direction.UP)
    #     time.sleep(1)
    #     gameboard.drawBoard()



    sys.exit( app.exec_() )
