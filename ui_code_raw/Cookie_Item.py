# Form implementation generated from reading ui file './ui/Cookie_Item.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(599, 279)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_7 = QtWidgets.QGroupBox(Form)
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 180))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_ip = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ip.setFont(font)
        self.label_ip.setObjectName("label_ip")
        self.horizontalLayout_2.addWidget(self.label_ip)
        self.horizontalLayout_6.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_port = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_port.setFont(font)
        self.label_port.setObjectName("label_port")
        self.horizontalLayout_3.addWidget(self.label_port)
        self.horizontalLayout_6.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_username = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.horizontalLayout_4.addWidget(self.label_username)
        self.horizontalLayout_6.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_password = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.horizontalLayout_5.addWidget(self.label_password)
        self.horizontalLayout_6.addWidget(self.groupBox_4)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 70))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_RemoveUid = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_RemoveUid.setMaximumSize(QtCore.QSize(50, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_RemoveUid.setFont(font)
        self.pushButton_RemoveUid.setObjectName("pushButton_RemoveUid")
        self.horizontalLayout_9.addWidget(self.pushButton_RemoveUid)
        self.label_port_4 = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_port_4.setFont(font)
        self.label_port_4.setObjectName("label_port_4")
        self.horizontalLayout_9.addWidget(self.label_port_4)
        self.horizontalLayout.addWidget(self.groupBox_8)
        self.pushButton_CheckConnection = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_CheckConnection.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_CheckConnection.setFont(font)
        self.pushButton_CheckConnection.setObjectName("pushButton_CheckConnection")
        self.horizontalLayout.addWidget(self.pushButton_CheckConnection)
        self.label = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_Remove = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_Remove.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Remove.setFont(font)
        self.pushButton_Remove.setObjectName("pushButton_Remove")
        self.horizontalLayout.addWidget(self.pushButton_Remove)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.verticalLayout.addWidget(self.groupBox_7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_5.setTitle(_translate("Form", "Info"))
        self.groupBox.setTitle(_translate("Form", "Ip"))
        self.label_ip.setText(_translate("Form", "255.255.255.255"))
        self.groupBox_2.setTitle(_translate("Form", "Port"))
        self.label_port.setText(_translate("Form", "1111"))
        self.groupBox_3.setTitle(_translate("Form", "User name"))
        self.label_username.setText(_translate("Form", "xxxxxx"))
        self.groupBox_4.setTitle(_translate("Form", "Password"))
        self.label_password.setText(_translate("Form", "xxxxxx"))
        self.groupBox_8.setTitle(_translate("Form", "Uid"))
        self.pushButton_RemoveUid.setText(_translate("Form", "Remove"))
        self.label_port_4.setText(_translate("Form", "100000000000"))
        self.pushButton_CheckConnection.setText(_translate("Form", "Check connection"))
        self.label.setText(_translate("Form", "N/A"))
        self.pushButton_Remove.setText(_translate("Form", "Remove"))
