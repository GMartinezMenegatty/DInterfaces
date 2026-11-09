import math
import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout, QListView)

from ModeloListaTarefas import ModeloTarefas


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("exemplo QListView")

        self.setMinimumSize(400, 600)
        self.setMaximumSize(400, 400)

        self.listaTarefas = [[True, "Ir o centro DC"], [False, "Ir o ximnasio"], [False, "Ir a compra"], [False, "Outra"]]

        self.modelo = ModeloTarefas(self.listaTarefas)

        caixaV = QVBoxLayout()

        self.lstTarefas = QListView()
        self.lstTarefas.setModel(self.modelo)
        self.lstTarefas.setSelectionMode(QListView.SelectionMode.MultiSelection)
        caixaV.addWidget(self.lstTarefas)

        caixaBotons = QHBoxLayout()
        btnBorrar = QPushButton("Borrar")
        btnBorrar.clicked.connect(self.on_btnBorrar_clicked)
        btnFeito = QPushButton("Feito")
        btnFeito.clicked.connect(self.on_btnFeito_clicked)

        caixaBotons.addWidget(btnBorrar)
        caixaBotons.addWidget(btnFeito)

        caixaV.addLayout(caixaBotons)

        self.txtTarefa = QLineEdit()
        caixaV.addWidget(self.txtTarefa)
        btnEngadir = QPushButton("Engadir Tarefa")
        btnEngadir.clicked.connect(self.on_btnEngadir_clicked)
        caixaBotons.addWidget(btnEngadir)


        contenedor = QWidget()
        contenedor.setLayout(caixaV)
        self.setCentralWidget(contenedor)

        self.show()

    def on_btnBorrar_clicked(self):
        indices = self.lstTarefas.selectedIndexes()
        if indices:
            for indice in sorted (indices, reverse = True):
                del (self.modelo.tarefas[indice.row()])
            self.modelo.layoutChanged.emit()

    def on_btnFeito_clicked(self):
        indices = self.lstTarefas.selectedIndexes()
        if indices:
            for indice in indices:
                self.modelo.tarefas[indice.row()][0] = True
            self.modelo.layoutChanged.emit()


    def on_btnEngadir_clicked(self):
        txt = self.txtTarefa.text().strip()

        if txt != "":
            self.listaTarefas.append([False, self.txtTarefa.text()])
            self.txtTarefa.clear()
            self.modelo.layoutChanged.emit()


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()