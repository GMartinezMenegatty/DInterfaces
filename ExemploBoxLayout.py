import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QHBoxLayout)
from PyQt6.QtGui import QColor, QPalette

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

        self.setWindowTitle("Exemplo BoxLayout")

        self.setMinimumSize(300, 200)
        self.setMaximumSize(500, 400)

        window = QWidget()
        contenedor = QHBoxLayout()
        window.setLayout(contenedor)
        self.setCentralWidget(window)

        layout_col1 = QVBoxLayout()
        layout_col1.addWidget(CaixaCor("red"))
        layout_col1.addWidget(CaixaCor("yellow"))
        layout_col1.addWidget(CaixaCor("purple"))

        caixa_verde = CaixaCor("green")

        layout_col3 = QVBoxLayout()
        layout_col3.addWidget(CaixaCor("red"))
        layout_col3.addWidget(CaixaCor("purple"))

        contenedor.addLayout(layout_col1)
        contenedor.addWidget(caixa_verde)
        contenedor.addLayout(layout_col3)

        self.show()

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()