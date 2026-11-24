
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QFormLayout, QTableWidget,
    QTableWidgetItem, QLineEdit, QPushButton,
    QSpinBox, QDoubleSpinBox, QLabel,
    QMessageBox, QAbstractItemView
)


class Ventana(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de productos")
        self.resize(650, 450)

        # Controles
        self.txtNombre = QLineEdit()

        self.spnPrecio = QDoubleSpinBox()
        self.spnPrecio.setRange(0, 10000)
        self.spnPrecio.setSuffix(" €")

        self.spnCantidad = QSpinBox()
        self.spnCantidad.setRange(1, 1000)

        self.btnAnadir = QPushButton("Añadir")
        self.btnEliminar = QPushButton("Eliminar")
        self.btnModificar = QPushButton("Modificar")
        self.btnLimpiar = QPushButton("Limpiar")

        self.lblTotal = QLabel("Total: 0 €")

        # Tabla
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setRowCount(0)

        self.tabla.setHorizontalHeaderLabels(
            ["Producto", "Precio", "Cantidad", "Total"]
        )

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

        formulario.addRow("Nombre:", self.txtNombre)
        formulario.addRow("Precio:", self.spnPrecio)
        formulario.addRow("Cantidad:", self.spnCantidad)

        botones = QHBoxLayout()
        botones.addWidget(self.btnAnadir)
        botones.addWidget(self.btnEliminar)
        botones.addWidget(self.btnModificar)
        botones.addWidget(self.btnLimpiar)

        principal = QVBoxLayout()
        principal.addLayout(formulario)
        principal.addLayout(botones)
        principal.addWidget(self.tabla)
        principal.addWidget(self.lblTotal)

        self.setLayout(principal)

        # Señales
        self.btnAnadir.clicked.connect(self.anadir)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnLimpiar.clicked.connect(self.limpiar)

        self.tabla.cellClicked.connect(
            self.seleccionarProducto
        )

    def anadir(self):
        nombre = self.txtNombre.text().strip()

        if nombre == "":
            QMessageBox.warning(
                self, "Error", "Introduce un nombre"
            )
            return

        fila = self.tabla.rowCount()
        self.tabla.insertRow(fila)

        self.escribirFila(fila)
        self.calcularTotal()
        self.limpiarCampos()

    def escribirFila(self, fila):
        nombre = self.txtNombre.text().strip()
        precio = self.spnPrecio.value()
        cantidad = self.spnCantidad.value()
        total = precio * cantidad

        datos = [
            nombre,
            f"{precio:.2f}",
            str(cantidad),
            f"{total:.2f}"
        ]

        for columna, dato in enumerate(datos):
            self.tabla.setItem(
                fila, columna, QTableWidgetItem(dato)
            )

    def eliminar(self):
        fila = self.tabla.currentRow()

        if fila != -1:
            self.tabla.removeRow(fila)
            self.calcularTotal()
            self.limpiarCampos()
        else:
            QMessageBox.warning(
                self, "Error", "Selecciona una fila"
            )

    def modificar(self):
        fila = self.tabla.currentRow()

        if fila == -1:
            QMessageBox.warning(
                self, "Error", "Selecciona una fila"
            )
            return

        if self.txtNombre.text().strip() == "":
            QMessageBox.warning(
                self, "Error", "Introduce un nombre"
            )
            return

        self.escribirFila(fila)
        self.calcularTotal()

    def seleccionarProducto(self, fila, columna):
        nombre = self.tabla.item(fila, 0).text()
        precio = self.tabla.item(fila, 1).text()
        cantidad = self.tabla.item(fila, 2).text()

        self.txtNombre.setText(nombre)
        self.spnPrecio.setValue(float(precio))
        self.spnCantidad.setValue(int(cantidad))

    def calcularTotal(self):
        total = 0

        for fila in range(self.tabla.rowCount()):
            valor = self.tabla.item(fila, 3).text()
            total += float(valor)

        self.lblTotal.setText(f"Total: {total:.2f} €")

    def limpiarCampos(self):
        self.txtNombre.clear()
        self.spnPrecio.setValue(0)
        self.spnCantidad.setValue(1)

    def limpiar(self):
        self.tabla.setRowCount(0)
        self.calcularTotal()
        self.limpiarCampos()

        """"def buscar(self):

    nombre = self.txtNombre.text()

    for fila in range(self.tabla.rowCount()):

        elemento = self.tabla.item(fila, 0)

        if elemento is not None:
            if elemento.text() == nombre:
                self.tabla.selectRow(fila)
                return"""

        '''def filtrar(self, categoria):

    for fila in range(self.tabla.rowCount()):

        valor = self.tabla.item(fila, 1).text()

        ocultar = (
            categoria != "Todas"
            and valor != categoria
        )

        self.tabla.setRowHidden(fila, ocultar)'''


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
