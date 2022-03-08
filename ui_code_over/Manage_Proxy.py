from typing import List

from main_utils import qtable_utils
from main_utils.api import Proxy, get_list_proxy, login
from main_utils.define import ResultBase
from PyQt6.QtWidgets import (QLabel, QMainWindow, QTableWidget,
                             QTableWidgetItem, QWidget)
from ui_code_raw.Proxy_Manager import Ui_MainWindow_Proxy_Manager

from ui_code_over.Config_Window_Over import Ui_Config_Over
from ui_code_over.Import_Proxy_Over import ImportProxy_Over


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

        self.import_proxy_window = ImportProxy_Over()
        self.import_proxy_window.set_Manage_Proxy(self)
        self.ui_import_proxy_window = QMainWindow()
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
