
from tkinter import Widget
from typing import List

import PyQt6
from main_utils import qtable_utils
from main_utils.api import (Facebook_Account, get_all_normal_user,
                            get_list_facebook_account, login)
from main_utils.define import ResultBase
from main_utils.str_utils import remove_accent
from PyQt6.QtWidgets import (QLabel, QMainWindow, QTableWidget,
                             QTableWidgetItem, QWidget)
from ui_code_raw.Manage_Facebook_Account import Ui_Manage_Facebook_Account

from ui_code_over.Config_Window_Over import Ui_Config_Over
from ui_code_over.Import_Cookies_Over import Import_Cookies_Over
from ui_code_over.Manage_Proxy import Ui_Proxy_Manager_Over
from ui_code_over.Remove_Permission_over import Ui_Form_Remove_Permission_over
from ui_code_over.Share_Permission_over import Ui_Form_Share_Permission_over


class Ui_Manage_Facebook_Account_Over(Ui_Manage_Facebook_Account):
    """_summary_

    Args:
        Ui_Manage_Facebook_Account (_type_): _description_
    """

    def setupUi(self, Manage_Facebook_Account):
        super().setupUi(Manage_Facebook_Account)
        self.window = Manage_Facebook_Account
        self.actionConfigs_Authentication.triggered[bool].connect(
            self.open_config)
        self.actionImport_Cookie.triggered[bool].connect(
            self.import_cookie
        )
        self.actionConfigs_Authentication.triggered[bool].connect(
            self.import_cookie
        )
        self.actionProxy_Manager.triggered[bool].connect(
            self.open_manage_proxy)

        self.facebook_accounts = None
        self.pushButton_Reload.clicked[bool].connect(
            lambda x: self.load_data())
        self.pushButton_reset.clicked[bool].connect(
            lambda x: self.reset_filter())
        self.list_statistics_state_child = None

        self.load_data()
        self.lineEdit_filter_name.textChanged.connect(self.filter)
        self.lineEdit_filter_uid.textChanged.connect(self.filter)
        self.comboBox_filter_state.currentTextChanged.connect(self.filter)
        self.checkBox_filter_name.toggled[bool].connect(self.filter)
        self.checkBox_filter_uid.toggled[bool].connect(self.filter)
        self.checkBox_filter_state.toggled[bool].connect(self.filter)
        self.pushButton_share_permissions.clicked[bool].connect(
            self.open_share_permission)
        self.pushButton_remove_permissions.clicked[bool].connect(
            self.open_remove_permission
        )

    def open_remove_permission(self):
        self.remove_permission_windows = QWidget()
        self.remove_permission = Ui_Form_Remove_Permission_over()
        self.remove_permission.setupUi(self.remove_permission_windows)
        self.remove_permission_windows.show()

    def open_share_permission(self):
        indexs = self.tableWidget_list_account.selectedIndexes()
        data = ""
        for index in indexs:
            uid = self.tableWidget_list_account.item(0, index.row())
            data += uid.text()+"\n"
        self.permission_windows = QWidget()
        self.share_permission = Ui_Form_Share_Permission_over()
        self.share_permission.setupUi(self.permission_windows)
        self.share_permission.set_list_uid(data)
        self.permission_windows.show()

    def open_manage_proxy(self):

        proxy_mamager = Ui_Proxy_Manager_Over()
        proxy_mamager.setupUi(self.window)
        proxy_mamager.set_Facebook_Account_Manager(self)
        self.window.show()

    def import_cookie(self):
        import_cookie = Import_Cookies_Over()
        import_cookie.setupUi(self.window)
        import_cookie.set_Manager_Facebook_Account_excel(
            Ui_Manage_Facebook_Account_Over())
        self.window.show()

    def reset_filter(self):
        self.checkBox_filter_name.setChecked(False)
        self.checkBox_filter_uid.setChecked(False)
        self.checkBox_filter_state.setChecked(False)
        self.lineEdit_filter_name.setText("")
        self.lineEdit_filter_uid.setText("")
        self.comboBox_filter_state.setCurrentIndex(0)

    def filter(self):
        list_data = []
        if self.checkBox_filter_name.isChecked():
            text = self.lineEdit_filter_name.text()

            if len(text) > 0:
                text = remove_accent(text)
                for account in self.facebook_accounts:
                    if remove_accent(str(account.name)).find(text) >= 0:
                        list_data.append(account)
            else:
                list_data = self.facebook_accounts.copy()
        else:
            list_data = self.facebook_accounts.copy()

        list_data_2 = []
        if self.checkBox_filter_uid.isChecked():
            text = self.lineEdit_filter_uid.text()
            if len(text) > 0:
                for account in list_data:
                    if str(account.uid).find(text) >= 0:
                        list_data_2.append(account)
            else:
                list_data_2 = list_data.copy()
        else:
            list_data_2 = list_data.copy()

        list_data_3 = []
        if self.checkBox_filter_state.isChecked():
            text = self.comboBox_filter_state.currentText()
            if len(text) > 0:
                for account in list_data_2:
                    if str(account.state) == text:
                        list_data_3.append(account)
            else:
                list_data_3 = list_data_2.copy()
        else:
            list_data_3 = list_data_2.copy()

        self.load_data(facebook_accounts=list_data_3)

    def load_data(self, facebook_accounts: List[Facebook_Account] = None):
        self.label_result_api.setText("")
        if facebook_accounts is None:
            result, data = login()
            if result == ResultBase.AUTHENTICATION_CONFIG_NONE:
                self.label_result_api.setText(data)
                return
            result, data = get_list_facebook_account()
            if result.is_ok:
                pass
            else:
                self.label_result_api.setText(result.msg+": "+str(data))
                return
            self.comboBox_filter_state.clear()
            self.facebook_accounts = data
            facebook_accounts = data
        self.data = {}
        list_state = {"": -1}

        self.tableWidget_list_account.clear()
        total = 0
        for account in facebook_accounts:
            account = account.__dict__
            for key in account:
                if key == "cookies":
                    continue
                if key == "state":
                    if list_state.get(str(account[key])) is None:
                        list_state[str(account[key])] = 0
                    list_state[str(account[key])] += 1
                    total += 1

                if not self.data.get(key):
                    self.data[key] = []
                self.data[key].append(str(account[key]))
        qtable_utils.setData(self.tableWidget_list_account, data=self.data)
        if self.comboBox_filter_state.count() <= 0:
            self.comboBox_filter_state.addItems(list_state.keys())
        if self.list_statistics_state_child:
            for child in self.list_statistics_state_child:
                child.deleteLater()
        self.list_statistics_state_child = []

        label = QLabel(self.scrollAreaWidgetContents_statistics)
        label.setText(f"Total: {total}")
        self.verticalLayout_statistics.addWidget(label)
        self.list_statistics_state_child.append(label)
        for state in list_state:
            if len(state) > 0:
                label = QLabel(self.scrollAreaWidgetContents_statistics)
                label.setText(f"{state}: {list_state[state]}")
                self.verticalLayout_statistics.addWidget(label)
                self.list_statistics_state_child.append(label)
        result, data = get_all_normal_user()
        if result.is_error:
            self.label_result_api.setText(str(data))
            return

    def open_config(self):
        self.ui_Config_Over = QWidget()
        self._ui_Config_Over = Ui_Config_Over()
        self._ui_Config_Over.setupUi(self.ui_Config_Over)
        self.ui_Config_Over.show()
