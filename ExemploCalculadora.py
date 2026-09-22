import sys

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QHBoxLayout)

class CaixaCor (QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo Calculadora")

        self.setMinimumSize(200, 300)
        self.setMaximumSize(500, 400)

        window = QWidget()
        contenedor = QVBoxLayout()
        window.setLayout(contenedor)
        self.setCentralWidget(window)

        pantalla = QHBoxLayout()
        pantalla.addWidget(CaixaCor("white"))

        botones = QHBoxLayout()

        layout_col1 = QVBoxLayout()
        layout_col1.addWidget(QPushButton("C"))
        layout_col1.addWidget(QPushButton("7"))
        layout_col1.addWidget(QPushButton("4"))
        layout_col1.addWidget(QPushButton("1"))
        layout_col1.addWidget(QPushButton("0"))

        layout_col2 = QVBoxLayout()
        layout_col2.addWidget(QPushButton("("))
        layout_col2.addWidget(QPushButton("8"))
        layout_col2.addWidget(QPushButton("5"))
        layout_col2.addWidget(QPushButton("2"))
        layout_col2.addWidget(QPushButton(","))

        layout_col3 = QVBoxLayout()
        layout_col3.addWidget(QPushButton(")"))
        layout_col3.addWidget(QPushButton("9"))
        layout_col3.addWidget(QPushButton("6"))
        layout_col3.addWidget(QPushButton("3"))
        layout_col3.addWidget(QPushButton("%"))

        layout_col4 = QVBoxLayout()
        layout_col4.addWidget(QPushButton("mod"))
        layout_col4.addWidget(QPushButton("div"))
        layout_col4.addWidget(QPushButton("x"))
        layout_col4.addWidget(QPushButton("-"))
        layout_col4.addWidget(QPushButton("+"))

        layout_col5 = QVBoxLayout()
        layout_col5.addWidget(QPushButton("π"))
        layout_col5.addWidget(QPushButton("√"))
        layout_col5.addWidget(QPushButton("x²"))
        layout_col5.addWidget(QPushButton("="))


        contenedor.addLayout(pantalla)
        contenedor.addLayout(botones)
        botones.addLayout(layout_col1)
        botones.addLayout(layout_col2)
        botones.addLayout(layout_col3)
        botones.addLayout(layout_col4)
        botones.addLayout(layout_col5)

        self.show()











if __name__ == '__main__':
        aplicacion = QApplication(sys.argv)
        fiestra = FiestraPrincipal()
        aplicacion.exec()
