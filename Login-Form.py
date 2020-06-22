idd="r"
passs="r"
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(413, 306)
        self.formLayoutWidget = QtWidgets.QWidget(LoginPage)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 30, 371, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.horizontalLayoutWidget = QtWidgets.QWidget(LoginPage)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 190, 371, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)



        self.pushButton_2.clicked.connect(self.login)
        self.pushButton.clicked.connect(self.clear)




        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "Dialog"))
        self.label.setText(_translate("LoginPage", "USER-ID:"))
        self.label_2.setText(_translate("LoginPage", "PASSWORD:"))
        self.pushButton_2.setText(_translate("LoginPage", "LOGIN"))
        self.pushButton.setText(_translate("LoginPage", "CLEAR"))

    def login(self):
        eid=self.lineEdit.text()
        epass=self.lineEdit_2.text()
        
        if eid==idd and epass==passs:
            from BloodBank import Ui_MainWindow
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.MainWindow)
            LoginPage.hide()
            self.MainWindow.show()
        else:
            self.msgdlg("Wrong ID or Password!")
        


    def clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()


    def msgdlg(self,msg):
        msgdlg=QtWidgets.QMessageBox()
        msgdlg.setText(msg)
        msgdlg.setWindowTitle("Error")
        _=msgdlg.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QDialog()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())
