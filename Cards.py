import sys

from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit,
                             QHBoxLayout, QComboBox, QStackedLayout, QGridLayout, QRadioButton, QCheckBox, QTimeEdit)

class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QStakedLayout")

        self.setMinimumSize(300, 200)
        self.setMaximumSize(500, 400)

        maia = QVBoxLayout()

        self.persona = QComboBox()
        self.persona.addItems(["Alumno", "Profesor", "PAS"])
        self.persona.setCurrentIndex(-1)  # -1 para q no empiece con ninguno seleccionado

        maia.addWidget(self.persona)

        #ALUMNO

        alumno = QWidget()
        fAlumno = QGridLayout()

        self.ciclo = QLabel("Ciclo")

        self.cmbTipo = QComboBox()
        self.cmbTipo.addItems(["DAM","DAW","ASIR","SMR"])
        self.cmbTipo.setCurrentIndex(-1) #-1 para q no empiece con ninguno seleccionado

        self.radioButton1 = QRadioButton()
        self.radioButton1.setText("Primero")
        self.radioButton2 = QRadioButton()
        self.radioButton2.setText("Segundo")

        self.anoMatricula = QLabel("Ano Matricula")

        self.ano = QComboBox()
        self.ano.addItems(["20-21","21-22","22-23","23-24","24-25","25-26","26-27"])
        self.ano.setCurrentIndex(-1)  # -1 para q no empiece con ninguno seleccionado

        self.nai = QLabel("Nome Nai")
        self.nomeNai = QLineEdit()

        self.pai = QLabel("Nome Pai")
        self.nomePai = QLineEdit()


        fAlumno.addWidget(self.ciclo,0,0)
        fAlumno.addWidget(self.cmbTipo,0,1)
        fAlumno.addWidget(self.radioButton1,1,0)
        fAlumno.addWidget(self.radioButton2,1,1)
        fAlumno.addWidget(self.anoMatricula,2,0)
        fAlumno.addWidget(self.ano,2,1)
        fAlumno.addWidget(self.nai,3,0)
        fAlumno.addWidget(self.nomeNai,3,1)
        fAlumno.addWidget(self.pai,4,0)
        fAlumno.addWidget(self.nomePai,4,1)

        alumno.setLayout(fAlumno)

        #PROFESOR

        profesor = QWidget()
        fProfesor = QGridLayout()

        self.nome = QLabel("Nome")
        self.txtNome = QLineEdit()

        self.apellidos = QLabel("Apelidos")
        self.txtApellidos = QLineEdit()

        self.titor = QCheckBox()
        self.titor.setText("Titor")

        self.departamentoTxt = QLabel("Departamento")
        self.departamento = QComboBox()
        self.departamento.addItems(["DAM","DAW","ASIR","SMR"])
        self.departamento.setCurrentIndex(-1) #-1 para q no empiece con ninguno seleccionado

        self.radioButton1 = QRadioButton()
        self.radioButton1.setText("Primero")
        self.radioButton2 = QRadioButton()
        self.radioButton2.setText("Segundo")

        self.nivel = QLabel("Nivel")

        self.basico = QCheckBox()
        self.basico.setText("Basico")
        self.medio = QCheckBox()
        self.medio.setText("Medio")
        self.superior = QCheckBox()
        self.superior.setText("Superior")


        fProfesor.addWidget(self.nome, 0, 0)
        fProfesor.addWidget(self.txtNome, 0, 1)
        fProfesor.addWidget(self.apellidos, 1, 0)
        fProfesor.addWidget(self.txtApellidos, 1, 1)
        fProfesor.addWidget(self.titor, 2, 0)
        fProfesor.addWidget(self.departamentoTxt, 3, 0)
        fProfesor.addWidget(self.departamento, 3, 1)
        fProfesor.addWidget(self.nivel, 4, 0)
        fProfesor.addWidget(self.basico, 5, 0)
        fProfesor.addWidget(self.medio, 6,0)
        fProfesor.addWidget(self.superior, 7,0)


        profesor.setLayout(fProfesor)

        self.titor.stateChanged.connect(self.activarTitor)
        self.activarTitor(0)

        #PAS
        pas = QWidget()
        fPas = QGridLayout()

        self.nome = QLabel("Nome")
        self.txtNome = QLineEdit()
        self.apellidos = QLabel("Apelidos")
        self.txtApellidos = QLineEdit()

        self.ocupacionNome = QLabel("Ocupacion")
        self.ocupacion = QComboBox()
        self.ocupacion.addItems(["1", "Secretaria", "Limpieza"])
        self.ocupacion.setCurrentIndex(-1)

        self.horaEntradaNome = QLabel("Hora de Entrada")
        self.horaEntrada = QTimeEdit()
        self.horaEntrada.setTime(QTime.currentTime())

        self.horaSalidaNome = QLabel("Hora de Salida")
        self.horaSalida = QTimeEdit()
        self.horaSalida.setTime(QTime.currentTime())

        fPas.addWidget(self.nome, 0, 0)
        fPas.addWidget(self.txtNome, 0, 1)
        fPas.addWidget(self.apellidos, 1, 0)
        fPas.addWidget(self.txtApellidos, 1, 1)
        fPas.addWidget(self.ocupacionNome, 2, 0)
        fPas.addWidget(self.ocupacion, 2, 1)
        fPas.addWidget(self.horaEntradaNome, 3, 0)
        fPas.addWidget(self.horaEntrada, 3, 1)
        fPas.addWidget(self.horaSalidaNome, 4, 0)
        fPas.addWidget(self.horaSalida, 4, 1)

        pas.setLayout(fPas)

        #Apilado

        self.tarxetas = QStackedLayout()

        self.tarxetas.addWidget(alumno)
        self.tarxetas.addWidget(profesor)
        self.tarxetas.addWidget(pas)

        maia.addLayout(self.tarxetas)

        contenedor = QWidget()
        contenedor.setLayout(maia)

        self.setCentralWidget(contenedor)

        self.persona.currentIndexChanged.connect(self.cambiarFormulario)

        self.tarxetas.setCurrentIndex(0)
        self.tarxetas.currentWidget().hide()

    def activarTitor(self, estado):
        if estado == 2:
            self.departamento.setEnabled(True)
            self.basico.setEnabled(True)
            self.medio.setEnabled(True)
            self.superior.setEnabled(True)

        else:
            self.departamento.setEnabled(False)
            self.basico.setEnabled(False)
            self.medio.setEnabled(False)
            self.superior.setEnabled(False)

            # Volver a los valores por defecto
            self.departamento.setCurrentIndex(-1)
            self.basico.setChecked(False)
            self.medio.setChecked(False)
            self.superior.setChecked(False)

    def cambiarFormulario(self, indice):
        self.tarxetas.currentWidget().show()
        self.tarxetas.setCurrentIndex(indice)
        self.tarxetas.currentWidget().show()

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    aplicacion.exec()