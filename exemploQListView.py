import math
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QGridLayout, QPushButton, QTextEdit, QVBoxLayout,
                             QApplication, QPushButton, QWidget, QLabel, QListView, QHBoxLayout)

from ModeloListaTarefas import ModeloTarefas


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo QGridLayout")

        self.setMinimumSize(400, 300)
        self.setMaximumSize(400, 400)

        listaTarefas = [(True, "Ir o centro DC"), (False, "Ir o ximnasio"), (False, "Ir a compra")]

        self.modelo = ModeloTarefas(listaTarefas)

        maia = QVBoxLayout()

        self.lstTarefas = QListView()
        self.lstTarefas.setModel(self.modelo)
        self.lstTarefas.setSelectionMode(QListView.SelectionMode.MultiSelection)

        maia.addWidget(self.lstTarefas)


        caixaBotons = QHBoxLayout()

        btnBorrar = QPushButton("Borrar")
        btnBorrar.clicked.connect(self.on_btnBorrar_clicked)
        btnFeito = QPushButton("Feito")
        btnFeito.clicked.connect (self.on_btnFeito_clicked)
        caixaBotons.addWidget(btnBorrar)
        caixaBotons.addWidget(btnFeito)

        maia.addLayout(caixaBotons)


        window = QWidget()
        window.setLayout(maia)
        self.setCentralWidget(window)

        self.show()

    def on_btnBorrar_clicked(self):
        pass


    def on_btnFeito_clicked(self):
        pass



if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()