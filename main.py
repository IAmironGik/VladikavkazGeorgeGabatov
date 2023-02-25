import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

import random


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.bt = QPushButton(self)
        self.bt.resize(50, 50)
        self.bt.setText("")
        self.bt.move(0, 0)
        self.bt.clicked.connect(self.paint)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Draw text')
        self.do_paint = False
        self.show()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            color = [Qt.yellow, Qt.red, Qt.green, Qt.blue, Qt.black, Qt.darkBlue]
            qp.setPen(QPen(random.choice(color), 8, Qt.SolidLine))
            x = random.randint(200, 401)
            qp.drawEllipse(40, 40, x, x)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
