# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'criccom.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(370, 431)
        Dialog.setMinimumSize(QtCore.QSize(370, 391))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setMouseTracking(False)
        Dialog.setWindowOpacity(0.9)
        Dialog.setToolTip("")
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(36, 36, 36);\n"
"font: 12pt \"Russo One\";\n"
"color:rgb(255, 255, 255);")
        self.matchinput = QtWidgets.QTextEdit(Dialog)
        self.matchinput.setGeometry(QtCore.QRect(60, 80, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.matchinput.setFont(font)
        self.matchinput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.matchinput.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.matchinput.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.matchinput.setObjectName("matchinput")
        self.compname = QtWidgets.QLabel(Dialog)
        self.compname.setGeometry(QtCore.QRect(60, 48, 151, 21))
        self.compname.setStyleSheet("color: #20B2AA;\n"
"font-size: 24px;")
        self.compname.setObjectName("compname")
        self.teama = QtWidgets.QLabel(Dialog)
        self.teama.setGeometry(QtCore.QRect(60, 130, 71, 16))
        self.teama.setObjectName("teama")
        self.teamb = QtWidgets.QLabel(Dialog)
        self.teamb.setGeometry(QtCore.QRect(60, 160, 71, 16))
        self.teamb.setObjectName("teamb")
        self.scorea = QtWidgets.QLabel(Dialog)
        self.scorea.setGeometry(QtCore.QRect(230, 130, 51, 16))
        self.scorea.setObjectName("scorea")
        self.scoreb = QtWidgets.QLabel(Dialog)
        self.scoreb.setGeometry(QtCore.QRect(230, 160, 47, 13))
        self.scoreb.setObjectName("scoreb")
        self.status = QtWidgets.QLabel(Dialog)
        self.status.setGeometry(QtCore.QRect(60, 210, 251, 51))
        self.status.setStyleSheet("font-size:14px;")
        self.status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.status.setObjectName("status")
        self.commentary = QtWidgets.QLabel(Dialog)
        self.commentary.setGeometry(QtCore.QRect(60, 300, 251, 91))
        self.commentary.setStyleSheet("font-size:12px;")
        self.commentary.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.commentary.setWordWrap(True)
        self.commentary.setObjectName("commentary")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 80, 41, 31))
        self.pushButton.setStyleSheet("background:#9FE37D;\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CricCom"))
        Dialog.setWhatsThis(_translate("Dialog", "Enter the name of the match Eg. India vs England for live commentary!"))
        self.matchinput.setPlaceholderText(_translate("Dialog", "Enter the live match ..."))
        self.compname.setText(_translate("Dialog", "CricCom"))
        self.teama.setText(_translate("Dialog", "Team A"))
        self.teamb.setText(_translate("Dialog", "Team B"))
        self.scorea.setText(_translate("Dialog", "Score"))
        self.scoreb.setText(_translate("Dialog", "Score"))
        self.status.setText(_translate("Dialog", "Status"))
        self.commentary.setText(_translate("Dialog", "Commentary"))
        self.pushButton.setText(_translate("Dialog", "GO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
