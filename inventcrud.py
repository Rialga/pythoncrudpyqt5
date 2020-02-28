# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crud.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import cursor as cursor
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import DBconnection as Db
import datetime


class Ui_MainWindow(object):

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def kontil(self):
        self.messagebox("fuck","anjink")

    def koneksi(self):
        con = Db.DBConnection.getConnection()
        cur = con.cursor()

        if (cur):
             self.messagebox("Test Data", "Koneksi Berhasil")
             self.messagebox("Koneksi", "Koneksi Berhasil")
        else:
             self.messagebox("Koneksi", "Koneksi Gagal")

    def input(self):
        con = pymysql.connect(host='localhost', user='root', password='', db='inventaris')
        cur = con.cursor()

        nama = self.textnama.text()
        jenis = str(self.cmbboxjenis.currentText())

        gettgl = self.tglmasuk.text()
        # tglmasuk = datetime.strptime(gettgl, '%d/%m/%y')

        sql1 = "SELECT COUNT(*) FROM data_inventaris WHERE inventaris_jenis ='"+str(jenis)+"'"

        urut  =cur.execute(sql1) + 1
        no_inven = "LBI.1.'"+str(urut)+"'"

        self.messagebox("Notif", " "+no_inven+" ")
        #
        #
        # sql2 = ("insert into data_inventaris(inventaris_no, inventaris_nama, inventaris_jenis, inventaris_tglmasuk) values(%s,%s,%s,%s)")
        # data = cur.execute(sql2,(no_inven,nama,jenis,gettgl))

        # if (data):
        #     self.messagebox("Notif", "Input data berhasil")
        # else:
        #     self.messagebox("Notif", "Input data gagal")



    def setupUi(self, MainWindow):
        self.koneksi()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(834, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 250, 271, 181))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 113, 47, 20))
        self.label_3.setObjectName("label_3")


        self.btnclear = QtWidgets.QPushButton(self.groupBox)
        self.btnclear.setGeometry(QtCore.QRect(200, 140, 51, 31))
        self.btnclear.setObjectName("btnclear")


        self.cmbboxjenis = QtWidgets.QComboBox(self.groupBox)
        self.cmbboxjenis.setGeometry(QtCore.QRect(100, 30, 111, 22))
        self.cmbboxjenis.setObjectName("cmbboxjenis")
        self.cmbboxjenis.addItem("LAMA")
        self.cmbboxjenis.addItem("PENDEK")



        self.textnama = QtWidgets.QLineEdit(self.groupBox)
        self.textnama.setGeometry(QtCore.QRect(100, 110, 113, 20))
        self.textnama.setObjectName("textnama")


        self.tglmasuk = QtWidgets.QDateEdit(self.groupBox)
        self.tglmasuk.setGeometry(QtCore.QRect(100, 70, 110, 22))
        self.tglmasuk.setObjectName("tglmasuk")


        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 47, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 61, 20))
        self.label_2.setObjectName("label_2")


        self.btndelete = QtWidgets.QPushButton(self.groupBox)
        self.btndelete.setGeometry(QtCore.QRect(20, 140, 51, 31))
        self.btndelete.setObjectName("btndelete")


        self.btnedit = QtWidgets.QPushButton(self.groupBox)
        self.btnedit.setGeometry(QtCore.QRect(80, 140, 51, 31))
        self.btnedit.setObjectName("btnedit")


        self.btninput = QtWidgets.QPushButton(self.groupBox)
        self.btninput.setGeometry(QtCore.QRect(140, 140, 51, 31))
        self.btninput.setObjectName("btninput")
        self.btninput.clicked.connect(self.input)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 80, 651, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")


        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(340, 230, 431, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)


        self.btncari = QtWidgets.QPushButton(self.centralwidget)
        self.btncari.setGeometry(QtCore.QRect(714, 200, 51, 23))
        self.btncari.setObjectName("btncari")


        self.textcari = QtWidgets.QLineEdit(self.centralwidget)
        self.textcari.setGeometry(QtCore.QRect(590, 200, 113, 20))
        self.textcari.setObjectName("textcari")


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 200, 113, 20))
        self.lineEdit.setObjectName("textcek")


        self.btncek = QtWidgets.QPushButton(self.centralwidget)
        self.btncek.setGeometry(QtCore.QRect(240, 200, 75, 23))
        self.btncek.setObjectName("btncek")
        self.btncek.clicked.connect(self.kontil)


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 200, 47, 21))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "PENDATAAN INVENTARIS"))
        self.label_3.setText(_translate("MainWindow", "NAMA"))
        self.btnclear.setText(_translate("MainWindow", "CLEAR"))
        self.cmbboxjenis.setItemText(0, _translate("MainWindow", "LAMA"))
        self.cmbboxjenis.setItemText(1, _translate("MainWindow", "PENDEK"))
        self.label.setText(_translate("MainWindow", "JENIS"))
        self.label_2.setText(_translate("MainWindow", "TGL MASUK"))
        self.btndelete.setText(_translate("MainWindow", "DELETE"))
        self.btnedit.setText(_translate("MainWindow", "EDIT"))
        self.btninput.setText(_translate("MainWindow", "INPUT"))
        self.label_4.setText(_translate("MainWindow", "PENGELOLAAN INVENTARIS LBI"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No Inventaris"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nama"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Jenis"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tanggal Masuk"))
        self.btncari.setText(_translate("MainWindow", "CARI"))
        self.btncek.setText(_translate("MainWindow", "Check"))
        self.label_5.setText(_translate("MainWindow", "No Invent"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
