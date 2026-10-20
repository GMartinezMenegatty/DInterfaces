import sys

from PyQt6.QtCore import QTime, QTimer, Qt, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit, QHBoxLayout, QComboBox, QStackedLayout, QGridLayout, QRadioButton, QCheckBox, QTimeEdit
from PyQt6.QtGui import QColor, QPalette

import random

class Boton(QPushButton):

    banderaCambiada = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.RightButton:
            if self.text() == "🚩":
                self.setText("")
                self.banderaCambiada.emit(1)

            elif self.styleSheet() == "background-color: red;" or self.styleSheet() == "background-color: lightgray;":
                return
            else:
                self.setText("🚩")
                self.banderaCambiada.emit(-1)
        else:
            super().mousePressEvent(event)

class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MineSweeper")

        self.setMinimumSize(300, 200)
        self.setMaximumSize(500, 400)

        GRID = 8
        MINAS = 10

        self.tablero = []

        for i in range(GRID):
            fila = []

            for j in range(GRID):
                fila.append(0)

            self.tablero.append(fila)

        # Colocar las 10 minas en posiciones aleatorias
        minasColocadas = 0

        while minasColocadas < MINAS:
            fila = random.randint(0, GRID - 1)
            columna = random.randint(0, GRID - 1)

            if self.tablero[fila][columna] == 0:
                self.tablero[fila][columna] = 1
                minasColocadas += 1

        for fila in self.tablero:
            print(fila)

        maia = QVBoxLayout()
        gridUp = QGridLayout()
        grid = QGridLayout()

        self.minasRestantes = QLabel("10")
        self.vivo = QPushButton("Vivo")
        self.vivo.clicked.connect(self.restart)

        self.tiempo = QLabel("0")
        self.segundos = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizarTiempo)
        self.timer.start(1000)


        gridUp.addWidget(self.minasRestantes, 0, 0)
        gridUp.addWidget(self.vivo, 0, 1)
        gridUp.addWidget(self.tiempo, 0, 2)


        self.botones = []

        #bucle for de creacion de grid de botones
        for x in range(GRID):
            filaBotones = []

            for y in range(GRID):
                button = Boton()
                grid.addWidget(button, x, y)
                button.clicked.connect(self.pulsado)

                button.banderaCambiada.connect(self.actualizarMinas)

                button.setProperty("fila", x)
                button.setProperty("columna", y)

                filaBotones.append(button)

            self.botones.append(filaBotones)

        maia.addLayout(gridUp)
        maia.addLayout(grid)
        maia.addStretch()

        contenedor = QWidget()
        contenedor.setLayout(maia)
        self.setCentralWidget(contenedor)

    def pulsado(self):
        boton = self.sender()

        if boton.text() == "🚩":
            return

        fila = boton.property("fila")
        columna = boton.property("columna")

        print(fila, columna)

        if self.tablero[fila][columna] == 1:
            boton.setText("*")
            boton.setStyleSheet("background-color: red;")
            print("MINA")

        else:

            minas = self.contarMinas(fila, columna)
            if minas > 0:
                boton.setText(str(minas))
            else:
                boton.setText("")

            boton.setStyleSheet("background-color: lightgray;")
            print("seguro")

    def contarMinas(self, fila, columna):
        minas = 0

        for i in range(fila - 1, fila + 2):
            for j in range(columna - 1, columna + 2):

                if i >= 0 and i < 8 and j >= 0 and j < 8:
                    if self.tablero[i][j] == 1:
                        minas += 1

        return minas

    def actualizarMinas(self, cantidad):
        minas = int(self.minasRestantes.text())
        minas += cantidad
        self.minasRestantes.setText(str(minas))

    def actualizarTiempo(self):
        self.segundos += 1
        self.tiempo.setText(str(self.segundos))












    def restart(self):

        print("restart")

        GRID = 8
        MINAS = 10

        # Reiniciar el tablero
        self.tablero = []

        for i in range(GRID):
            fila = []

            for j in range(GRID):
                fila.append(0)

            self.tablero.append(fila)

        # Colocar las minas de nuevo
        minasColocadas = 0

        while minasColocadas < MINAS:
            fila = random.randint(0, GRID - 1)
            columna = random.randint(0, GRID - 1)

            if self.tablero[fila][columna] == 0:
                self.tablero[fila][columna] = 1
                minasColocadas += 1

        # Limpiar los botones
        for fila in self.botones:
            for boton in fila:
                boton.setText("")
                boton.setStyleSheet("")

        # Reiniciar el contador de minas
        self.minasRestantes.setText("10")

        # Reiniciar el tiempo
        self.segundos = 0
        self.tiempo.setText("0")



if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    aplicacion.exec()