import math
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QGridLayout, QPushButton, QTextEdit, QVBoxLayout,
                             QApplication, QPushButton, QWidget, QLabel)
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

        self.etiqueta = QLabel("")
        self.etiqueta.setMaximumSize(600, 200)

        self.num1 = ""
        self.operador = ""
        self.num2 = ""

        maia.addWidget(self.etiqueta, 1, 0, 1, 4)


        btn_clear = QPushButton("C")
        maia.addWidget(btn_clear, 2, 1)
        btn_siete = QPushButton("7")
        maia.addWidget(btn_siete, 3, 1)
        btn_cuatro = QPushButton("4")
        maia.addWidget(btn_cuatro, 4, 1)
        btn_uno = QPushButton("1")
        maia.addWidget(btn_uno, 5, 1)
        btn_cero = QPushButton("0")
        maia.addWidget(btn_cero, 6, 1)

        btn_izq = QPushButton("(")
        maia.addWidget(btn_izq, 2, 2)
        btn_ocho = QPushButton("8")
        maia.addWidget(btn_ocho, 3, 2)
        btn_cinco = QPushButton("5")
        maia.addWidget(btn_cinco, 4, 2)
        btn_dos = QPushButton("2")
        maia.addWidget(btn_dos, 5, 2)
        btn_coma = QPushButton(",")
        maia.addWidget(btn_coma, 6, 2)

        btn_der = QPushButton(")")
        maia.addWidget(btn_der, 2, 3)
        btn_nueve = QPushButton("9")
        maia.addWidget(btn_nueve, 3, 3)
        btn_seis = QPushButton("6")
        maia.addWidget(btn_seis, 4, 3)
        btn_tres = QPushButton("3")
        maia.addWidget(btn_tres, 5, 3)
        btn_porcentaje = QPushButton("%")
        maia.addWidget(btn_porcentaje, 6, 3)

        btn_mod = QPushButton("mod")
        maia.addWidget(btn_mod, 2, 4)
        btn_div = QPushButton("div")
        maia.addWidget(btn_div, 3, 4)
        btn_por = QPushButton("x")
        maia.addWidget(btn_por, 4, 4)
        btn_menos = QPushButton("-")
        maia.addWidget(btn_menos, 5, 4)
        btn_mas = QPushButton("+")
        maia.addWidget(btn_mas, 6, 4)

        btn_pi = QPushButton("π")
        maia.addWidget(btn_pi, 2, 5)
        btn_raiz = QPushButton("√")
        maia.addWidget(btn_raiz, 3, 5)
        btn_elev = QPushButton("x²")
        maia.addWidget(btn_elev, 4, 5)
        btn_igual = QPushButton("=")
        btn_igual.setFixedSize(70,60)
        btn_igual.setStyleSheet("background-color: #FF7700;")
        maia.addWidget(btn_igual, 5, 5, 2, 1)

        btn_cero.clicked.connect(self.numeroPulsado)
        btn_uno.clicked.connect(self.numeroPulsado)
        btn_dos.clicked.connect(self.numeroPulsado)
        btn_tres.clicked.connect(self.numeroPulsado)
        btn_cuatro.clicked.connect(self.numeroPulsado)
        btn_cinco.clicked.connect(self.numeroPulsado)
        btn_seis.clicked.connect(self.numeroPulsado)
        btn_siete.clicked.connect(self.numeroPulsado)
        btn_ocho.clicked.connect(self.numeroPulsado)
        btn_nueve.clicked.connect(self.numeroPulsado)

        btn_pi.clicked.connect(self.mathPi)

        btn_mas.clicked.connect(self.operadorPulsado)
        btn_menos.clicked.connect(self.operadorPulsado)
        btn_por.clicked.connect(self.operadorPulsado)
        btn_div.clicked.connect(self.operadorPulsado)

        btn_igual.clicked.connect(self.igualPulsado)
        btn_clear.clicked.connect(self.ac)


        window = QWidget()
        window.setLayout(maia)
        self.setCentralWidget(window)

        self.show()

    def numeroPulsado(self):
            boton = self.sender()
            num = boton.text()

            if self.operador == "":
                self.num1 = self.num1 + num
                self.etiqueta.setText(self.num1)
            else:
                self.num2 = self.num2 + num
                self.etiqueta.setText(self.num2)

            print("Numero 1:", self.num1)
            print("Operador:", self.operador)
            print("Numero 2:", self.num2)

    def operadorPulsado(self):
            boton = self.sender()
            operador = boton.text()

            self.operador = operador

            print("Numero 1:", self.num1)
            print("Operador:", self.operador)
            print("Numero 2:", self.num2)

    def igualPulsado(self):
            if self.operador == "+":
                self.num1 = str(float(self.num1) + float(self.num2))
                self.etiqueta.setText(self.num1)
            elif self.operador == "-":
                self.num1 = str(float(self.num1) - float(self.num2))
                self.etiqueta.setText(self.num1)
            elif self.operador == "×":
                self.num1 = str(float(self.num1) * float(self.num2))
                self.etiqueta.setText(self.num1)
            elif self.operador == "÷":
                self.num1 = str(float(self.num1) / float(self.num2))
                self.etiqueta.setText(self.num1)
            self.num2 = ""

    def ac(self):
            self.etiqueta.setText("")
            self.operador = ""
            self.num1 = ""
            self.num2 = ""

    def mathPi(self):
            if self.operador == "":
                self.num1 = str(float(math.pi))
                self.etiqueta.setText(self.num1)
            else:
                self.num2 = str(float(math.pi))
                self.etiqueta.setText(self.num2)

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()