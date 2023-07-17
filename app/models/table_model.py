from PyQt6 import QtCore
from PyQt6.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, table):
        super().__init__()
        self.update_table(table)

    def update_table(self, table):
        self.layoutAboutToBeChanged.emit()
        self._table = table
        self.layoutChanged.emit()
        
    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsEnabled

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            self._table[index.row(), index.column()] = value
            return True
    
    def data(self, index, role):
        row = index.row()
        column = index.column()
        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._table[row, column])
    
    def rowCount(self, index):
        rows, _ = self._table.shape
        return rows
    
    def columnCount(self, index):
        _, columns = self._table.shape
        return columns
    
    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            match orientation:
                case Qt.Orientation.Horizontal:
                    return section
                case Qt.Orientation.Vertical:
                    return section