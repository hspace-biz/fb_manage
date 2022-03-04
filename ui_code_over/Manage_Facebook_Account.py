from main_utils.api import get_list_facebook_account, login
from main_utils.define import ResultBase
from main_utils.str_utils import remove_accent
from PyQt6.QtWidgets import QWidget
from ui_code_raw.Manage_Facebook_Account import Ui_Manage_Facebook_Account

from ui_code_over.Config_Window_Over import Ui_Config_Over
from ui_code_over.Facebook_Account_Item import Ui_Facebook_Item_Over


class Ui_Manage_Facebook_Account_Over(Ui_Manage_Facebook_Account):
    """_summary_

    Args:
        Ui_Manage_Facebook_Account (_type_): _description_
    """

    def setupUi(self, Manage_Facebook_Account):
        super().setupUi(Manage_Facebook_Account)
        result, data = login()
        if result.is_ok:
            pass
        else:
            self.label_result_api.setText(result.msg+": "+str(data))
            return

        result, data = get_list_facebook_account()
        self.list_item = []
        self.list_widget_item = []
        self.list_data = []

        if result.is_ok:
            self.list_account = data
            states = [""]
            for account in self.list_account:
                if str(account.state) not in states:
                    states.append(str(account.state))
                self.add_item(data=account)
            self.comboBox_filter_state.addItems(states)

            data = "Ok"
        else:
            self.list_account = []

        self.label_result_api.setText(result.msg+": "+str(data))
        self.actionConfigs_Authentication.triggered[bool].connect(
            self.open_config)
        self.lineEdit_filter_uid.textChanged.connect(self.filter_uid)
        self.lineEdit_filter_name.textChanged.connect(self.filter_name)
        self.comboBox_filter_state.currentIndexChanged.connect(
            self.filter_state)

    def filter_state(self):
        text = self.comboBox_filter_state.currentText()
        if len(text) > 0:
            self.remove_all_item()
            for account in self.list_account:
                if str(account.state) == text or len(text) <= 0:
                    self.add_item(data=account)

    def filter_name(self):
        text = self.lineEdit_filter_name.text()
        if len(text) > 0:
            text = remove_accent(text)

            self.remove_all_item()
            for account in self.list_account:
                if remove_accent(str(account.name)).find(text) >= 0:
                    self.add_item(data=account)

    def filter_uid(self):
        text = self.lineEdit_filter_uid.text()
        if len(text) > 0:
            self.remove_all_item()
            for account in self.list_account:
                if account.uid.find(text) >= 0:
                    self.add_item(data=account)

    def open_config(self):
        self.ui_Config_Over = QWidget()
        self._ui_Config_Over = Ui_Config_Over()
        self._ui_Config_Over.setupUi(self.ui_Config_Over)
        self.ui_Config_Over.show()

    def add_item(self, data: dict):
        item = Ui_Facebook_Item_Over()
        widget_item = QWidget(self.scrollArea_list_facebook_account)
        item.setupUi(widget_item)
        item.set_data(data=data)

        self.verticalLayout_list_facebook_account.addWidget(widget_item)
        self.list_item.append(item)
        self.list_widget_item.append(widget_item)
        item.set_color()

    def remove_all_item(self):
        for item in self.list_widget_item:
            item.deleteLater()
        self.list_widget_item.clear()

    def reset_list_item(self):
        for item in self.list_item:
            widget_item = QWidget(self.scrollArea_list_facebook_account)
            item.setupUi(widget_item)
            self.verticalLayout_list_facebook_account.addWidget(widget_item)
            self.list_widget_item.append(widget_item)
            item.set_color()
