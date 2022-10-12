from mimetypes import init
import random
import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
# from PySide6.QtGui import QAction
# from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QToolBar)




class Application(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.setWindowTitle("Lab Solution application")

        self.initMenu()

    def initMenu(self) -> None:
        menu = self.menuBar()
        file_menu = menu.addMenu("Файл")

        create = QtGui.QAction("Создать", self)
        create.setStatusTip("Основные операции")
        create.triggered.connect(self.onCreateClicked)

        save = QtGui.QAction("Сохранить", self)
        save.setStatusTip("Основные операции")
        save.triggered.connect(self.onSaveClicked)

        clear = QtGui.QAction("Очистить", self)
        clear.setStatusTip("Основные операции")
        clear.triggered.connect(self.onClearClicked)

        exit = QtGui.QAction("Выход", self)
        exit.setStatusTip("Основные операции")
        exit.triggered.connect(self.onExitClicked)

        file_menu.addAction(create)
        file_menu.addAction(save)
        file_menu.addAction(clear)
        file_menu.addAction(exit)

        file_menu = menu.addMenu("Настройки")
        file_menu = menu.addMenu("Расчет")
        file_menu = menu.addMenu("Справка")



    def onCreateClicked(self, s):
        print("click", s)

    def onSaveClicked(self, s):
        print("save", s)

    def onClearClicked(self, s):
        print("clear", s)

    def onExitClicked(self, s):
        print("exit", s)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)


    application = Application()
    application.resize(400, 300)
    application.show()

    sys.exit(app.exec())

# Сделано с душой и любовью за полчаса)