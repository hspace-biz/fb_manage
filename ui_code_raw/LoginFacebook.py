# Form implementation generated from reading ui file './ui/LoginFacebook.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_LoginFacebook(object):
    def setupUi(self, Form_LoginFacebook):
        Form_LoginFacebook.setObjectName("Form_LoginFacebook")
        Form_LoginFacebook.resize(654, 615)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_LoginFacebook)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_result = QtWidgets.QLabel(Form_LoginFacebook)
        self.label_result.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Form_LoginFacebook)
        QtCore.QMetaObject.connectSlotsByName(Form_LoginFacebook)

    def retranslateUi(self, Form_LoginFacebook):
        _translate = QtCore.QCoreApplication.translate
        Form_LoginFacebook.setWindowTitle(_translate("Form_LoginFacebook", "Login Facebook"))
