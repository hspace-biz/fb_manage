# Form implementation generated from reading ui file './ui/Config_Window.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Config(object):
    def setupUi(self, Config):
        Config.setObjectName("Config")
        Config.resize(529, 163)
        Config.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Config)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Config)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_server = QtWidgets.QLineEdit(Config)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_server.setFont(font)
        self.lineEdit_server.setText("")
        self.lineEdit_server.setObjectName("lineEdit_server")
        self.horizontalLayout.addWidget(self.lineEdit_server)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Config)
        self.label_4.setMinimumSize(QtCore.QSize(100, 0))
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_server_port = QtWidgets.QLineEdit(Config)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_server_port.setFont(font)
        self.lineEdit_server_port.setText("")
        self.lineEdit_server_port.setObjectName("lineEdit_server_port")
        self.horizontalLayout_4.addWidget(self.lineEdit_server_port)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Config)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_User_Name = QtWidgets.QLineEdit(Config)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_User_Name.setFont(font)
        self.lineEdit_User_Name.setText("")
        self.lineEdit_User_Name.setObjectName("lineEdit_User_Name")
        self.horizontalLayout_2.addWidget(self.lineEdit_User_Name)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Config)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_User_Pass = QtWidgets.QLineEdit(Config)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_User_Pass.setFont(font)
        self.lineEdit_User_Pass.setText("")
        self.lineEdit_User_Pass.setObjectName("lineEdit_User_Pass")
        self.horizontalLayout_3.addWidget(self.lineEdit_User_Pass)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_Check = QtWidgets.QPushButton(Config)
        self.pushButton_Check.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Check.setFont(font)
        self.pushButton_Check.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_Check.setObjectName("pushButton_Check")
        self.horizontalLayout_5.addWidget(self.pushButton_Check)
        self.label_result = QtWidgets.QLabel(Config)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.horizontalLayout_5.addWidget(self.label_result)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Config)
        QtCore.QMetaObject.connectSlotsByName(Config)

    def retranslateUi(self, Config):
        _translate = QtCore.QCoreApplication.translate
        Config.setWindowTitle(_translate("Config", "Configs Window"))
        self.label.setText(_translate("Config", "Server Ip:"))
        self.label_4.setText(_translate("Config", "Server Port:"))
        self.label_2.setText(_translate("Config", "User Name:"))
        self.label_3.setText(_translate("Config", "Password"))
        self.pushButton_Check.setText(_translate("Config", "Check"))
