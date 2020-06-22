from PyQt5 import QtCore, QtGui, QtWidgets

passs="r"
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(714, 558)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout.addWidget(self.listWidget_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.groupBox_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.pushButton.clicked.connect(self.searchdb)
        self.pushButton_2.clicked.connect(self.updateinfo)
        self.pushButton_3.clicked.connect(self.clear)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Information Required"))
        self.label.setText(_translate("Dialog", "Donator\'s E-Mail:"))
        self.pushButton.setText(_translate("Dialog", "Search"))
        self.groupBox_2.setTitle(_translate("Dialog", "Donator\'s Information-"))
        self.label_3.setText(_translate("Dialog", "Fields"))
        self.label_2.setText(_translate("Dialog", "Information"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "Email-Id"))
        item = self.listWidget.item(1)
        item.setText(_translate("Dialog", "Donator Name"))
        item = self.listWidget.item(2)
        item.setText(_translate("Dialog", "Blood Type"))
        item = self.listWidget.item(3)
        item.setText(_translate("Dialog", "Unit Donated"))
        item = self.listWidget.item(4)
        item.setText(_translate("Dialog", "Award/Certification Eligible"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_3.setTitle(_translate("Dialog", "Update Field"))
        self.label_4.setText(_translate("Dialog", "Information to Edit"))
        self.comboBox.setItemText(0, _translate("Dialog", "None"))
        self.comboBox.setItemText(1, _translate("Dialog", "EmailId"))
        self.comboBox.setItemText(2, _translate("Dialog", "DonorName"))
        self.comboBox.setItemText(3, _translate("Dialog", "BloodType"))
        self.comboBox.setItemText(4, _translate("Dialog", "UnitDonated"))
        self.pushButton_2.setText(_translate("Dialog", "Update"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))

    def updateinfo(self):
        import sqlite3
        conn = sqlite3.connect("BloodData.db")
        cur=conn.cursor()
        t=self.lineEdit.text()
        try:
            if t!="":
                sql="Select * from DonorData where EmailId='"+t+"';"
                curr=cur.execute(sql)
                row=curr.fetchall()
                row=list(row[0])
                if row[3]>=10:
                    row.append("Yes")
                else:
                    row.append("No")
                self.listWidget_2.clear()
                for i in row:
                    self.listWidget_2.addItem(str(i))
                #choice=["No","Yes"]
                field=self.comboBox.currentText()
                if field!="None":
                    info, ok=QtWidgets.QInputDialog.getText(None, "Update Information", "Enter New Information:")
                    if ok and info!="":
                        text1,ok1= QtWidgets.QInputDialog.getText(None, "Password", "Enter Password to Proceed:")
                        if ok1 and text1==passs:
                            try:
                                if field=="EmailId":
                                    sql="UPDATE DonorData SET EmailId= ? WHERE EmailId= ?"
                                    currr=cur.execute(sql,(info,t))
                                    conn.commit()
                                    self.showdlg("Data Updated")
                                    self.clear()

                                elif field=="DonorName":
                                    sql="UPDATE DonorData SET UserName= ? WHERE EmailId= ?"
                                    currr=cur.execute(sql,(info,t))
                                    conn.commit()
                                    self.showdlg("Data Updated")
                                    self.clear()

                                elif field=="BloodType":
                                    sql="UPDATE DonorData SET BloodType= ? WHERE EmailId= ?"
                                    currr=cur.execute(sql,(info,t))
                                    conn.commit()
                                    self.showdlg("Data Updated")
                                    self.clear()

                                elif field=="UnitDonated":
                                    sql="UPDATE DonorData SET UnitDonated= ? WHERE EmailId= ?"
                                    currr=cur.execute(sql,(info,t))
                                    conn.commit()
                                    self.showdlg("Data Updated")
                                    self.clear()
                            except Exception as e:
                                print(e)
                                msgdlg("Error in Deleting")
                        else:
                            self.msgdlg("Wrong Password")
                            self.clear()
                    else:
                        self.clear()
                else:
                    self.msgdlg("Enter Correct Field")
            else:
                self.msgdlg("No Data Entered")
        except Exception as e:
            #print(e)
            self.msgdlg("Data Not Found")

    
    def clear(self):
        self.lineEdit.clear()
        self.listWidget_2.clear()
    

    def searchdb(self):
        import sqlite3
        conn = sqlite3.connect("BloodData.db")
        cur=conn.cursor()
        t=self.lineEdit.text()
        try:
            if t!="":
                sql="Select * from DonorData where EmailId='"+t+"';"
                curr=cur.execute(sql)
                row=curr.fetchall()
                row=list(row[0])
                if row[3]>=10:
                    row.append("Yes")
                else:
                    row.append("No")
                self.listWidget_2.clear()
                for i in row:
                    self.listWidget_2.addItem(str(i))
            else:
                self.msgdlg("No Data Entered")
        except Exception as e:
            self.msgdlg("Data Not Found")

    def showdlg(self,msg):
        showbx= QtWidgets.QMessageBox()
        showbx.setText(msg)
        showbx.setWindowTitle("Notification")
        x=showbx.exec()


    
    def msgdlg(self,msg):
        msgbx= QtWidgets.QMessageBox()
        msgbx.setText(msg)
        msgbx.setWindowTitle("Error")
        x=msgbx.exec()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
