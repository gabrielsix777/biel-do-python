# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 650)
        MainWindow.setMinimumSize(QtCore.QSize(400, 650))
        MainWindow.setMaximumSize(QtCore.QSize(400, 650))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(100, 100))
        self.frame.setStyleSheet("font: 87 36pt \"Arial Black\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.outputLabel = QtWidgets.QLabel(self.frame)
        self.outputLabel.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: #000;\n"
"color: #fff;")
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.verticalLayout.addWidget(self.outputLabel)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clearButton = QtWidgets.QPushButton(self.frame_2)
        self.clearButton.setMinimumSize(QtCore.QSize(99, 106))
        self.clearButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(177, 177, 177);")
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_2.addWidget(self.clearButton)
        self.percentageButton = QtWidgets.QPushButton(self.frame_2)
        self.percentageButton.setMinimumSize(QtCore.QSize(99, 106))
        self.percentageButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(177, 177, 177);")
        self.percentageButton.setObjectName("percentageButton")
        self.horizontalLayout_2.addWidget(self.percentageButton)
        self.backspaceButton = QtWidgets.QPushButton(self.frame_2)
        self.backspaceButton.setMinimumSize(QtCore.QSize(99, 106))
        self.backspaceButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(177, 177, 177);")
        self.backspaceButton.setObjectName("backspaceButton")
        self.horizontalLayout_2.addWidget(self.backspaceButton)
        self.divisionButton = QtWidgets.QPushButton(self.frame_2)
        self.divisionButton.setMinimumSize(QtCore.QSize(99, 106))
        self.divisionButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);\n"
"")
        self.divisionButton.setObjectName("divisionButton")
        self.horizontalLayout_2.addWidget(self.divisionButton)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.seteButton = QtWidgets.QPushButton(self.frame_3)
        self.seteButton.setMinimumSize(QtCore.QSize(99, 106))
        self.seteButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.seteButton.setObjectName("seteButton")
        self.horizontalLayout_3.addWidget(self.seteButton)
        self.oitoButton = QtWidgets.QPushButton(self.frame_3)
        self.oitoButton.setMinimumSize(QtCore.QSize(99, 106))
        self.oitoButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.oitoButton.setObjectName("oitoButton")
        self.horizontalLayout_3.addWidget(self.oitoButton)
        self.novebutton = QtWidgets.QPushButton(self.frame_3)
        self.novebutton.setMinimumSize(QtCore.QSize(99, 106))
        self.novebutton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.novebutton.setObjectName("novebutton")
        self.horizontalLayout_3.addWidget(self.novebutton)
        self.mutiplicacaoButton = QtWidgets.QPushButton(self.frame_3)
        self.mutiplicacaoButton.setMinimumSize(QtCore.QSize(99, 106))
        self.mutiplicacaoButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);\n"
"")
        self.mutiplicacaoButton.setObjectName("mutiplicacaoButton")
        self.horizontalLayout_3.addWidget(self.mutiplicacaoButton)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.quatroButton = QtWidgets.QPushButton(self.frame_4)
        self.quatroButton.setMinimumSize(QtCore.QSize(99, 106))
        self.quatroButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.quatroButton.setObjectName("quatroButton")
        self.horizontalLayout_4.addWidget(self.quatroButton)
        self.cincoButton = QtWidgets.QPushButton(self.frame_4)
        self.cincoButton.setMinimumSize(QtCore.QSize(99, 106))
        self.cincoButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.cincoButton.setObjectName("cincoButton")
        self.horizontalLayout_4.addWidget(self.cincoButton)
        self.seisButton = QtWidgets.QPushButton(self.frame_4)
        self.seisButton.setMinimumSize(QtCore.QSize(99, 106))
        self.seisButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.seisButton.setObjectName("seisButton")
        self.horizontalLayout_4.addWidget(self.seisButton)
        self.menosButton = QtWidgets.QPushButton(self.frame_4)
        self.menosButton.setMinimumSize(QtCore.QSize(99, 106))
        self.menosButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);\n"
