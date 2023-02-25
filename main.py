import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


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
            qp.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            qp.drawEllipse(40, 40, 400, 400)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
