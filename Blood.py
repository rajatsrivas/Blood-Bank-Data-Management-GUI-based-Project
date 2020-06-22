from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow=None):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(679, 363)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
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
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
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
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout.addWidget(self.listWidget_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.pushButton_2.clicked.connect(self.updatedata)
        self.spinBox.setRange(-10000,10000)
        self.pushButton.clicked.connect(self.click)

        #self.radioButton.toggled.connect(self.graph)
        #self.radioButton.toggled.connect(self.graph)

        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Graph"))
        self.radioButton.setText(_translate("MainWindow", "Pie Chart"))
        self.radioButton_2.setText(_translate("MainWindow", "Bar Graph"))
        self.pushButton.setText(_translate("MainWindow", "Show Graph"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Blood Available Edit"))
        self.label.setText(_translate("MainWindow", "Select Blood Type and Amount to edit:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox.setItemText(1, _translate("MainWindow", "A+"))
        self.comboBox.setItemText(2, _translate("MainWindow", "A-"))
        self.comboBox.setItemText(3, _translate("MainWindow", "B+"))
        self.comboBox.setItemText(4, _translate("MainWindow", "B-"))
        self.comboBox.setItemText(5, _translate("MainWindow", "O+"))
        self.comboBox.setItemText(6, _translate("MainWindow", "O-"))
        self.comboBox.setItemText(7, _translate("MainWindow", "AB+"))
        self.comboBox.setItemText(8, _translate("MainWindow", "AB-"))
        self.pushButton_2.setText(_translate("MainWindow", "Update Database"))
        self.groupBox.setTitle(_translate("MainWindow", "Blood Available"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "A+"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "A-"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "B-"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "B+"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "O-"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "O+"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "AB+"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "AB-"))
        self.listWidget.setSortingEnabled(__sortingEnabled)




    def updatelist(self):
        self.listWidget_2.clear()
        import sqlite3
        conn = sqlite3.connect("BloodData.db")
        cur = conn.cursor()
        for i in range(8):
            bg=self.listWidget.item(i).text()
            sql= "SELECT * FROM Blood WHERE BloodType='"+bg+"' "
            cursor = cur.execute(sql)
            row= cursor.fetchone()
            #print(row)
            left=row[1]
            #print(left)
            self.listWidget_2.addItem(str(left))

    def updatedata(self):
        import sqlite3
        conn=sqlite3.connect("BloodData.db")
        cur=conn.cursor()
        num = self.spinBox.value()
        bgtxt = self.comboBox.currentText()
        if bgtxt!="None" and num!=0:
            try:
                sql="SELECT UnitLeft FROM Blood WHERE BloodType='"+bgtxt+"' "
                row=cur.execute(sql)
                unit=row.fetchone()
                unit=unit[0]+num
                #print(unit)
                if unit>=0:
                    sql="UPDATE Blood SET UnitLeft= ? WHERE BloodType= ?"
                    #print("OK")
                    curr=conn.execute(sql,(unit,bgtxt))
                    #print("OK")
                    conn.commit()
                    self.msgdlg("Saved Successfully")
                    self.updatelist()
                else:
                    self.msgdlg("Not Enough Unit Available")
            except Exception as e:
                print(e)
                self.msgdlg("Error")
        else:
            self.msgdlg("Select Correct Blood Group and Enter Unit other than 0 to update database")



    def click(self):
        if self.radioButton.isChecked()==True:
            try:
                import matplotlib.pyplot as plt
                import sqlite3
                conn=sqlite3.connect("BloodData.db")
                curr=conn.cursor()
                group=(["A+","A-","B-","B+","O-","O+","AB+","AB-"])
                clr=['b','g','r','c','m','y','k','0.75']
                sql="SELECT UnitLeft FROM Blood"
                cur=curr.execute(sql)
                row=cur.fetchall()
                data=[]
                for i in range(len(row)):
                    a=row[i][0]
                    data.append(a)
                #print(len(data),len(group),len(clr))
                #print(data)
                plt.pie(data,colors=clr,labels=group,startangle=90,shadow=False,radius=1,explode = (0.1, 0.1 ,0.1, 0.1,0.1,0.1,0.1,0.1))
                #plt.legend(group)
                plt.title("Blood Data Pie Chart")
                plt.show()
            except Exception as e:
                print(e)
        elif self.radioButton_2.isChecked()==True:
            try:
                import matplotlib.pyplot as plt
                import sqlite3
                conn=sqlite3.connect("BloodData.db")
                curr=conn.cursor()
                group=(["A+","A-","B-","B+","O-","O+","AB+","AB-"])
                clr=['b','g','r','c','m','y','k','0.75']
                position=[1,2,3,4,5,6,7,8]
                sql="SELECT UnitLeft FROM Blood"
                cur=curr.execute(sql)
                row=cur.fetchall()
                data=[]
                for i in range(len(row)):
                    a=row[i][0]
                    data.append(a)
                #print(len(data),len(group),len(clr))
                #print(data)
                plt.bar(position,data,tick_label=group,width=0.8,color=clr)
                #plt.legend(group)
                plt.xlabel("Blood Group")
                plt.ylabel("Unit Left")
                plt.title("Blood Data Bar Graph")
                plt.show()
            except Exception as e:
                print(e)
        else:
            self.msgdlg("Choose Graph Type to Show")
            
        
            
                
    def msgdlg(self,txt):
        msgdlg=QtWidgets.QMessageBox()
        msgdlg.setText(txt)
        msgdlg.setWindowTitle("Notification")
        _=msgdlg.exec()




    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.updatelist()
    sys.exit(app.exec_())
