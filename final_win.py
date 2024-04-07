from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class FirstWindow(QWidget):
    def __init__(self, *args,**qwargs):
        super().__init__(*args,**qwargs)
        self.initUI()
    def initUI(self):
        first_Window_layout = QVBoxLayout
        self.info_label = QLabel('ФИО')
        self.index_label = QLabel('Индекс')
        self.result_label = QLabel('Результат')
        self.first_Window_layout.addWidget(first_Window_button)
        self.setLayout(first_Window_layout)