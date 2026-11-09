import math
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QLabel,
                             QCheckBox, QGridLayout, QTextEdit, QSlider, QComboBox, QLineEdit, QAbstractSlider)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Examen")

        self.setMinimumSize(400, 250)
        self.setMaximumSize(1000, 1000)

        caixaGrid = QGridLayout()

        # Menú
        self.zoa1 = QPushButton("Configuración zoa 1")
        self.zoa2 = QPushButton("Configuración zoa 2")
        self.consola = QPushButton("Consola")

        caixaGrid.addWidget(self.zoa1, 7, 0)
        caixaGrid.addWidget(self.zoa2, 7, 2)
        caixaGrid.addWidget(self.consola, 7, 4)

        #Zona activada
        self.zoaActivada = QLabel("Zoa Activada")
        self.zoaActivadaBtn = QCheckBox()
        caixaGrid.addWidget(self.zoaActivada, 0 , 0)
        caixaGrid.addWidget(self.zoaActivadaBtn, 0, 1)

        #Rego general
        self.horaRego = QLabel("Hora de comezo de rego")
        self.horaRegoTxt = QLineEdit()
        caixaGrid.addWidget(self.horaRego, 1, 0)
        caixaGrid.addWidget(self.horaRegoTxt, 1, 1)

        self.duracionRego = QLabel("Duración rego")
        self.duracionRegoSlide = QSlider(Qt.Orientation.Horizontal)
        self.duracionRegoSlide.setMaximum(600)
        self.duracionRegoSlide.setMinimum(0)
        caixaGrid.addWidget(self.duracionRego, 2, 0)
        caixaGrid.addWidget(self.duracionRegoSlide, 2, 1)

        #Opciones semanal - diario
        self.opcions = QLabel("Opcións")
        self.opcionsCombo = QComboBox()
        self.opcionsCombo.addItems(["Semanal", "Diario"])
        caixaGrid.addWidget(self.opcions, 3, 0)
        caixaGrid.addWidget(self.opcionsCombo, 4, 0)

        self.antixiada = QCheckBox("Antixiada")
        self.chuvia = QCheckBox("Chuvia")
        caixaGrid.addWidget(self.antixiada, 4, 1)
        caixaGrid.addWidget(self.chuvia, 4, 2)

        #Boton aceptar
        self.aceptar = QPushButton("Aceptar")
        caixaGrid.addWidget(self.aceptar, 5, 4)

        #Dias rego
        self.dias = QLabel("Dias")
        caixaGrid.addWidget(self.dias, 0, 3)

        self.lunes = QCheckBox("Lunes")
        self.martes = QCheckBox("Martes")
        self.mercoles = QCheckBox("Mercoles")
        self.xoves = QCheckBox("Xoves")
        self.venres = QCheckBox("Venres")
        self.sabado = QCheckBox("Sabado")
        self.domingo = QCheckBox("Domingo")

        caixaGrid.addWidget(self.lunes, 1, 3)
        caixaGrid.addWidget(self.martes, 1, 4)
        caixaGrid.addWidget(self.mercoles, 2, 3)
        caixaGrid.addWidget(self.xoves, 2, 4)
        caixaGrid.addWidget(self.venres, 3, 3)
        caixaGrid.addWidget(self.sabado, 3, 4)
        caixaGrid.addWidget(self.domingo, 4, 3)

        #Text Consola
        self.text = QTextEdit()
        #self.consola.addWidget(self.text)



        contenedor = QWidget()
        contenedor.setLayout(caixaGrid)
        self.setCentralWidget(contenedor)

        self.show()


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()