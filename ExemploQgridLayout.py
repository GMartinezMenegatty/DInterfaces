import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QGridLayout, QPushButton, QTextEdit, QVBoxLayout,
                             QApplication, QPushButton, QWidget)
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

        self.setWindowTitle("Exemplo QGridLayout")

        self.setMinimumSize(400, 300)
        self.setMaximumSize(400, 400)

        maia = QGridLayout()

        txtCadrotexto = QTextEdit()
        maia.addWidget(txtCadrotexto, 0, 1, 1, 5)


        btn_clear = QPushButton("C")
        maia.addWidget(btn_clear, 1, 1)
        btn_siete = QPushButton("7")
        maia.addWidget(btn_siete, 2, 1)
        btn_cuatro = QPushButton("4")
        maia.addWidget(btn_cuatro, 3, 1)
        btn_uno = QPushButton("1")
        maia.addWidget(btn_uno, 4, 1)
        btn_cero = QPushButton("0")
        maia.addWidget(btn_cero, 5, 1)

        btn_izq = QPushButton("(")
        maia.addWidget(btn_izq, 1, 2)
        btn_ocho = QPushButton("8")
        maia.addWidget(btn_ocho, 2, 2)
        btn_cinco = QPushButton("5")
        maia.addWidget(btn_cinco, 3, 2)
        btn_dos = QPushButton("2")
        maia.addWidget(btn_dos, 4, 2)
        btn_coma = QPushButton(",")
        maia.addWidget(btn_coma, 5, 2)

        btn_der = QPushButton(")")
        maia.addWidget(btn_der, 1, 3)
        btn_nueve = QPushButton("9")
        maia.addWidget(btn_nueve, 2, 3)
        btn_seis = QPushButton("6")
        maia.addWidget(btn_seis, 3, 3)
        btn_tres = QPushButton("3")
        maia.addWidget(btn_tres, 4, 3)
        btn_porcentaje = QPushButton("%")
        maia.addWidget(btn_porcentaje, 5, 3)

        btn_mod = QPushButton("mod")
        maia.addWidget(btn_mod, 1, 4)
        btn_div = QPushButton("div")
        maia.addWidget(btn_div, 2, 4)
        btn_por = QPushButton("x")
        maia.addWidget(btn_por, 3, 4)
        btn_menos = QPushButton("-")
        maia.addWidget(btn_menos, 4, 4)
        btn_mas = QPushButton("+")
        maia.addWidget(btn_mas, 5, 4)

        btn_pi = QPushButton("π")
        maia.addWidget(btn_pi, 1, 5)
        btn_raiz = QPushButton("√")
        maia.addWidget(btn_raiz, 2, 5)
        btn_elev = QPushButton("x²")
        maia.addWidget(btn_elev, 3, 5)
        btn_igual = QPushButton("=")
        btn_igual.setFixedSize(70,60)
        btn_igual.setStyleSheet("background-color: #FF7700;")
        maia.addWidget(btn_igual, 4, 5, 2, 1)


        window = QWidget()
        window.setLayout(maia)
        self.setCentralWidget(window)

        self.show()


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()