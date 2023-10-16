from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QPushButton
from random import randint

app= QApplication([])
win =  QWidget()

win.setWindowTitle("Рандомайзер")
win.resize(3000,3050)

text=QLabel(win)
text.setText("Натисніть,щоб дізнатися переможця")
text.move(550,350)

text2 = QLabel(win)
text2.setText("?")
text2.move(635,400)

button = QPushButton(win)
button.setText("Згенерувати")
button.move(600,450)
text.setStyleSheet("color:fuchsia;font-size:25px")
win.setStyleSheet("background:white")

def show_win():
    num = randint(1,100)
    text2.setText(str(num))
    text.setText("Переможець:")
button.clicked.connect(show_win)


win.show()
app.exec_()