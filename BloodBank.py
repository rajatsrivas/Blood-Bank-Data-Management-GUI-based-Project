from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 551)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setIndent(6)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setIndent(6)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setIndent(6)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(9, "")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(10, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setIndent(6)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(13, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBlood = QtWidgets.QAction(MainWindow)
        self.actionBlood.setObjectName("actionBlood")
        self.actionDonator_Detail = QtWidgets.QAction(MainWindow)
        self.actionDonator_Detail.setObjectName("actionDonator_Detail")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionDelete_Info = QtWidgets.QAction(MainWindow)
        self.actionDelete_Info.setObjectName("actionDelete_Info")
        self.actionEdit_Info = QtWidgets.QAction(MainWindow)
        self.actionEdit_Info.setObjectName("actionEdit_Info")
        self.menuFile.addAction(self.actionBlood)
        self.menuFile.addAction(self.actionDonator_Detail)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionDelete_Info)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionEdit_Info)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())



        self.menuFile.triggered[QtWidgets.QAction].connect(self.menu)
        self.menuEdit.triggered[QtWidgets.QAction].connect(self.menuedit)

        self.pushButton_2.clicked.connect(self.mainscr)
        self.pushButton.clicked.connect(self.clear)

        

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Donator\'s Name:"))
        self.label_2.setText(_translate("MainWindow", "Donator\'s Email:"))
        self.label_3.setText(_translate("MainWindow", "Blood Group Type:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox.setItemText(1, _translate("MainWindow", "A+"))
        self.comboBox.setItemText(2, _translate("MainWindow", "A-"))
        self.comboBox.setItemText(3, _translate("MainWindow", "B+"))
        self.comboBox.setItemText(4, _translate("MainWindow", "B-"))
        self.comboBox.setItemText(5, _translate("MainWindow", "AB+"))
        self.comboBox.setItemText(6, _translate("MainWindow", "AB-"))
        self.comboBox.setItemText(7, _translate("MainWindow", "O+"))
        self.comboBox.setItemText(8, _translate("MainWindow", "O-"))
        self.label_4.setText(_translate("MainWindow", "Unit Donated:"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.pushButton.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "DataBase"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionBlood.setText(_translate("MainWindow", "Blood"))
        self.actionDonator_Detail.setText(_translate("MainWindow", "Donator Detail"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionDelete_Info.setText(_translate("MainWindow", "Delete Info"))
        self.actionEdit_Info.setText(_translate("MainWindow", "Edit Info"))
        

    def menu(self,action):
        txt=(action.text())
        if txt=="Blood":
            try:
                from Blood import Ui_MainWindow
                self.MainWindow1 = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.MainWindow1)
                #MainWindow.hide()
                self.ui.updatelist()
                self.MainWindow1.show()
            except Exception as e:
                print(e)
        elif txt =="Donator Detail":
            from DonatorDetail import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            _=Dialog.exec()
        else:
            import sys
            self.msgdlg("""Thankyou for Using BloodBank""")
            sys.exit()
        
    
    def menuedit(self,action):
        txt=action.text()
        if txt=="Delete Info":
            from DeleteInfo import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            p=Dialog.exec()
        elif txt=="Edit Info":
            from EditInfo import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            p=Dialog.exec()

    def mainscr(self):
        import sqlite3
        conn = sqlite3.connect("BloodData.db")
        dn = self.lineEdit.text()
        de = self.lineEdit_2.text()
        bg = self.comboBox.currentText()
        ud = self.lineEdit_3.text()
        #print(dn,de,bg,ud)
        sql="INSERT INTO DonorData (EmailId, UserName,BloodType,UnitDonated) VALUES ('"+de+"','"+dn+"','"+bg+"','"+(ud)+"');"
        try:
            cur=conn.execute(sql)
            sq="SELECT UnitLeft from Blood where BloodType='"+bg+"';"
            curr=conn.execute(sq)
            unit=curr.fetchone()
            #print(type(unit[0]))
            unit=int(unit[0])+int(ud)
            #print("ok")
            sq="UPDATE Blood SET UnitLeft=? WHERE BloodType=?"
            #print("OK1")
            curr=conn.execute(sq,(unit,bg))
            self.msgdlg("Detail saved Successfully!")
            conn.commit()
            self.clear()
        except Exception as e:
            #print(e)
            self.msgdlg("Error")
            conn.rollback()

    def clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.comboBox.setCurrentIndex(0)


        
    def msgdlg(self,msg):
        msgdlg=QtWidgets.QMessageBox()
        msgdlg.setText(msg)
        msgdlg.setWindowTitle("BloodBank")
        _=msgdlg.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
