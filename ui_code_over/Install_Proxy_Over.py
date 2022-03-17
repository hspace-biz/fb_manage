from faulthandler import is_enabled

from main_utils.api import get_all_normal_user, install_proxy, uninstall_proxy
from ui_code_raw.Install_Proxy import Ui_Form_Install_Proxy


class Ui_Form_Install_Proxy(Ui_Form_Install_Proxy):
    def setupUi(self, Form_Install_Proxy):
        super().setupUi(Form_Install_Proxy)
        self.radioButton_input.toggled[bool].connect(self.enable_input)
        self.pushButton_install.clicked[bool].connect(self.install_proxy)
        self.pushButton_uninstall.clicked[bool].connect(self.uninstall_proxy)
        retsult, data = get_all_normal_user()
        self.comboBox_user_code.addItems(data)

    def install_proxy(self):
        list_uids = []
        for uid in self.plainTextEdit_Input.toPlainText().split("/n"):
            if len(uid) > 3:
                list_uids.append(uid)
        if self.radioButton_input.isChecked() == False:
            list_uids = None
        is_disable = None
        if self.radioButton_disable.isChecked():
            is_disable = True

        if self.radioButton_enable.isChecked():
            is_disable = False
        user_code = self.comboBox_user_code.currentText()
        result, data = install_proxy(
            user_code=user_code, list_uids=list_uids, is_disable=is_disable)
        self.plainTextEdit_result.setPlainText(result.msg+"  "+str(data))

    def uninstall_proxy(self):
        list_uids = []
        for uid in self.plainTextEdit_Input.toPlainText().split("/n"):
            if len(uid) > 3:
                list_uids.append(uid)
        if self.radioButton_input.isChecked() == False:
            list_uids = None
        is_disable = None
        if self.radioButton_disable.isChecked():
            is_disable = True

        if self.radioButton_enable.isChecked():
            is_disable = False
        user_code = self.comboBox_user_code.currentText()
        result, data = uninstall_proxy(
            user_code=user_code, list_uids=list_uids, is_disable=is_disable)
        self.plainTextEdit_result.setPlainText(result.msg+"  "+str(data))

    def enable_input(self):
        self.plainTextEdit_Input.setReadOnly(
            self.radioButton_input.isChecked() == False)
