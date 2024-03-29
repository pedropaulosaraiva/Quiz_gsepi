# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_inicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_inicial(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1640, 924)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imag/icone_padrao.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.Tela_fundo = QtWidgets.QLabel(Dialog)
        self.Tela_fundo.setGeometry(QtCore.QRect(0, 0, 1661, 931))
        self.Tela_fundo.setStyleSheet("background-image: url(:/imag/Quiz G-SEPi.png);")
        self.Tela_fundo.setText("")
        self.Tela_fundo.setObjectName("Tela_fundo")
        self.Botao_start = QtWidgets.QPushButton(Dialog)
        self.Botao_start.setGeometry(QtCore.QRect(670, 360, 291, 61))
        self.Botao_start.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-left-color: rgb(38, 38, 38);\n"
"border-top-color: rgb(38, 38, 38);\n"
"border-color: rgb(38, 38, 38);\n"
"font: 22pt \"Noto Sans Lisu\";\n"
"background-color: rgb(38, 38, 38);")
        self.Botao_start.setAutoDefault(False)
        self.Botao_start.setFlat(True)
        self.Botao_start.setObjectName("Botao_start")
        self.Botao_instrucoes = QtWidgets.QPushButton(Dialog)
        self.Botao_instrucoes.setGeometry(QtCore.QRect(600, 500, 441, 81))
        self.Botao_instrucoes.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(38, 38, 38);\n"
"font: 22pt \"Noto Sans Lisu\";\n"
"background-color: rgb(38, 38, 38);")
        self.Botao_instrucoes.setAutoDefault(False)
        self.Botao_instrucoes.setFlat(True)
        self.Botao_instrucoes.setObjectName("Botao_instrucoes")
        self.Botao_ranking = QtWidgets.QPushButton(Dialog)
        self.Botao_ranking.setGeometry(QtCore.QRect(590, 660, 461, 81))
        self.Botao_ranking.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(38, 38, 38);\n"
"font: 22pt \"Noto Sans Lisu\";\n"
"background-color: rgb(38, 38, 38);")
        self.Botao_ranking.setAutoDefault(False)
        self.Botao_ranking.setFlat(True)
        self.Botao_ranking.setObjectName("Botao_ranking")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Quiz G-SEPi: Tela de início"))
        self.Botao_start.setText(_translate("Dialog", "COMEÇAR"))
        self.Botao_instrucoes.setText(_translate("Dialog", "INSTRUÇÕES"))
        self.Botao_ranking.setText(_translate("Dialog", "RANKING DE RESULTADOS"))

from res_tela_inicial import tela_inicial_res

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_inicial()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
