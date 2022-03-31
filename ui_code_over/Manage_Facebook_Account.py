
import threading
from threading import Thread
from tkinter import Widget
from typing import List

import PyQt6
from configs import DATA_FOLDER
from main_utils import qtable_utils
from main_utils.api import (Facebook_Account, get_all_normal_user,
                            get_list_facebook_account, get_list_proxy, login)
from main_utils.define import ResultBase
from main_utils.str_utils import remove_accent
from PyQt6.QtWidgets import (QLabel, QMainWindow, QTableWidget,
                             QTableWidgetItem, QWidget)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from seleniumwire import webdriver
from ui_code_raw.Manage_Facebook_Account import Ui_Manage_Facebook_Account
from webdriver_manager.chrome import ChromeDriverManager

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

        self.actionProxy_Manager.triggered[bool].connect(
            self.open_manage_proxy)

        self.facebook_accounts = None
        self.pushButton_Reload.clicked[bool].connect(
            lambda x: self.load_data())
        self.pushButton_reset.clicked[bool].connect(
            lambda x: self.reset_filter())
        self.list_statistics_state_child = None

        self.list_account = []
        self.list_proxy = []

        self.load_data()
        self.lineEdit_filter_name.textChanged.connect(self.filter)
        self.lineEdit_filter_user_code.textChanged.connect(self.filter)
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
        self.pushButton_login.clicked.connect(self.login)

        self.driver = None
        self.tableWidget_list_account.clicked.connect(self.detect_login)
        self.pushButton_login.setEnabled(False)
        self.current_list_fb_account = None

    def detect_login(self):
        indexs = self.tableWidget_list_account.selectedIndexes()

        if len(indexs) <= 0:
            self.pushButton_login.setEnabled(False)
            return
        if self.current_list_fb_account is None:
            self.pushButton_login.setEnabled(False)
            return
        uid = self.current_list_fb_account[indexs[0].row()].uid
        print(uid)
        _proxy = None
        for proxy in self.list_proxy:
            if proxy.facebook_uid == uid:
                _proxy = proxy
                break
        if _proxy is None:
            self.pushButton_login.setEnabled(False)
            return
        self.pushButton_login.setEnabled(True)

    def __login__(self):
        if self.current_list_fb_account is None:
            self.pushButton_login.setEnabled(False)
            return
        indexs = self.tableWidget_list_account.selectedIndexes()
        if len(indexs) <= 0:
            return
        cookies = self.current_list_fb_account[indexs[0].row()].cookies
        uid = self.current_list_fb_account[indexs[0].row()].uid
        _proxy = None
        for proxy in self.list_proxy:
            if proxy.facebook_uid == uid:
                _proxy = proxy
                break
        if _proxy is None:
            return
        options = {
            'proxy': {
                'https': f'https://{proxy.user_name}:{proxy.password}@{proxy.ip}:{proxy.port}',
            }
        }
        opts = Options()
        opts.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36")
        # opts.add_argument('--ignore-certificate-errors')

        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(), seleniumwire_options=options, chrome_options=opts)

        self.driver.get("https://mbasic.facebook.com")

        for cookie in cookies:
            self.driver.add_cookie(
                {"name": cookie.get("name"), "value": cookie.get("value")})

        self.driver.get("https://mbasic.facebook.com")

    def login(self):
        if self.driver:
            try:
                self.driver.close()
                self.driver.quit()
            except:
                pass
        self.login_thread = threading.Thread(target=self.__login__)
        self.login_thread.start()

    def open_remove_permission(self):
        self.remove_permission_windows = QWidget()
        self.remove_permission = Ui_Form_Remove_Permission_over()
        self.remove_permission.setupUi(self.remove_permission_windows)
        self.remove_permission_windows.show()

    def open_share_permission(self):
        indexs = self.tableWidget_list_account.selectedIndexes()
        data = ""
        for index in indexs:
            uid = self.tableWidget_list_account.item(index.row(), 0)
            if uid is None:
                continue
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
        self.import_cookie_window = QMainWindow()
        import_cookie = Import_Cookies_Over()
        import_cookie.setupUi(self.import_cookie_window)
        import_cookie.set_Manager_Facebook_Account_excel(
            Ui_Manage_Facebook_Account_Over())
        self.import_cookie_window.show()

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
                list_data_2 = list_data
        else:
            list_data_2 = list_data

        list_data_3 = []
        if self.checkBox_filter_user_code.isChecked():
            text = self.lineEdit_filter_user_code.text()
            if len(text) > 0:
                for account in list_data_2:
                    if str(account.user_code).find(text) >= 0:
                        list_data_3.append(account)
            else:
                list_data_3 = list_data_2
        else:
            list_data_3 = list_data_2

        list_data_2 = list_data_3

        list_data_3 = []
        if self.checkBox_filter_state.isChecked():
            text = self.comboBox_filter_state.currentText()
            if len(text) > 0:
                for account in list_data_2:
                    if str(account.state) == text:
                        list_data_3.append(account)
            else:
                list_data_3 = list_data_2
        else:
            list_data_3 = list_data_2

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

            result, list_proxy = get_list_proxy()
            if result.is_ok:
                pass
            else:
                self.label_result_api.setText(result.msg+": "+str(list_proxy))
                return
            self.list_proxy = list_proxy
            self.list_account = [account for account in data]
            for account in self.list_account:
                uid = account.uid
                account.has_a_proxy = False
                for proxy in self.list_proxy:
                    if proxy.facebook_uid == uid:
                        account.has_a_proxy = True
                        break

        self.data = {}
        list_state = {"": -1}

        self.tableWidget_list_account.clear()
        total = 0
        self.current_list_fb_account = facebook_accounts
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
