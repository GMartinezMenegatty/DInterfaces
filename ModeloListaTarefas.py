from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QImage, QColor

tick = QImage ('tic16x16.png')

class ModeloTarefas (QAbstractListModel):
    def __init__(self, tarefas = None):
        super().__init__()
        self.tarefas = tarefas or []


    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            _, texto = self.tarefas [indice.row()]
            return texto
        if rol == Qt.ItemDataRole.DecorationRole:
            estado, _ = self.tarefas [indice.row()]
            if estado:
                return tick
        if rol == Qt.ItemDataRole.BackgroundRole:
            estado, _ = self.tarefas [indice.row()]
            if not estado:
                return QColor("light blue")
        if rol == Qt.ItemDataRole.ForegroundRole:
            estado, _ = self.tarefas [indice.row()]
            if not estado:
                return QColor("Blue")
        if rol == Qt.ItemDataRole.CheckStateRole:
            estado, _ = self.tarefas [indice.row()]
            if not estado:
                return Qt.CheckState(True)



    def rowCount(self, indice):
        return len (self.tarefas)















