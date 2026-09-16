import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout, QGridLayout)
from PyQt6.QtGui import QColor, QPalette

class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Primera aplicacion")

        self.setMinimumSize(300, 200)
        self.setMaximumSize(500, 400)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("lightblue"))
        self.setPalette(paleta)

        caixaV = QVBoxLayout()

        boton = QPushButton("Saudar")
        boton.clicked.connect(self.on_boton_clicked)
        self.etiqueta = QLabel("Hola a todos")
        self.cadroTexto = QLineEdit()
        self.cadroTexto.returnPressed.connect(self.on_cadroTexto_return_pressed)
        self.cadroTexto.setPlaceholderText("Introduce tu nombre")

        caixaV.addWidget(self.etiqueta)
        caixaV.addWidget(self.cadroTexto)
        caixaV.addWidget(boton)

        contedor = QWidget()
        contedor.setLayout(caixaV)
        self.setCentralWidget(contedor)

        #self.setCentralWidget(boton)
        #self.setCentralWidget(etiqueta)

        self.show()

    def on_boton_clicked(self):
        self.saudar()

    def on_cadroTexto_return_pressed(self):
        self.saudar()

    def saudar(self):
        nome = self.cadroTexto.text()
        if len(nome) != 0 :
            self.etiqueta.setText ("Hola "+nome)
        else:
            self.etiqueta.setText ("Tienes que introducir un nombre")

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()