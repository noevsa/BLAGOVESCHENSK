from PyQt5 import uic
from random import randint
import sys
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.draw_krug)
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

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_krug(qp)
        qp.end()

    def draw_krug(self, qp):
        a = self.getRandomSize()
        qp.setBrush([255, 255, 204])
        qp.drawEllipse(100, 100, a, a)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())