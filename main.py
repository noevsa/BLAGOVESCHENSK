from PyQt5 import uic
from random import randint
import sys
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import math
from PyQt5.QtCore import Qt, QPointF

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.minSize = 300
        self.maxSize = 1000
        self.w = 0
        self.h = 0
        self.getRandomWinSize()

    def getRandomWinSize(self):
        self.w = randint(self.minSize, self.maxSize)
        self.h = randint(self.minSize, self.maxSize)

    def getRandomSize(self):
        return randint(10, self.minSize)


    def draw_krug(self, qp):
        a = self.getRandomSize()
        qp.setBrush(255, 255, 204)
        qp.drawEllipse(100, 100, a, a)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())