
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QFormLayout, QTableWidget,
    QTableWidgetItem, QLineEdit, QPushButton,
    QSpinBox, QDoubleSpinBox, QLabel,
    QMessageBox, QAbstractItemView, QComboBox
)


class Ventana(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("examen 2")
        self.resize(600, 300)

        # Controles
        self.cliente = QLabel("Cliente")

        self.numeroClienteCaja = QComboBox()
        self.numeroClienteCaja.addItems(["1", "2", "3"])
        self.numeroClienteCaja.setCurrentIndex(-1)

        self.txtNombre = QLineEdit()
        self.txtApelidos = QLineEdit()
        self.txtDireccion = QLineEdit()
        self.txtCidade = QLineEdit()
        self.txtProvincia = QLineEdit()


        self.btnAnadir = QPushButton("Engadir")
        self.btnEliminar = QPushButton("Borrar")
        self.btnModificar = QPushButton("Editar")

        self.lblCancelar = QPushButton("Cancelar")

        # Tabla
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(6)

        self.tabla.setHorizontalHeaderLabels(["Num Cliente", "Nome", "Apelidos", "Dirección", "Cidade", "Provincia"])

        # Seleccionar filas completas
        self.tabla.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.tabla.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        # Impedir edición directa
        self.tabla.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        # Layouts
        formulario = QFormLayout()

        formulario.addRow("Número Cliente:", self.numeroClienteCaja)
        formulario.addRow("Nombre:", self.txtNombre)
        formulario.addRow("Apelidos:", self.txtApelidos)
        formulario.addRow("Direccion:", self.txtDireccion)
        formulario.addRow("Cidade:", self.txtCidade)
        formulario.addRow("Provincia:", self.txtProvincia)

        botones = QHBoxLayout()
        botones.addWidget(self.btnAnadir)
        botones.addWidget(self.btnEliminar)
        botones.addWidget(self.btnModificar)

        principal = QVBoxLayout()
        principal.addWidget(self.cliente)
        principal.addLayout(formulario)
        principal.addLayout(botones)
        principal.addWidget(self.tabla)
        principal.addWidget(self.lblCancelar)


        self.setLayout(principal)

        # Señales
        self.btnAnadir.clicked.connect(self.crear)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)

        self.tabla.cellClicked.connect(
            self.seleccionarProducto
        )

    def crear(self):
        nombre = self.txtNombre.text().strip()
        apelidos = self.txtApelidos.text().strip()
        direccion = self.txtDireccion.text().strip()
        cidade = self.txtCidade.text().strip()
        provincia = self.txtProvincia.text().strip()

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
        numeroCliente = self.numeroClienteCaja.create()
        nombre = self.txtNombre.text().strip()
        apelidos = self.txtApelidos.text().strip()
        direccion = self.txtDireccion.text().strip()
        cidade = self.txtCidade.text().strip()
        provincia = self.txtProvincia.text().strip()

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
                self, "Error", "Introduce un numero")
            return

        self.escribirFila(fila)

    def seleccionarProducto(self, fila, columna):
        nombre = self.tabla.item(fila, 0).text()
        apelidos = self.tabla.item(fila, 1).text()
        direccion = self.tabla.item(fila, 2).text()
        cidade = self.tabla.item(fila, 3).text()
        provincia = self.tabla.item(fila, 4).text()

        self.txtNombre.setText(nombre)
        self.txtApelidos.setText(apelidos)
        self.txtDireccion.setText(direccion)
        self.txtCidade.setText(cidade)
        self.txtProvincia.setText(provincia)


    def limpiarCampos(self):
        self.numeroClienteCaja.clear()
        self.txtNombre.clear()
        self.txtApelidos.clear()
        self.txtDireccion.clear()
        self.txtCidade.clear()
        self.txtProvincia.clear()

    def limpiar(self):
        self.tabla.setRowCount(0)
        self.limpiarCampos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
