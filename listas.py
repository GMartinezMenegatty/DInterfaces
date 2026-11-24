
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QListWidget, QLineEdit,
    QPushButton, QLabel, QMessageBox
)


class Ventana(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de alumnos")
        self.resize(450, 350)

        self.txtNombre = QLineEdit()
        self.txtNombre.setPlaceholderText("Nombre")

        self.lista = QListWidget()
        self.lista.addItems(["Ana", "Carlos", "Lucía"])

        self.btnAnadir = QPushButton("Añadir")
        self.btnEliminar = QPushButton("Eliminar")
        self.btnOrdenar = QPushButton("Ordenar")
        self.btnLimpiar = QPushButton("Limpiar")

        self.lblTotal = QLabel("Total: 3")

        # Layouts
        principal = QVBoxLayout()
        botones = QHBoxLayout()

        botones.addWidget(self.btnAnadir)
        botones.addWidget(self.btnEliminar)
        botones.addWidget(self.btnOrdenar)
        botones.addWidget(self.btnLimpiar)

        principal.addWidget(self.txtNombre)
        principal.addWidget(self.lista)
        principal.addLayout(botones)
        principal.addWidget(self.lblTotal)

        self.setLayout(principal)

        # Señales
        self.btnAnadir.clicked.connect(self.anadir)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnOrdenar.clicked.connect(self.ordenar)
        self.btnLimpiar.clicked.connect(self.limpiar)

    def anadir(self):
        nombre = self.txtNombre.text().strip()

        if nombre == "":
            QMessageBox.warning(
                self, "Error", "Introduce un nombre"
            )
            return

        self.lista.addItem(nombre)
        self.txtNombre.clear()
        self.actualizarTotal()

    def eliminar(self):
        fila = self.lista.currentRow()

        if fila != -1:
            self.lista.takeItem(fila)
            self.actualizarTotal()
        else:
            QMessageBox.warning(
                self, "Error", "Selecciona un alumno"
            )

    def ordenar(self):
        self.lista.sortItems()

    def limpiar(self):
        self.lista.clear()
        self.actualizarTotal()

    def actualizarTotal(self):
        cantidad = self.lista.count()
        self.lblTotal.setText(f"Total: {cantidad}")

        """def buscar(self):

    nombre = self.txtNombre.text()

    for i in range(self.lista.count()):

        elemento = self.lista.item(i)

        if elemento.text() == nombre:
            self.lista.setCurrentRow(i)
            return"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
