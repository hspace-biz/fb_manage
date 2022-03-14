from operator import is_
from select import select
from typing import List

from main_utils.api import (get_all_normal_user,
                            share_facebook_from_master_user_to_normal_user)
from ui_code_raw.Share_Permission import Ui_Form_Share_Permission


class Ui_Form_Share_Permission_over(Ui_Form_Share_Permission):

    def setupUi(self, Form_Share_Permission):
        super().setupUi(Form_Share_Permission)
        self.checkBox_random.toggled[bool].connect(self.disable_input)
        self.pushButton_share_permission.clicked[bool].connect(
            self.share_permissions)

        result, data = get_all_normal_user()
        if result.is_error:
            self.label_result.setText(result.msg)
        self.comboBox_user_code.addItems(data)

    def set_list_uid(self, list_uid: str):

        self.plainTextEdit_list_uid.setPlainText(list_uid)

    def share_permissions(self):
        data = []
        count = None

        if self.checkBox_random.isChecked() == False:
            data = self.plainTextEdit_list_uid.toPlainText()
            for char in data:
                if char != '\n' and (char < '0' or char > '9'):
                    self.label_result.setText("Input incorrect")
                    return
            data = data.split("\n")
            if len(data) <= 0:
                self.label_result.setText("Plase enter list uid.")
                return
        else:
            count = self.lineEdit_number_account.text()
            try:
                count = int(count)
            except:
                self.label_result.setText("Count account is number")
                return
        list_uid = []
        for uid in data:
            is_valid = True
            for char in uid:
                if char < '0' or char > '9':
                    is_valid = False
                    break
            if len(uid) < 4:
                is_valid = False
            if is_valid:
                list_uid.append(uid)
        data = {
            "random": self.checkBox_random.isChecked(),
            "list_uid": list_uid,
            "ma_tv": self.comboBox_user_code.currentText(),
            "count": count
        }
        result, data = share_facebook_from_master_user_to_normal_user(
            data=data)

        self.plainTextEdit_result.setPlainText(str(data))

    def disable_input(self):
        if self.checkBox_random.isChecked():
            self.plainTextEdit_list_uid.setReadOnly(True)
            self.lineEdit_number_account.setReadOnly(False)
        else:
            self.plainTextEdit_list_uid.setReadOnly(False)
            self.lineEdit_number_account.setReadOnly(True)
