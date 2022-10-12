from mimetypes import init
import random
import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
# from PySide6.QtGui import QAction
# from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QToolBar)


class CreateWindow(QtWidgets.QWidget):

    def __init__(self, appwindow) -> None:
        super().__init__()

        self.appwindow = appwindow

        layout = QtWidgets.QVBoxLayout()
        self.setWindowTitle("Создать матрицу")
        self.label1 = QtWidgets.QLabel("Введите количество строк")
        layout.addWidget(self.label1)

        self.edit1 = QtWidgets.QLineEdit()
        self.edit1.setInputMask('000;')
        layout.addWidget(self.edit1)

        self.label2 = QtWidgets.QLabel("Введите количество столбцов")
        layout.addWidget(self.label2)
        self.edit2 = QtWidgets.QLineEdit()
        self.edit2.setInputMask('000;')
        layout.addWidget(self.edit2)

        self.confirm = QtWidgets.QPushButton("Подтвердить", self)
        self.confirm.clicked.connect(self.onConfirmClicK)
        layout.addWidget(self.confirm)
        self.setLayout(layout)

    def onConfirmClicK(self, s):
        self.appwindow.initTable(int(self.edit1.text()), int(self.edit2.text()))
        self.close()

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def flags(self, index):
        return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsEditable
    
    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._data[index.row()][index.column()] = value
            return True


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.setWindowTitle("Lab Solution application")

        self.initMenu()
        # self.initTable()

    def initMenu(self) -> None:
        menu = self.menuBar()
        file_menu = menu.addMenu("Файл")

        create = QtGui.QAction("Создать", self)
        create.triggered.connect(self.onCreateClicked)

        save = QtGui.QAction("Сохранить", self)
        save.triggered.connect(self.onSaveClicked)

        clear = QtGui.QAction("Очистить", self)
        clear.triggered.connect(self.onClearClicked)

        exit = QtGui.QAction("Выход", self)
        exit.triggered.connect(self.onExitClicked)

        file_menu.addAction(create)
        file_menu.addAction(save)
        file_menu.addAction(clear)
        file_menu.addAction(exit)

        file_menu = menu.addMenu("Настройки")
        file_menu = menu.addMenu("Расчет")
        file_menu = menu.addMenu("Справка")


    def initTable(self, x, y):
        self.table = QtWidgets.QTableView()

        data = []

        for i in range(x):
            d = []
            for j in range(y):
                d.append(0)
            data.append(d)

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

    def clearTable(self):
        self.table = None
        self.model = None
        self.setCentralWidget(None)

    def onCreateClicked(self, s):
        self.w = CreateWindow(self)
        self.w.resize(300, 200)
        self.w.show()

    def onSaveClicked(self, s):
        print("save", s)

    def onClearClicked(self, s):
        self.clearTable()

    def onExitClicked(self, s):
        self.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)


    application = Application()
    application.resize(800, 600)
    application.show()

    sys.exit(app.exec())

# Сделано с душой и любовью за полчаса)