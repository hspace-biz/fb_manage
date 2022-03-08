from distutils import text_file
from http.client import IM_USED

from Item.Cookie_Item import Cookie_Import_Item
from main_utils import api, define
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from ui_code_raw.Import_Cookies import Ui_Import_Cookie
from ui_code_raw.Result_Insert_Cookie import Ui_Result_Insert_Cookie

from ui_code_over.Config_Window_Over import Ui_Config_Over
from ui_code_over.Import_Proxy_Over import ImportProxy_Over


class Import_Cookies_Over(Ui_Import_Cookie):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton_Check_Cookie.clicked[bool].connect(self.check_cookie)
        self.actionConfig.triggered[bool].connect(self.open_config)
        self.actionFacebook_Account_Manager.triggered[bool].connect(
            lambda: self.open_manager_Facebook_Account_excel())

        self.pushButton_CheckAll.clicked[bool].connect(self.check_all)
        self.pushButton_UncheckAll.clicked[bool].connect(self.uncheck_all)
        self.pushButton_Remove_Item_Selected.clicked[bool].connect(
            self.remove_item_checked)
        self.pushButton_Insert.clicked[bool].connect(self.insert_to_db)
        self.item_cookies = []

    def set_Manager_Facebook_Account_excel(self, window):
        self._Manager_Facebook_Account_excel = window

    def open_manager_Facebook_Account_excel(self):
        print("======================")
        self._Manager_Facebook_Account_excel.setupUi(self.MainWindow)
        self.MainWindow.show()

    def insert_to_db(self):
        list_uid = []

        for item in self.item_cookies:
            if item.is_checked():
                result = api.insert_cookie(cookies=item.cookies,
                                           is_update=self.checkBox_Update_when_exists.isChecked()
                                           )
                if result == define.ResultBase.PERMISSION_DENIED:
                    self.label_result.setText(
                        "This account has no insert permission.")
                    return
                if result == define.ResultBase.OK:
                    list_uid.append(f"updated - {item.cookies['c_user']}")
                if result == define.ResultBase.THE_COOKIE_ALREADY_EXISTS:
                    list_uid.append(f"exists  - {item.cookies['c_user']}")

        self.label_result.setText(
            f"Update Successfull: {len(list_uid)}/{len(self.item_cookies)}")
        ui = Ui_Result_Insert_Cookie()
        text_ = ""
        for uid in list_uid:
            text_ += uid+"\n"
        self.widget_result = QWidget()
        ui.setupUi(self.widget_result)
        ui.textEdit_Result.setText(text_)

        self.widget_result.show()

    def check_all(self):
        for item in self.item_cookies:
            item._check()

    def uncheck_all(self):
        for item in self.item_cookies:
            item._uncheck()

    def remove_item_checked(self):
        list_check = []
        for item in self.item_cookie:
            if item.is_checked():
                list_check.append(item)

        for item in list_check:
            item.remove()

    def open_config(self):
        self.ui_Config_Over = QWidget()
        self._ui_Config_Over = Ui_Config_Over()
        self._ui_Config_Over.setupUi(self.ui_Config_Over)
        self.ui_Config_Over.show()

    def check_cookie(self):
        self.label_count_cookie.setText("0")
        self.item_cookies.clear()
        for chi in self.groupBox_list_cookie.children():
            if chi != self.groupBox_list_cookie and type(chi) != QVBoxLayout:
                chi.deleteLater()
        cookie_text = self.textEdit_import_cookie.toPlainText().replace(" ", "").split("\n")
        uids = []
        for _cookie in cookie_text:
            cookie = {
                "sb": None,
                "xs": None,
                "c_user": None
            }
            _cookie = _cookie.split(";")
            for __cookie in _cookie:
                __cookie = __cookie.split("=")
                if len(__cookie) > 0 and __cookie[0] in cookie.keys():
                    cookie[__cookie[0]] = __cookie[1]
            for key in cookie:
                if cookie.get(key) is None:
                    cookie = None
                    break

            if cookie and cookie.get("c_user") not in uids:
                uids.append(cookie.get("c_user"))
                item = Cookie_Import_Item(
                    self.verticalLayout_list_cookie,
                    self.groupBox_list_cookie,
                    count_uids=self.label_count_cookie,
                    count_check=self.label_count_check,
                    item_cookies=self.item_cookies,
                    uid=cookie.get("c_user"),
                    state="N/A",
                    cookies=cookie
                )
                self.item_cookies.append(item)
