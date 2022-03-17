from re import S
from tkinter import Widget
from typing import List

from main_utils import qtable_utils
from main_utils.api import Proxy, get_list_proxy, login
from main_utils.define import ResultBase
from main_utils.str_utils import remove_accent
from PyQt6.QtWidgets import (QLabel, QMainWindow, QTableWidget,
                             QTableWidgetItem, QWidget)
from ui_code_raw.Proxy_Manager import Ui_MainWindow_Proxy_Manager

from ui_code_over.Config_Window_Over import Ui_Config_Over
from ui_code_over.Import_Proxy_Over import Ui_ImportProxy_over
from ui_code_over.Install_Proxy_Over import Ui_Form_Install_Proxy


class Ui_Proxy_Manager_Over(Ui_MainWindow_Proxy_Manager):

    def setupUi(self, window):
        super().setupUi(window)
        self.window = window
        self.actionFacebook_Manager.triggered[bool].connect(
            lambda x: self.open_Facebook_Account_Manager())
        self.actionAuthentication.triggered[bool].connect(
            lambda x: self.open_config()
        )
        self.actionImport_Proxy.triggered[bool].connect(
            lambda x: self.open_import_proxy()
        )
        self.load_data()
        self.lineEdit_ip.textChanged.connect(self.filter)
        self.lineEdit_port.textChanged.connect(self.filter)
        self.lineEdit_user_name.textChanged.connect(self.filter)
        self.lineEdit_password.textChanged.connect(self.filter)
        self.lineEdit_facebook_id.textChanged.connect(self.filter)
        self.lineEdit_facebook_name.textChanged.connect(self.filter)

        self.checkBox_ip.toggled[bool].connect(self.filter)
        self.checkBox_port.toggled[bool].connect(self.filter)
        self.checkBox_password.toggled[bool].connect(self.filter)
        self.checkBox_user_name.toggled[bool].connect(self.filter)
        self.checkBox_facebook_id.toggled[bool].connect(self.filter)
        self.checkBox_facebook_name.toggled[bool].connect(self.filter)

        self.pushButton_install_proxy.clicked[bool].connect(
            self.open_install_proxy)

    def open_install_proxy(self):
        self.install_proxy_windows = QWidget()
        self.install_proxy = Ui_Form_Install_Proxy()
        self.install_proxy.setupUi(self.install_proxy_windows)
        self.install_proxy_windows.show()

    def filter(self):
        list_data = []
        if self.checkBox_user_name.isChecked():
            text = self.lineEdit_user_name.text()
            if len(text) > 0:
                text = remove_accent(text)
                for account in self.list_proxy:
                    if remove_accent(str(account.user_name)).find(text) >= 0:
                        list_data.append(account)
            else:
                list_data = self.list_proxy.copy()
        else:
            list_data = self.list_proxy.copy()

        list_data_1 = []
        if self.checkBox_facebook_name.isChecked():
            text = self.lineEdit_facebook_name.text()
            if len(text) > 0:
                text = remove_accent(text)
                for account in list_data:
                    if remove_accent(str(account.facebook_name)).find(text) >= 0:
                        list_data_1.append(account)
            else:
                list_data_1 = list_data.copy()
        else:
            list_data_1 = list_data.copy()
        list_data = list_data_1

        list_data_1 = []
        if self.checkBox_facebook_id.isChecked():
            text = self.lineEdit_facebook_id.text()
            if len(text) > 0:
                for account in list_data:
                    if str(account.facebook_id).find(text) >= 0:
                        list_data_1.append(account)
            else:
                list_data_1 = list_data.copy()
        else:
            list_data_1 = list_data.copy()
        list_data = list_data_1

        list_data_1 = []
        if self.checkBox_ip.isChecked():
            text = self.lineEdit_ip.text()
            if len(text) > 0:
                for account in list_data:
                    print(account.ip)
                    if str(account.ip).find(text) >= 0:
                        list_data_1.append(account)
            else:
                list_data_1 = list_data.copy()
        else:
            list_data_1 = list_data.copy()
        list_data = list_data_1

        list_data_1 = []
        if self.checkBox_port.isChecked():
            text = self.lineEdit_port.text()
            if len(text) > 0:
                for account in list_data:
                    if str(account.port).find(text) >= 0:
                        list_data_1.append(account)
            else:
                list_data_1 = list_data.copy()
        else:
            list_data_1 = list_data.copy()
        list_data = list_data_1

        list_data_1 = []
        if self.checkBox_password.isChecked():
            text = self.lineEdit_password.text()
            if len(text) > 0:
                for account in list_data:
                    if str(account.password).find(text) >= 0:
                        list_data_1.append(account)
            else:
                list_data_1 = list_data.copy()
        else:
            list_data_1 = list_data.copy()
        list_data = list_data_1

        self.load_data(list_proxy=list_data)

    def load_data(self, list_proxy: List[Proxy] = None):
        self.label_result_api.setText("")
        if list_proxy is None:
            result, data = login()
            if result == ResultBase.AUTHENTICATION_CONFIG_NONE:
                self.label_result_api.setText(data)
                return
            result, data = get_list_proxy()
            if result.is_ok:
                pass
            else:
                self.label_result_api.setText(result.msg+": "+str(data))
                return
            self.list_proxy = data
            list_proxy = data
        self.data = {}

        self.tableWidget_list_proxy.clear()
        for proxy in list_proxy:
            proxy = proxy.__dict__
            for key in proxy:
                if not self.data.get(key):
                    self.data[key] = []
                self.data[key].append(str(proxy[key]))
        qtable_utils.setData(self.tableWidget_list_proxy, data=self.data)

    def open_import_proxy(self):
        self.import_proxy_window = Ui_ImportProxy_over()
        self.ui_import_proxy_window = QWidget()
        self.import_proxy_window.setupUi(self.ui_import_proxy_window)
        self.ui_import_proxy_window.show()

    def open_config(self):
        self.ui_Config_Over = QWidget()
        self._ui_Config_Over = Ui_Config_Over()
        self._ui_Config_Over.setupUi(self.ui_Config_Over)
        self.ui_Config_Over.show()

    def open_Facebook_Account_Manager(self):
        window = QMainWindow()
        self.facebook_Account_Manager.setupUi(window)
        window.show()
        self.window.close()
        self.window.deleteLater()

    def set_Facebook_Account_Manager(self, facebook_Account_Manager):
        self.facebook_Account_Manager = facebook_Account_Manager