"")
        self.menosButton.setObjectName("menosButton")
        self.horizontalLayout_4.addWidget(self.menosButton)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.umButton = QtWidgets.QPushButton(self.frame_5)
        self.umButton.setMinimumSize(QtCore.QSize(99, 106))
        self.umButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.umButton.setObjectName("umButton")
        self.horizontalLayout_5.addWidget(self.umButton)
        self.doisButton = QtWidgets.QPushButton(self.frame_5)
        self.doisButton.setMinimumSize(QtCore.QSize(99, 106))
        self.doisButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.doisButton.setObjectName("doisButton")
        self.horizontalLayout_5.addWidget(self.doisButton)
        self.tresButton = QtWidgets.QPushButton(self.frame_5)
        self.tresButton.setMinimumSize(QtCore.QSize(99, 106))
        self.tresButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.tresButton.setObjectName("tresButton")
        self.horizontalLayout_5.addWidget(self.tresButton)
        self.maisButton = QtWidgets.QPushButton(self.frame_5)
        self.maisButton.setMinimumSize(QtCore.QSize(99, 106))
        self.maisButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);\n"
"")
        self.maisButton.setObjectName("maisButton")
        self.horizontalLayout_5.addWidget(self.maisButton)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.zeroButton = QtWidgets.QPushButton(self.frame_6)
        self.zeroButton.setMinimumSize(QtCore.QSize(99, 106))
        self.zeroButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.zeroButton.setObjectName("zeroButton")
        self.horizontalLayout_6.addWidget(self.zeroButton)
        self.maismenosButton = QtWidgets.QPushButton(self.frame_6)
        self.maismenosButton.setMinimumSize(QtCore.QSize(99, 106))
        self.maismenosButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.maismenosButton.setObjectName("maismenosButton")
        self.horizontalLayout_6.addWidget(self.maismenosButton)
        self.pontobutton = QtWidgets.QPushButton(self.frame_6)
        self.pontobutton.setMinimumSize(QtCore.QSize(99, 106))
        self.pontobutton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.pontobutton.setObjectName("pontobutton")
        self.horizontalLayout_6.addWidget(self.pontobutton)
        self.igualButton = QtWidgets.QPushButton(self.frame_6)
        self.igualButton.setMinimumSize(QtCore.QSize(99, 106))
        self.igualButton.setStyleSheet("font: 87 36pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);\n"
"")
        self.igualButton.setObjectName("igualButton")
        self.horizontalLayout_6.addWidget(self.igualButton)
        self.verticalLayout.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "calculadoraPython"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.clearButton.setText(_translate("MainWindow", "ac"))
        self.percentageButton.setText(_translate("MainWindow", "%"))
        self.backspaceButton.setText(_translate("MainWindow", "<<"))
        self.divisionButton.setText(_translate("MainWindow", "/"))
        self.seteButton.setText(_translate("MainWindow", "7"))
        self.oitoButton.setText(_translate("MainWindow", "8"))
        self.novebutton.setText(_translate("MainWindow", "9"))
        self.mutiplicacaoButton.setText(_translate("MainWindow", "*"))
        self.quatroButton.setText(_translate("MainWindow", "4"))
        self.cincoButton.setText(_translate("MainWindow", "5"))
        self.seisButton.setText(_translate("MainWindow", "6"))
        self.menosButton.setText(_translate("MainWindow", "-"))
        self.umButton.setText(_translate("MainWindow", "1"))
        self.doisButton.setText(_translate("MainWindow", "2"))
        self.tresButton.setText(_translate("MainWindow", "3"))
        self.maisButton.setText(_translate("MainWindow", "+"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.maismenosButton.setText(_translate("MainWindow", "+/-"))
        self.pontobutton.setText(_translate("MainWindow", "."))
        self.igualButton.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
