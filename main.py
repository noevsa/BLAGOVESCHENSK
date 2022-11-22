from random import randint
import sys
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

from man import Ui_MainWindow

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.minSize = 600
        self.maxSize = 1000
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_krug(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def getRandomSize(self):
        return randint(10, self.minSize)

    def getRandomColor(self):
        return QColor(randint(0, 255), randint(0, 255), randint(0, 255))

    def draw_krug(self, qp):
        a = self.getRandomSize()
        qp.setBrush(self.getRandomColor())
        qp.drawEllipse(20, 20, a, a)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
