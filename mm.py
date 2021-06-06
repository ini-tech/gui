import sys
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QMessageBox

# sqlite connection
import sqlite3
db = sqlite3.connect("C:\\Users\\Lenovo\\PycharmProjects\\pythonProject1\\employees.sqlite")
cur = db.cursor()

class Dashboard(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Dashboard, self).__init__(parent)
        uic.loadUi("C:\\Users\\Lenovo\\PycharmProjects\\pythonProject1\\venv\\Lib\\site-packages\\QtDesigner\\MyServiceApp.ui", self)
        self.show()
        self.addserviceBtn.clicked.connect(self.openAddService)
        self.updateBtn.clicked.connect(self.openEditService)
        self.deleteBtn.clicked.connect(self.openDeleteService)
        self.lineEdit.textChanged.connect(self.opensearchdatabase)
        # calling a method directly
        self.populateTablefromdatabase()
    def openAddService(self):
        # opening or calling the Add Service class
        window = AddService(self)
        # closing the current window to prevent multiple windows from opening
        self.hide()
    def openEditService(self):
        window = EditService(self)
        self.hide()
    def openDeleteService(self):
        window = Deleteservice(self)
        self.hide()
    def populateTablefromdatabase(self):
        # selecting all services from the database table
        query = cur.execute('SELECT * FROM Services')
        content = query.fetchall()
        print(content)

        self.servicetableWidget.setRowCount(len(content))
        row = 0 # row vvariable
        for service in content:
            self.servicetableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(service[0]))) # add str as prefix to convert to string
            self.servicetableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(service[1]))
            self.servicetableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(service[2]))
            self.servicetableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(service[3]))#passes into the table any variable in an orderly manner
            row = row + 1



    def opensearchdatabase(self):
        # getting the text to be searched for
        value = self.lineEdit.text()
        # returning matching values from the database
        query = cur.execute(f"SELECT * FROM Services WHERE Title like '%{value}%' or Description like '%{value}%'")
        content = query.fetchall()

        self.servicetableWidget.setRowCount(len(content))
        row = 0  # row vvariable
        for service in content:
            self.servicetableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(
                str(service[0])))  # add str as prefix to convert to string
            self.servicetableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(service[1]))
            self.servicetableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(service[2]))
            self.servicetableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(service[3]))  # passes into the table any variable in an orderly manner
            row = row + 1


class AddService(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AddService, self).__init__(parent)
        uic.loadUi("C:\\Users\\Lenovo\\PycharmProjects\\pythonProject1\\venv\\Lib\\site-packages\\QtDesigner\\AddService.ui", self)
        self.show()
        self.addserviceBtn.clicked.connect(self.addnewService)
        self.dashboardbtn.clicked.connect(self.opendashboard)
    def addnewService(self):
         # getting the content within the text boxes
        title = self.addtitletype.text()
        description = self.descriptiontype.text()
        price = self.pricingtype.text()
        print(title, description, price)
        # add data to database
        status = cur.execute("INSERT into Services (Title,Description,Cost) values(?,?,?)", (title, description, price))
        db.commit()
        print(status)
    def opendashboard(self):
        # Opening the dashboard
        window = Dashboard(self)
        # closing the current page _ add service
        self.hide()


class EditService(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(EditService, self).__init__(parent)
        uic.loadUi(
            "C:\\Users\\Lenovo\\PycharmProjects\\pythonProject1\\venv\\Lib\\site-packages\\QtDesigner\\updateservice.ui",
            self)
        self.show()
        self.updatebtn.clicked.connect(self.editService)
        self.dashboardbtn.clicked.connect(self.opendashboard)

    def editService(self):
        # getting the content within the text boxes
        title = self.addtitletype.text()
        description = self.descriptiontype.text()
        price = self.pricingtype.text()
        print(title, description, price)

        # add data to database
        status = cur.execute("INSERT into Services (Title,Description,Cost) values(?,?,?)", (title, description, price))
        db.commit()
        print(status)

    def opendashboard(self):
        # Opening the dashboard
        window = Dashboard(self)

        # closing the current page _ add service
        self.hide()

class Deleteservice(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Deleteservice, self).__init__(parent)
        uic.loadUi(
            "C:\\Users\\Lenovo\\PycharmProjects\\pythonProject1\\venv\\Lib\\site-packages\\QtDesigner\\Deleteservice.ui",
            self)
        self.show()
        self.dashboardbtn.clicked.connect(self.opendashboard)
        self.deleteBtn.clicked.connect(self.deleteservice)
    def opendashboard(self):
        # getting the content within the text boxes
        window = Dashboard(self)
        self.hide()
    def deleteservice(self):
        # getting the text in the line edits
        column = self.deleteoptionsBtn.currentText()
        value = self.deletetargetBtn.text()

        try:
            # update statement logic
            if column == "ServiceId":
                cur.execute(f"DELETE FROM Services WHERE STAFF ID = {value}")
                db.commit()
            elif column == "Title":
                cur.execute(f"DELETE FROM Services WHERE Title = {value}")
                db.commit()

        except:
            #  popping up a notification unto the screen
            msgbox = QMessageBox(self) # creating the notification
            msgbox.setFixedSize(800,800) # setting the size
            msgbox.setIcon(QMessageBox.warning) # choosing the display icon
            msgbox.setText("Error: Duplicate values found!") # notification message
            msgbox.exec_() # executing the notification command



app = QtWidgets.QApplication(sys.argv)
window = Dashboard()
app.setQuitOnLastWindowClosed(True)
app.exec_()
