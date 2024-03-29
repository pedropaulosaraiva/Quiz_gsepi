# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_ranking.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *


class Ui_ranking(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(820, 462)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imag-rank/icone_padrao.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.tela_fundo = QtWidgets.QLabel(Dialog)
        self.tela_fundo.setGeometry(QtCore.QRect(0, 0, 831, 471))
        self.tela_fundo.setStyleSheet("background-image: url(:/imag-rank/5.png);")
        self.tela_fundo.setText("")
        self.tela_fundo.setObjectName("tela_fundo")
        self.label_iNSTRUCOES = QtWidgets.QLabel(Dialog)
        self.label_iNSTRUCOES.setGeometry(QtCore.QRect(330, 40, 201, 51))
        self.label_iNSTRUCOES.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"Noto Sans Lisu\";")
        self.label_iNSTRUCOES.setObjectName("label_iNSTRUCOES")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(270, 140, 301, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Quiz G-SEPi: Ranking"))
        self.label_iNSTRUCOES.setText(_translate("Dialog", "RANKING"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "->"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "->"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "->"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "->"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "->"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "->"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "->"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "->"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "->"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "NOME"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "SCORE"))

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Pedro"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("40"))
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)
        #self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
from res_tela_ranking import ranking_res


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ranking()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
