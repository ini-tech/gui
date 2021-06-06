import sys
from PyQt5 import QtWidgets, QtGui, uic

class Calculator(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        uic.loadUi("C:\\Users\\Lenovo\\PycharmProjects\\pythonProject1\\venv\\Lib\\site-packages\\QtDesigner\\Call.ui", self)
        self.show()

        # creating a click button for the button
        self.pushButton.clicked.connect(self.performcalculation)

    def performcalculation(self):
        print('Hello')

        # getting text from a line edit
        num1 = self.lineEdit.text()
        print(num1)
        num2 = self.lineEditt.text()
        print(num2)

        # getting the text from a combo box
        sign = self.comboBox.currentText()
        print(sign)

        # converting strings to integers
        num1 = int(num1)
        num2 = int(num2)

        # calculator logic
        try:
            if sign == '+':
                result = num1 + num2
                self.answerbox.setText(str(result))

            elif sign == '-':
                result = num1 - num2
                self.answerbox.setText(str(result))

            elif sign == '/':
                result = num1 / num2
                self.answerbox.setText(str(result))

            elif sign == '*':
                result = num1 * num2
                self.answerbox.setText(str(result))

        except ValueError:
            self.answerbox.setTEXT('Invalid Number')


app = QtWidgets.QApplication(sys.argv)
window = Calculator()
app.setQuitOnLastWindowClosed(True)
app.exec_()
