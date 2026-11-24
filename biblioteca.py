
import sys

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QFormLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton,
    QComboBox, QCheckBox, QSpinBox,
    QDial, QSlider, QTextEdit,
    QStackedWidget, QTableWidget,
    QTableWidgetItem, QListWidget,
    QGroupBox, QButtonGroup, QMessageBox,
    QAbstractItemView
)

from PyQt6.QtCore import Qt


class Biblioteca(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de biblioteca")
        self.resize(800, 550)

        self.crearInterfaz()
        self.conectarSenales()

    # ===================================
    # CREAR INTERFAZ PRINCIPAL
    # ===================================

    def crearInterfaz(self):

        principal = QVBoxLayout()

        self.paginas = QStackedWidget()

        self.zona1 = QWidget()
        self.zona2 = QWidget()
        self.zona3 = QWidget()

        self.crearZona1()
        self.crearZona2()
        self.crearZona3()

        self.paginas.addWidget(self.zona1)
        self.paginas.addWidget(self.zona2)
        self.paginas.addWidget(self.zona3)

        # Botones de navegación
        self.btnConfiguracion = QPushButton(
            "Configuración"
        )

        self.btnBiblioteca = QPushButton(
            "Biblioteca"
        )

        self.btnConsola = QPushButton("Consola")

        self.grupoBotones = QButtonGroup(self)
        self.grupoBotones.setExclusive(True)

        botones = QHBoxLayout()

        listaBotones = [
            self.btnConfiguracion,
            self.btnBiblioteca,
            self.btnConsola
        ]

        for i, boton in enumerate(listaBotones):
            boton.setCheckable(True)
            self.grupoBotones.addButton(boton, i)
            botones.addWidget(boton)

        principal.addWidget(self.paginas)
        principal.addLayout(botones)

        self.setLayout(principal)

        # Página inicial
        self.paginas.setCurrentIndex(0)
        self.btnConfiguracion.setChecked(True)

    # ===================================
    # ZONA 1: CONFIGURACIÓN
    # ===================================

    def crearZona1(self):

        layout = QVBoxLayout()
        formulario = QFormLayout()

        self.txtTitulo = QLineEdit()

        self.cmbCategoria = QComboBox()
        self.cmbCategoria.addItems([
            "Novela",
            "Informática",
            "Historia",
            "Ciencia"
        ])

        self.chkDisponible = QCheckBox("Disponible")
        self.chkDisponible.setChecked(True)

        self.spnEjemplares = QSpinBox()
        self.spnEjemplares.setRange(1, 100)

        self.dialValoracion = QDial()
        self.dialValoracion.setRange(0, 10)
        self.dialValoracion.setValue(5)
        self.dialValoracion.setNotchesVisible(True)

        self.lblValoracion = QLabel("5/10")

        self.sliderPrestamo = QSlider(
            Qt.Orientation.Horizontal
        )
        self.sliderPrestamo.setRange(1, 30)
        self.sliderPrestamo.setValue(15)

        self.lblPrestamo = QLabel("15 días")

        formulario.addRow(
            "Título:", self.txtTitulo
        )

        formulario.addRow(
            "Categoría:", self.cmbCategoria
        )

        formulario.addRow(
            "Disponibilidad:", self.chkDisponible
        )

        formulario.addRow(
            "Ejemplares:", self.spnEjemplares
        )

        formulario.addRow(
            "Valoración:", self.dialValoracion
        )

        formulario.addRow(
            "Nota:", self.lblValoracion
        )

        formulario.addRow(
            "Duración préstamo:", self.sliderPrestamo
        )

        formulario.addRow(
            "Días:", self.lblPrestamo
        )

        # Grupo de opciones
        self.grupoOpciones = QGroupBox("Opciones")
        opciones = QGridLayout()

        self.chkDigital = QCheckBox("Digital")
        self.chkFisico = QCheckBox("Físico")

        opciones.addWidget(self.chkDigital, 0, 0)
        opciones.addWidget(self.chkFisico, 0, 1)

        self.grupoOpciones.setLayout(opciones)

        self.btnRegistrar = QPushButton(
            "Registrar libro"
        )

        layout.addLayout(formulario)
        layout.addWidget(self.grupoOpciones)
        layout.addWidget(self.btnRegistrar)

        self.zona1.setLayout(layout)

    # ===================================
    # ZONA 2: TABLA Y LISTA
    # ===================================

    def crearZona2(self):

        layout = QVBoxLayout()

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(7)
        self.tabla.setRowCount(0)

        self.tabla.setHorizontalHeaderLabels([
            "Título",
            "Categoría",
            "Disponible",
            "Ejemplares",
            "Valoración",
            "Formato",
            "Préstamo"
        ])

        self.tabla.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.tabla.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        self.tabla.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.listaFavoritos = QListWidget()

        self.btnEliminarLibro = QPushButton(
            "Eliminar libro"
        )

        self.btnFavorito = QPushButton(
            "Añadir a favoritos"
        )

        self.btnEliminarFavorito = QPushButton(
            "Eliminar favorito"
        )

        self.btnOrdenar = QPushButton(
            "Ordenar favoritos"
        )

        self.lblTotal = QLabel("Total de libros: 0")

        botones = QHBoxLayout()

        botones.addWidget(self.btnEliminarLibro)
        botones.addWidget(self.btnFavorito)

        botonesFavoritos = QHBoxLayout()

        botonesFavoritos.addWidget(
            self.btnEliminarFavorito
        )

        botonesFavoritos.addWidget(self.btnOrdenar)

        layout.addWidget(QLabel("Libros registrados"))
        layout.addWidget(self.tabla)
        layout.addLayout(botones)

        layout.addWidget(QLabel("Favoritos"))
        layout.addWidget(self.listaFavoritos)
        layout.addLayout(botonesFavoritos)
        layout.addWidget(self.lblTotal)

        self.zona2.setLayout(layout)

    # ===================================
    # ZONA 3: CONSOLA
    # ===================================

    def crearZona3(self):

        layout = QVBoxLayout()

        self.consola = QTextEdit()
        self.consola.setReadOnly(True)
        self.consola.append("Aplicación iniciada")

        self.btnLimpiarConsola = QPushButton(
            "Limpiar consola"
        )

        layout.addWidget(self.consola)
        layout.addWidget(self.btnLimpiarConsola)

        self.zona3.setLayout(layout)

    # ===================================
    # SEÑALES
    # ===================================

    def conectarSenales(self):

        self.grupoBotones.idClicked.connect(
            self.cambiarZona
        )

        self.chkDisponible.toggled.connect(
            self.cambiarDisponibilidad
        )

        self.cmbCategoria.currentTextChanged.connect(
            self.cambiarCategoria
        )

        self.dialValoracion.valueChanged.connect(
            self.cambiarValoracion
        )

        self.sliderPrestamo.valueChanged.connect(
            self.cambiarPrestamo
        )

        self.btnRegistrar.clicked.connect(
            self.registrarLibro
        )

        self.btnEliminarLibro.clicked.connect(
            self.eliminarLibro
        )

        self.btnFavorito.clicked.connect(
            self.anadirFavorito
        )

        self.btnEliminarFavorito.clicked.connect(
            self.eliminarFavorito
        )

        self.btnOrdenar.clicked.connect(
            self.listaFavoritos.sortItems
        )

        self.btnLimpiarConsola.clicked.connect(
            self.consola.clear
        )

        self.tabla.cellClicked.connect(
            self.seleccionarLibro
        )

        self.listaFavoritos.itemDoubleClicked.connect(
            self.mostrarFavorito
        )

    # ===================================
    # FUNCIONES DE CONFIGURACIÓN
    # ===================================

    def cambiarZona(self, indice):
        self.paginas.setCurrentIndex(indice)

    def cambiarDisponibilidad(self, estado):

        self.spnEjemplares.setEnabled(estado)
        self.sliderPrestamo.setEnabled(estado)

        if estado:
            self.consola.append("Libro disponible")
        else:
            self.consola.append("Libro no disponible")

    def cambiarCategoria(self, categoria):

        self.consola.append(
            f"Categoría seleccionada: {categoria}"
        )

    def cambiarValoracion(self, valor):

        self.lblValoracion.setText(f"{valor}/10")

        self.consola.append(
            f"Valoración seleccionada: {valor}"
        )

    def cambiarPrestamo(self, dias):

        self.lblPrestamo.setText(f"{dias} días")

        self.consola.append(
            f"Duración préstamo: {dias} días"
        )

    # ===================================
    # REGISTRAR LIBRO
    # ===================================

    def registrarLibro(self):

        titulo = self.txtTitulo.text().strip()

        if titulo == "":
            QMessageBox.warning(
                self, "Error", "Introduce un título"
            )
            return

        categoria = self.cmbCategoria.currentText()
        disponible = self.chkDisponible.isChecked()

        ejemplares = self.spnEjemplares.value()
        valoracion = self.dialValoracion.value()
        prestamo = self.sliderPrestamo.value()

        if disponible:
            estado = "Sí"
        else:
            estado = "No"
            ejemplares = 0
            prestamo = 0

        formatos = []

        if self.chkDigital.isChecked():
            formatos.append("Digital")

        if self.chkFisico.isChecked():
            formatos.append("Físico")

        formato = ", ".join(formatos)

        if formato == "":
            formato = "Sin especificar"

        datos = [
            titulo,
            categoria,
            estado,
            str(ejemplares),
            str(valoracion),
            formato,
            str(prestamo)
        ]

        fila = self.tabla.rowCount()
        self.tabla.insertRow(fila)

        for columna, dato in enumerate(datos):

            self.tabla.setItem(
                fila,
                columna,
                QTableWidgetItem(dato)
            )

        self.consola.append(
            f"Libro registrado: {titulo}"
        )

        self.actualizarTotal()
        self.txtTitulo.clear()

    # ===================================
    # FUNCIONES DE TABLA
    # ===================================

    def eliminarLibro(self):

        fila = self.tabla.currentRow()

        if fila == -1:
            QMessageBox.warning(
                self, "Error", "Selecciona un libro"
            )
            return

        titulo = self.tabla.item(fila, 0).text()

        self.tabla.removeRow(fila)

        self.consola.append(
            f"Libro eliminado: {titulo}"
        )

        self.actualizarTotal()

    def seleccionarLibro(self, fila, columna):

        titulo = self.tabla.item(fila, 0).text()

        self.consola.append(
            f"Libro seleccionado: {titulo}"
        )

    def actualizarTotal(self):

        total = self.tabla.rowCount()

        self.lblTotal.setText(
            f"Total de libros: {total}"
        )

    # ===================================
    # FUNCIONES DE LISTA
    # ===================================

    def anadirFavorito(self):

        fila = self.tabla.currentRow()

        if fila == -1:
            QMessageBox.warning(
                self, "Error", "Selecciona un libro"
            )
            return

        titulo = self.tabla.item(fila, 0).text()

        # Comprobar que no esté repetido
        for i in range(self.listaFavoritos.count()):

            elemento = self.listaFavoritos.item(i)

            if elemento.text() == titulo:
                QMessageBox.warning(
                    self, "Error", "Ya está en favoritos"
                )
                return

        self.listaFavoritos.addItem(titulo)

        self.consola.append(
            f"Añadido a favoritos: {titulo}"
        )

    def eliminarFavorito(self):

        fila = self.listaFavoritos.currentRow()

        if fila != -1:

            elemento = self.listaFavoritos.takeItem(fila)

            self.consola.append(
                f"Favorito eliminado: {elemento.text()}"
            )

        else:
            QMessageBox.warning(
                self, "Error", "Selecciona un favorito"
            )

    def mostrarFavorito(self, elemento):

        self.consola.append(
            f"Favorito seleccionado: {elemento.text()}"
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    ventana = Biblioteca()
    ventana.show()

    sys.exit(app.exec())
