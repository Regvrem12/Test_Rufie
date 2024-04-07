from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class FirstWindow(QWidget):
    def __init__(self, *args,**qwargs):
        super().__init__(*args,**qwargs)
        self.initUI()
    def initUI(self):
        first_Window_layout = QVBoxLayout
        coding=utf8 info_label = QLabel('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровьа потом — за последние 15 секунд первой минуты периода восстановления.\nВажно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\nушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.')
        first_Window_layout.addWidget(info_label)
        first_Window_button = QPushButton('Начать')
        first_Window_layout.addWidget(first_Window_button)
        self.setLayout(first_Window_layout)
app = QApplication([])
windows = []
for i in range(300)
    windows.append(FirstWindow())
for winow in windows:
    window.show()
app.exec_()








