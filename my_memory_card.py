from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton,QMessageBox,QGroupBox,QButtonGroup

from PyQt5.QtGui import QFont, QIcon
#создание приложения и главного окна

def show_results():
    RGB1.hide()
    RGB2.show()
    button.setText('Следующий вопрос')
def show_quest():
    RGB1.show()
    RGB2.hide()
    button.setText('Ответить')
    Gbuttons.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    Gbuttons.setExclusive(True)
def start_test():
    if button.text() == 'Ответить':
        show_results()
    else:
        show_quest()
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс от SUPERCELL!')
main_win.resize(568,654)
question = QLabel('КАКОЙ УРОН У ШЕЛЛИ НА 9 СИЛЕ?')
button = QPushButton('Ответить')
btn_answer1 = QRadioButton('2090')
btn_answer2 = QRadioButton('1560')
btn_answer3 = QRadioButton('2900')
btn_answer4 = QRadioButton('2100')

Gbuttons = QButtonGroup()
Gbuttons.addButton(btn_answer1)
Gbuttons.addButton(btn_answer2)
Gbuttons.addButton(btn_answer3)
Gbuttons.addButton(btn_answer4)






RGB1 = QGroupBox('Варианты')
h_line = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()

v_line1.addWidget(btn_answer1)
v_line1.addWidget(btn_answer2)
v_line2.addWidget(btn_answer3)
v_line2.addWidget(btn_answer4)

h_line.addLayout(v_line1)
h_line.addLayout(v_line2)

RGB1.setLayout(h_line)


RGB2 = QGroupBox('Результат теста')
v_line2_RGB = QVBoxLayout()
txt1 = QLabel('Правильно/Не правильно')
txt2 = QLabel('правильный ответ тут')
v_line2_RGB.addWidget(txt1)
v_line2_RGB.addWidget(txt2)
RGB2.setLayout(v_line2_RGB)
RGB2.hide()
layout_quest = QVBoxLayout()
layout_quest.addWidget(btn_answer1)


line9 = QVBoxLayout()
line9.addWidget(question)
line9.addWidget(RGB1)
line9.addWidget(RGB2)
line9.addWidget(button)
main_win.setLayout(line9)

button.clicked.connect(start_test)





main_win.show()
app.exec_()
