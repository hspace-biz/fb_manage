from PyQt6 import QtWidgets,QtGui,QtCore
class Cookie_Import_Item():
    
    def __init__(self,verticalLayout_list_cookie:QtWidgets.QVBoxLayout,
                 groupBox_list_cookie:QtWidgets.QGroupBox,
                 count_uids:QtWidgets.QLabel,
                 count_check:QtWidgets.QLabel,
                 item_cookies:list,
                 uid:str,
                 state:str,
                 cookies:dict
                 ) -> (None):
        self.item_cookies = item_cookies
        self.count_uids = count_uids
        self.count_check = count_check
        self.verticalLayout_list_cookie = verticalLayout_list_cookie
        self.groupBox_list_cookie = groupBox_list_cookie
        self.cookies = cookies
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.groupBox_Cookie_Item = QtWidgets.QGroupBox(self.groupBox_list_cookie)
        self.horizontalLayout_cookie_item = QtWidgets.QHBoxLayout(self.groupBox_Cookie_Item)
        
        self.checkBox_select = QtWidgets.QCheckBox(self.groupBox_Cookie_Item)
        self.checkBox_select.setFont(font)
        
        self.label_uid = QtWidgets.QLabel(self.groupBox_Cookie_Item)
        self.label_uid.setFont(font)
        
        self.label_state = QtWidgets.QLabel(self.groupBox_Cookie_Item)
        self.label_state.setFont(font)
        
        self.pushButton_Remove = QtWidgets.QPushButton(self.groupBox_Cookie_Item)
        self.pushButton_Remove.setFont(font)
        
        
        
        self.groupBox_Cookie_Item.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox_Cookie_Item.setTitle("")
        self.groupBox_Cookie_Item.setObjectName("groupBox_Cookie_Item")
        self.horizontalLayout_cookie_item.setObjectName("horizontalLayout_cookie_item")
        
        self.checkBox_select.setMaximumSize(QtCore.QSize(20, 16777215))
        self.checkBox_select.setText("")
        self.checkBox_select.setObjectName("checkBox_select")
        self.horizontalLayout_cookie_item.addWidget(self.checkBox_select)
        
        self.label_uid.setFont(font)
        self.label_uid.setObjectName("label_uid")
        self.horizontalLayout_cookie_item.addWidget(self.label_uid)
        
        self.label_state.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_state.setObjectName("label_state")
        self.label_state.setFont(font)
        self.horizontalLayout_cookie_item.addWidget(self.label_state)
        
        self.pushButton_Remove.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_Remove.setObjectName("pushButton_Remove")
        self.horizontalLayout_cookie_item.addWidget(self.pushButton_Remove)
        
        _translate = QtCore.QCoreApplication.translate
        self.label_uid.setText(_translate("Import_Cookie", uid))
        self.label_state.setText(_translate("Import_Cookie", state))
        self.pushButton_Remove.setText(_translate("Import_Cookie", "Remove"))
        self.verticalLayout_list_cookie.addWidget(self.groupBox_Cookie_Item)
        
        try:
            count = int(count_uids.text())
            count+=1
            count_uids.setText(str(count))
        except:
            count=1
            count_uids.setText(str(count))
        
        self.pushButton_Remove.clicked[bool].connect(lambda x:self.remove())
        self.checkBox_select.toggled[bool].connect(lambda x:self.toggled())
    def toggled(self):
        if self.checkBox_select.isChecked():
            self.check()
        else:
            self.uncheck()
    def is_checked(self):
        return self.checkBox_select.isChecked()
    
    def _check(self):
        self.checkBox_select.setChecked(True)
        
    def check(self):
       
        try:
            count = int(self.count_check.text())
            count+=1
            self.count_check.setText(str(count))
        except:
            count=0
            self.count_check.setText(str(count))
    
    def _uncheck(self):
        self.checkBox_select.setChecked(False)
        
    def uncheck(self):
       
        try:
            count = int(self.count_check.text())
            count-=1
            self.count_check.setText(str(count))
        except:
            count=0
            self.count_check.setText(str(count))
        print(self.count_check.text())
        
    def remove(self):
        self.item_cookies.remove(self)
        self.groupBox_Cookie_Item.deleteLater()
        self.horizontalLayout_cookie_item.deleteLater()
        try:
            count = int(self.count_uids.text())
            count-=1
            self.count_uids.setText(str(count))
        except:
            count=0
            self.count_uids.setText(str(count))
        
        if self.checkBox_select.isChecked():
            self.uncheck()
            
        
        