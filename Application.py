from mimetypes import init
import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

# TODO:
# нужно до делать кнопки, и там остальное по тз лабы, а так вроде все
# пс. люблю python - лаба на питоне больше, чем курсовая по c++


class SolveWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.setWindowTitle("Решение")
        self.setLayout(self.layout)

    # Теперь решение здесь1
    def solve(self, data) -> None:

        layout = self.layout
        
        str = ""
        # 1. Сумма строки
        for i in range(len(data)):
            d = data[i]
            sum = 0
            for j in range(len(d)):
                sum += int(d[j])
            
            str += f"Сумма строки %i равна %i\n" %(i + 1, sum)

        self.label1 = QtWidgets.QLabel(str)
        layout.addWidget(self.label1)

        # 2. на это забил

        # 3. Количество строк, хранящих хотя бы одно отрицательное число
        v = 0
        for i in range(len(data)):
            d = data[i]
            for j in range(len(d)):
                if(int(d[j]) < 0):
                    v += 1
                    break
        self.label2 = QtWidgets.QLabel(f"Количество строк с отрицательными числами %i" % (v))
        layout.addWidget(self.label2)
        

class InfoWindow(QtWidgets.QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Справка")
        layout = QtWidgets.QVBoxLayout()

        self.label1 = QtWidgets.QLabel("Супер важная инфа111!")
        layout.addWidget(self.label1)

        layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.setLayout(layout)



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

        layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

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

    def getData(self):
        return self._data

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

        settings_menu = menu.addMenu("Настройки")
        
        solve_menu = menu.addMenu("Расчет")

        solve = QtGui.QAction("Вариант 12", self)
        solve.triggered.connect(self.solve)

        solve_menu.addAction(solve)

        info_menu = menu.addMenu("Справка")
        info = QtGui.QAction("Справка", self)
        info.triggered.connect(self.onInfoClicked)
        info_menu.addAction(info)


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
        self.w.resize(300, 150)
        self.w.show()

    def onSaveClicked(self, s):
        print("save", s)

    def onClearClicked(self, s):
        self.clearTable()

    def onExitClicked(self, s):
        self.close()

    # Тут решение 12 варианта
    def solve(self, s):
        data = self.model.getData()
        self.w2 = SolveWindow()
        self.w2.resize(400, 300)
        self.w2.show()
        self.w2.solve(data)
        

    def onInfoClicked(self, s):
        self.w1 = InfoWindow()
        self.w1.resize(300, 200)
        self.w1.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    application = Application()
    application.resize(800, 600)
    application.show()

    sys.exit(app.exec())

# Сделано с душой и любовью за полчаса)
# уже не за пол часа