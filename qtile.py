# from PyQt5.QtCore import
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel,QGraphicsDropShadowEffect

from tile import Tile

class QTile(QLabel):
        def __init__(self, tile = Tile(0)):
            QLabel.__init__(self)
            self.setAlignment(Qt.AlignCenter)
            # self.tile = tile
            # if(self.tile != Tile(0):
            self.tile = tile
            self.value = self.tile.value

        def draw(self):
            if(self.value == 0):
                self.setText("")
                self.setStyleSheet("QTile { background: rgb(204,192,179); border-radius: 10px; }")
            else:
                self.setText(str(self.value))
                if int(self.value) == 2:
                    self.setStyleSheet("QTile { background: rgb(238,228,218); color: rgb(119,110,101); font: bold; border-radius: 10px; font: 40pt; }")
                elif int(self.value) == 4:
                    self.setStyleSheet("QTile { background: rgb(238,210,220); color: rgb(119,110,101); font: bold; border-radius: 10px; font: 40pt; }")
                elif int(self.value) == 8:
                    self.setStyleSheet("QTile { background: rgb(242,177,121); color: rgb(255,255,255); font: bold; border-radius: 10px; font: 40pt; }")
                elif int(self.value) == 16:
                    self.setStyleSheet("QTile { background: rgb(245,150,100); color: rgb(255,255,255); font: bold; border-radius: 10px; font: 40pt; }")
                elif int(self.value) == 32:
                    self.setStyleSheet("QTile { background: rgb(245,125,95); color: rgb(255,255,255); font: bold; border-radius: 10px; font: 40pt; }")
                elif int(self.value) == 64:
                    self.setStyleSheet("QTile { background: rgb(245,95,60); color: rgb(255,255,255); font: bold; border-radius: 10px; font: 40pt; }")
                elif int(self.value) == 128:
                    self.setStyleSheet("QTile { background: rgb(237,207,114); color: rgb(255,255,255); font: bold; border-radius: 10px; font: 40pt; }")
                elif int(self.value) == 256:
                    dse = QGraphicsDropShadowEffect();
                    dse.setColor(Qt.yellow);
                    dse.setBlurRadius(20);
                    dse.setOffset(-1);
                    self.setGraphicsEffect(dse);
                    self.setStyleSheet("QTile { background: rgb(237,204,97); color: rgb(255,255,255); font: bold; border-radius: 10px; font: 40pt; }");
                elif int(self.value) == 512:
                    dse = QGraphicsDropShadowEffect();
                    dse.setColor(Qt.yellow);
                    dse.setBlurRadius(30);
                    dse.setOffset(-1);
                    self.setGraphicsEffect(dse);
                    self.setStyleSheet("QTile { background: rgb(237,204,97); color: rgb(255,255,255); font: bold; border-radius: 10px; font: 40pt; }")
                elif int(self.value) == 1024:
                    dse = QGraphicsDropShadowEffect();
                    dse.setColor(Qt.yellow);
                    dse.setBlurRadius(40);
                    dse.setOffset(-1);
                    self.setGraphicsEffect(dse);
                    self.setStyleSheet("QTile { background: rgb(237,204,97); color: rgb(255,255,255); font: bold; border-radius: 10px; font: 40pt; }");
                elif int(self.value) == 2048:
                    dse = QGraphicsDropShadowEffect();
                    dse.setColor(Qt.yellow);
                    dse.setBlurRadius(50);
                    dse.setOffset(-1);
                    self.setGraphicsEffect(dse);
                    self.setStyleSheet("QTile { background: rgb(237,204,97); color: rgb(255,255,255); font: bold; border-radius: 10px; font: 40pt; }");
                else:
                    self.setStyleSheet("QTile { background: rgb(238,228,218); color: rgb(119,110,101); font: bold; border-radius: 10px; font: 40pt; }");
