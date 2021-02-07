import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")

        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки',
                                                    'молотый/в зёрнах', 'описание вкуса', 'цена',
                                                    'объём упаковки'])

        res = self.connection.cursor().execute('''SELECT * FROM coffes''').fetchall()

        for i in range(len(res)):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j in range(3):
                if j == 0:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(res[i][1])))
                elif j == 1:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(res[i][3])))
                elif j == 2:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(res[i][2])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
