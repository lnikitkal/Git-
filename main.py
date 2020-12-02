import sys
from random import randrange
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.flag = False
        self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.flag = True
        self.repaint()

    def paintEvent(self, event):
        if self.flag:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_flag(qp)
            # Завершаем рисование
            qp.end()


    def draw_flag(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 255, 0))
        # Рисуем прямоугольник заданной кистью
        n = randrange(10, 200)
        qp.drawEllipse(200 - n // 2, 200 - n//2, n, n)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())