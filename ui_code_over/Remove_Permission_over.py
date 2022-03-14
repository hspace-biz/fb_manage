from typing import List

from main_utils import api, qtable_utils
from main_utils.api import (Facebook_Account, get_all_normal_user,
                            get_list_facebook_account, login)
from main_utils.define import ResultBase
from ui_code_raw.Remove_Permission import Ui_Form_Remove_Permission


class Ui_Form_Remove_Permission_over(Ui_Form_Remove_Permission):

    def setupUi(self, Form_Share_Permission):
        super().setupUi(Form_Share_Permission)
        result, data = get_all_normal_user()
        print(result.msg)
        if result.is_error:
            self.label_result.setText(result.msg)
        self.comboBox_user_code.addItems(data)
        self.load_data()

        self.comboBox_user_code.currentTextChanged.connect(
            lambda x: self.load_data(self.facebook_accounts))

        self.tableWidget_list_account.itemSelectionChanged.connect(
            self.change_item)
        self.pushButton_remove_permission.clicked[bool].connect(
            self.remove_permission
        )
        self.list_uid = []

    def remove_permission(self):
        if len(self.list_uid) <= 0:
            self.label_result.setText("Please choose a few items.")
            return

        data = {
            "random": False,
            "list_uid": self.list_uid,
            "ma_tv": self.comboBox_user_code.currentText(),
            "count": 0
        }
        result, data = api.remove_facebook_from_normal_user(
            data=data)
        self.plainTextEdit_result.setPlainText(str(data))

    def change_item(self):
        self.list_uid = []
        uid_selected = ""
        for item in self.tableWidget_list_account.selectedItems():
            uid = self.tableWidget_list_account.item(item.row(), 0).text()
            print(uid)
            uid_selected += uid+"\n"
            self.list_uid.append(uid)

        self.plainTextEdit_result.setPlainText(uid_selected)

    def load_data(self, facebook_accounts: List[Facebook_Account] = None):
        self.label_result.setText("")
        if facebook_accounts is None:
            result, data = login()
            if result == ResultBase.AUTHENTICATION_CONFIG_NONE:
                self.label_result.setText(data)
                return
            result, data = get_list_facebook_account()
            if result.is_ok:
                pass
            else:
                self.label_result.setText(result.msg+": "+str(data))
                return
            self.facebook_accounts = data
            facebook_accounts = data
        self.data = {}
        list_state = {"": -1}

        self.tableWidget_list_account.clear()
        total = 0
        for account in facebook_accounts:
            if type(account) != Facebook_Account:
                continue
            account = account.__dict__
            for key in account:
                if key == "cookies" or account.get("user_code") != self.comboBox_user_code.currentText():
                    continue
                if not self.data.get(key):
                    self.data[key] = []
                self.data[key].append(str(account[key]))
        qtable_utils.setData(self.tableWidget_list_account, data=self.data)
