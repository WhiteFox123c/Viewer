import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile, QTextStream

from gui import MainWindow


app = QtWidgets.QApplication([])  # Создание объекта нового приложения

file = QFile("stylesheet.qss")  # Объект предостовляющий интерфейс для работы с файлом
file.open(QFile.ReadOnly | QFile.Text)  # Открытие файла
stream = QTextStream(file)  # Создал объект потока файла
app.setStyleSheet(stream.readAll())  # Указание таблицы стилей

main_window = MainWindow.MainWindow()  # Создание объекта главного окна
main_window.show()  # Вывод окна на экран

sys.exit(app.exec_())  # Выход из приложения
