import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from FahrenheitConverter import Ui_MainWindow
from WordGuesser import Ui_Guesser
from Writer import Ui_MainWindow as Ui_Writer


class TemperatureConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(TemperatureConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Fahrenheit')
        self.ui.line_Input.setPlaceholderText(
            'Entry temperature in Fahrenheit:')

        self.ui.btn_Convert.clicked.connect(self.converter)
        self.ui.btn_Quit.clicked.connect(self.close)

    def converter(self):
        input_line = int(self.ui.line_Input.text())
        celseus = f'{round((input_line-32)*5/9, 2)} in celsius'
        self.ui.label_Input.setText(str(celseus))


class WordGuesser(QtWidgets.QMainWindow):
    words = {
        'car': 'автомобиль', 'boat': 'лодка', 'helicopter': 'вертолёт', 'bike': 'велосипед',
        'driver': 'водитель', 'wheel': 'колесо', 'magazine': 'журнал'}
    counter = 5

    def __init__(self):
        super(WordGuesser, self).__init__()
        self.ui = Ui_Guesser()
        self.ui.setupUi(self)
        random.seed()
        self.init_Guess()

    def init_Guess(self):
        self.setWindowTitle('Word guesser')

        self.ruword = ''
        i = random.randint(0, len(self.words))
        for key, val in self.words.items():
            if i == 0:
                self.ruword = val
            i -= 1
        self.ui.label_ruword.setText(self.ruword)
        self.ui.lcdNumber.display(self.counter)

        self.ui.pushButton_confirm.clicked.connect(self.guessing)

    def guessing(self):
        enword = self.ui.lineEdit_enword.text()
        f = False
        for key, var in self.words.items():
            if self.ruword == var and enword == key:
                f = True
                self.ui.label.setText('Вы угадали!')
                self.ui.lcdNumber.display(999)
        if not f:
            self.ui.label.setText('Вы не угадали :(')
            self.counter -= 1
            self.ui.lcdNumber.display(self.counter)
            self.ui.lineEdit_enword.setText('')
            if self.counter == 0:
                self.close()

class Writer(QtWidgets.QMainWindow):
    def __init__(self):
        super(Writer, self).__init__()
        self.ui = Ui_Writer()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('File creator')
        self.ui.textEdit.setPlaceholderText('Entry text there:')
        self.ui.comboBox.addItem('txt')
        self.ui.comboBox.addItem('html')

        self.ui.pushButton.clicked.connect(self.genfile)

    def genfile(self):
        text = self.ui.textEdit.toPlainText()
        if self.ui.comboBox.currentIndex() == 0:
            file = open('Legal.txt', 'w')
            file.write(text)
            file.close()
        else:
            file = open('Illegal.html', 'w')
            file.write(text)
            file.close()


if __name__ == '__main__':
    ex = int(input('Введите номер задания: '))
    if ex == 1:
        app = QtWidgets.QApplication([])
        appllication = TemperatureConv()
        appllication.show()
        sys.exit(app.exec_())
    elif ex == 2:
        app = QtWidgets.QApplication([])
        appllication = WordGuesser()
        appllication.show()
        sys.exit(app.exec_())
    elif ex == 3:
        app = QtWidgets.QApplication([])
        appllication = Writer()
        appllication.show()
        sys.exit(app.exec_())
