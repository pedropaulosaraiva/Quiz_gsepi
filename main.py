from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *

import os, sys

from tela_inicial import Ui_inicial
from tela_instrucoes import  Ui_instrucoes
from tela_login import  Ui_login
from tela_pergunta import Ui_perguntas
from tela_ranking import  Ui_ranking

class tela_inicial(QDialog):

    def __init__(self, *args, **argvs):
        super(tela_inicial, self).__init__(*args, **argvs)
        self.ui = Ui_inicial()
        self.ui.setupUi(self)

        self.ui.Botao_start.clicked.connect(self.ir_login)
        self.ui.Botao_instrucoes.clicked.connect(self.ir_instrucoes)
        self.ui.Botao_ranking.clicked.connect(self.ir_ranking)

        self.window_23 = tela_ranking()
    def ir_login(self):
        self.window_2 = tela_login()
        self.window_2.show()

    def ir_instrucoes(self):
        self.window_22 = tela_instrucoes()
        self.window_22.show()

    def ir_ranking(self):
        self.window_23.show()

class tela_instrucoes(QDialog):
    def __init__(self, *args, **argvs):
        super(tela_instrucoes, self).__init__(*args, **argvs)
        self.ui = Ui_instrucoes()
        self.ui.setupUi(self)

class tela_ranking(QDialog):
    def __init__(self, *args, **argvs):
        super(tela_ranking, self).__init__(*args, **argvs)
        self.ui = Ui_ranking()
        self.ui.setupUi(self)

class tela_login(QDialog):
    def __init__(self, *args, **argvs):
        super(tela_login, self).__init__(*args, **argvs)
        self.ui = Ui_login()
        self.ui.setupUi(self)

        self.ui.Botao_confirmar.clicked.connect(self.ir_perguntas)

    def ir_perguntas(self):
        self.nome_jogador = self.ui.lineEdit_nome.text()

        self.window_3 = tela_pergunta()
        self.window_3.show()
        tela_login.hide(self)
        tela_inicial.hide(window)

class tela_pergunta(QDialog):
    def __init__(self, *args, **argvs):
        super(tela_pergunta, self).__init__(*args, **argvs)
        self.ui = Ui_perguntas()
        self.ui.setupUi(self)

        self.ui.Botao_A1.clicked.connect(self.atualizar_scoreA1)
        self.ui.Botao_A1.clicked.connect(self.atualizar_perguntas)
        self.ui.Botao_A2.clicked.connect(self.atualizar_scoreA2)
        self.ui.Botao_A2.clicked.connect(self.atualizar_perguntas)
        self.ui.Botao_A3.clicked.connect(self.atualizar_scoreA3)
        self.ui.Botao_A3.clicked.connect(self.atualizar_perguntas)
        self.ui.Botao_A4.clicked.connect(self.atualizar_scoreA4)
        self.ui.Botao_A4.clicked.connect(self.atualizar_perguntas)

        #Banco de perguntas e alternativas
        self.perguntas = [["e^pi","pi^e","pi","e","Qual maior número?"],
                          ["3,1435","3,1514","3,1453","3,1409", "Qual número é mais próximo de pi?"],
                          ["9,8","17,4","5,1","12,33", "Qual número mais próximo de pi!?"],
                          ["azul", "branco", "preto", "roxo", "Qual a cor favorita de Pedro?"]]
        self.gabarito = [1, 4, 3, 1]
        #Controle do score
        _translate = QtCore.QCoreApplication.translate
        self.score_num = 0
        self.ui.Score.setText(_translate("Dialog", str(self.score_num)))

        #Controle das perguntas
        self.n_pergunta = 0
        self.ui.Botao_A1.setText(_translate("Dialog", self.perguntas[self.n_pergunta][0]))
        self.ui.Botao_A2.setText(_translate("Dialog", self.perguntas[self.n_pergunta][1]))
        self.ui.Botao_A3.setText(_translate("Dialog", self.perguntas[self.n_pergunta][2]))
        self.ui.Botao_A4.setText(_translate("Dialog", self.perguntas[self.n_pergunta][3]))
        self.ui.Pergunta.setText(_translate("Dialog", self.perguntas[self.n_pergunta][4]))

    def atualizar_perguntas(self):
        if len(self.perguntas) != (self.n_pergunta+1):
            _translate = QtCore.QCoreApplication.translate
            self.n_pergunta = self.n_pergunta + 1
            self.ui.Botao_A1.setText(_translate("Dialog", self.perguntas[self.n_pergunta][0]))
            self.ui.Botao_A2.setText(_translate("Dialog", self.perguntas[self.n_pergunta][1]))
            self.ui.Botao_A3.setText(_translate("Dialog", self.perguntas[self.n_pergunta][2]))
            self.ui.Botao_A4.setText(_translate("Dialog", self.perguntas[self.n_pergunta][3]))
            self.ui.Pergunta.setText(_translate("Dialog", self.perguntas[self.n_pergunta][4]))
        else:
            QMessageBox.information(QMessageBox(), 'Quiz finalizado!', 'Parabéns!\nVocê finalizou o quiz, confira seu resultado no ranking geral')
            window.show()
            tela_pergunta.hide(self)
            window.window_23.ui.tableWidget.setItem(8, 0, QTableWidgetItem(window.window_2.nome_jogador))
            window.window_23.ui.tableWidget.setItem(8, 1, QTableWidgetItem(str(self.score_num)))
            window.window_23.ui.tableWidget.setSortingEnabled(True)
            window.window_23.ui.tableWidget.sortByColumn(1, Qt.DescendingOrder)



    def atualizar_scoreA1(self):
        _translate = QtCore.QCoreApplication.translate
        if self.gabarito[self.n_pergunta] == 1:
            self.score_num = self.score_num + 10
            self.ui.Score.setText(_translate("Dialog", str(self.score_num)))
        else:
            self.score_num = self.score_num - 5
            self.ui.Score.setText(_translate("Dialog", str(self.score_num)))

    def atualizar_scoreA2(self):
        _translate = QtCore.QCoreApplication.translate
        if self.gabarito[self.n_pergunta] == 2:
            self.score_num = self.score_num + 10
            self.ui.Score.setText(_translate("Dialog", str(self.score_num)))
        else:
            self.score_num = self.score_num - 5
            self.ui.Score.setText(_translate("Dialog", str(self.score_num)))

    def atualizar_scoreA3(self):
        _translate = QtCore.QCoreApplication.translate
        if self.gabarito[self.n_pergunta] == 3:
            self.score_num = self.score_num + 10
            self.ui.Score.setText(_translate("Dialog", str(self.score_num)))
        else:
            self.score_num = self.score_num - 5
            self.ui.Score.setText(_translate("Dialog", str(self.score_num)))

    def atualizar_scoreA4(self):
        _translate = QtCore.QCoreApplication.translate
        if self.gabarito[self.n_pergunta] == 4:
            self.score_num = self.score_num + 10
            self.ui.Score.setText(_translate("Dialog", str(self.score_num)))
        else:
            self.score_num = self.score_num - 5
            self.ui.Score.setText(_translate("Dialog", str(self.score_num)))


app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = tela_inicial()
    window.show()
sys.exit(app.exec_())