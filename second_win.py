from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class SecondWindow(QWidget):
    def __init__(self, *args,**qwargs):
        super().__init__(*args,**qwargs)
        self.initUI()
def initUI(self):
    main_layout = QHBoxLayout()
    'left_layout =' 

    label_name = QLabel('Введите ФИО')
    input_name = QLineEdit()
    input_name.setPlaceholderText('Игнат Игнатович Игнатов')

    label1_name = QLabel('Введите полный возраст:')
    input1_name = QLineEdit
    input1_name.setPlaceholderText('23')

    label2_name = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку ''Начать тест'', чтобы запустить таймер. Результат запишите в соответствующие поле')
    label2_name = QLabel('Введите результаты первого теста')
    input2_name = QLineEdit
    input2_name.setPlaceholderText('32,12')
    button_test1 = QPushButton('Начать тест')

    label3_name = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания"')
    labe3_name = QLabel('Введите результаты второго теста')
    input3_name = QLineEdit
    input3_name.setPlaceholderText('32,12')
    button_test2 = QPushButton('Начать приседания')

    label4_name = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания"')
    labe4_name = QLabel('Введите результаты второго теста')
    input4_name = QLineEdit
    input4_name.setPlaceholderText('32,12')
    button_test3 = QPushButton('Начать приседания')

    label5_name = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите на кнопку ''Начать финальный тест'',чтобы запустить таймер.\nЗеленым обозначены секунды в течении которых необходимо\nв течении которых необходимо проводить измерения черным-минуты без замера пульсаций. Результаты запишите в соответсвующие поля.')
    
    
    