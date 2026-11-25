import sys
from PyQt6.QtWidgets import *


# Taboa tera que ser creado mediante o patron vista-controlador
# Crear una lista, cos datos da taboa, para pasarlle o modelo de datos da taboa
# mostrar os botons Editar e borrar deshabilitados
# Crear o modelo, que teña como propiedade unha lista como soporte de datos

class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Examen 2")

        self.setMinimumSize(600, 300)

        principal = QVBoxLayout()

        caixaG = QGridLayout()

        principal.addLayout(caixaG)

        self.cliente = QLabel("Cliente")
        caixaG.addWidget(self.cliente, 0, 0)

        self.numeroCliente = QLabel("Número Cliente")
        caixaG.addWidget(self.numeroCliente, 1, 0)

        self.numeroClienteCaja = QComboBox()
        self.numeroClienteCaja.addItems(["1", "2", "3"])
        self.numeroClienteCaja.setCurrentIndex(-1)
        caixaG.addWidget(self.numeroClienteCaja,1, 1, 1, 2)

        self.nomeCliente = QLabel("Nome")
        caixaG.addWidget(self.nomeCliente, 1, 3)

        self.nomeClienteCaja = QLineEdit()
        caixaG.addWidget(self.nomeClienteCaja,1, 4, 1, 2)

        self.apelidos = QLabel("Apelidos")
        caixaG.addWidget(self.apelidos, 2, 0)

        self.apelidoscaja = QLineEdit()
        caixaG.addWidget(self.apelidoscaja,2, 1, 1, 5)

        self.engadir = QPushButton("Engadir")
        caixaG.addWidget(self.engadir, 2, 6)

        self.direccion = QLabel("Direccion")
        caixaG.addWidget(self.direccion, 3, 0)

        self.direccioncaja = QLineEdit()
        caixaG.addWidget(self.direccioncaja,3, 1, 1, 5)

        self.editar = QPushButton("Editar")
        caixaG.addWidget(self.editar, 3, 6)

        self.cidade = QLabel("Cidade")
        caixaG.addWidget(self.cidade, 4, 0)

        self.cidadecaja = QLineEdit()
        caixaG.addWidget(self.cidadecaja,4, 1, 1, 2)

        self.provincia = QLabel("Provincia")
        caixaG.addWidget(self.provincia, 4, 3)

        self.provinciacaja = QLineEdit()
        caixaG.addWidget(self.provinciacaja,4, 4, 1, 2)

        self.borrar = QPushButton("Borrar")
        caixaG.addWidget(self.borrar, 4, 6)

        self.cancelar = QPushButton("Cancelar")

        self.aceptar = QPushButton("Aceptar")

        #TABLA
        caixaTabla = QVBoxLayout()

        self.tabla = QTableWidget()
        caixaTabla.addWidget(self.tabla)

        principal.addLayout(caixaTabla)

        self.tabla.setColumnCount(6)

        self.tabla.setHorizontalHeaderLabels(["Num Cliente", "Nome", "Apelidos", "Dirección", "Cidade", "Provincia"])

        # Señales
        self.engadir.clicked.connect(self.crear)
        self.borrar.clicked.connect(self.eliminar)
        self.editar.clicked.connect(self.modificar)

        principal.addWidget(self.aceptar)
        principal.addWidget(self.cancelar)

        contenedor = QWidget()
        contenedor.setLayout(principal)
        self.setCentralWidget(contenedor)

        self.show()


    def crear(self):
        nombre = self.nomeClienteCaja.text().strip()
        apelidos = self.apelidoscaja.text().strip()
        direccion = self.direccioncaja.text().strip()
        cidade = self.cidadecaja.text().strip()
        provincia = self.provinciacaja.text().strip()

        if nombre == "":
            QMessageBox.warning(self, "Error", "Introduce un nombre")
        if apelidos == "":
            QMessageBox.warning(self, "Error", "Introduce un apellido")
        if provincia == "":
            QMessageBox.warning(self, "Error", "Introduce un provincia")
        if direccion == "":
            QMessageBox.warning(self, "Error", "Introduce un direccion")
        if cidade == "":
            QMessageBox.warning(self, "Error", "Introduce un cidade")
            return

        fila = self.tabla.rowCount()
        self.tabla.insertRow(fila)

        self.escribirFila(fila)

    def escribirFila(self, fila):
        numeroCliente = self.numeroCliente.create()
        nombre = self.nomeClienteCaja.text().strip()
        apelidos = self.apelidoscaja.text().strip()
        direccion = self.direccioncaja.text().strip()
        cidade = self.cidadecaja.text().strip()
        provincia = self.provinciacaja.text().strip()

        datos = [
            numeroCliente,
            nombre,
            apelidos,
            direccion,
            cidade,
            provincia
        ]

        for columna, dato in enumerate(datos):
            self.tabla.setItem(
                fila, columna, QTableWidgetItem(dato))

    def eliminar(self):
        fila = self.tabla.currentRow()

        if fila != -1:
            self.tabla.removeRow(fila)
        else:
            QMessageBox.warning(
                self, "Error", "Selecciona una fila")

    def modificar(self):
        fila = self.tabla.currentRow()

        if fila == -1:
            QMessageBox.warning(
                self, "Error", "Selecciona una fila")
            return

        if self.numeroClienteCaja == "":
            QMessageBox.warning(
                self, "Error", "Seleccione un numero")
            return

        self.escribirFila(fila)






if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()

