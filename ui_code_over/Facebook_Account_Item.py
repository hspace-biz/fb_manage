from main_utils.api import Facebook_Account
from PyQt6 import QtGui
from ui_code_raw.Facebook_Account_Item import Ui_Facebook_Item


class Ui_Facebook_Item_Over(Ui_Facebook_Item):
    def setupUi(self, Facebook_Item):
        super().setupUi(Facebook_Item)

    def set_data(self, data: Facebook_Account):
        self.lineEdit_uid.setText(str(data.uid))
        self.lineEdit_name.setText(str(data.name))
        self.label_master_code.setText(str(data.master_code))
        self.label_usercode.setText(str(data.user_code))
        self.lineEdit_state.setText(str(data.state))
        self.label_last_time_action.setText(str(data.last_time_action))
        self.lineEdit_action_name.setText(str(data.last_action))
        self.label_last_time_update_friend.setText(
            str(data.last_time_update_friends))
        self.label_last_time_update_profile.setText(
            str(data.last_time_update_profile))
        self.label_last_time_update_state.setText(
            str(data.last_time_update_state))
        self.data = data
        self.set_color()

    def set_color(self):
        if self.data.state is None:
            self.__set_color(self.groupBox_item, 50, 50, 10)
        elif self.data.state != "OK":
            self.__set_color(self.groupBox_item, 250, 50, 10)
        else:
            self.__set_color(self.groupBox_item, 0, 50, 10)

    def __set_color(self, ob, r, g, b):
        color = QtGui.QColor(r, g, b)
        alpha = 10
        values = "{r}, {g}, {b}, {a}".format(r=color.red(),
                                             g=color.green(),
                                             b=color.blue(),
                                             a=alpha
                                             )
        ob.setStyleSheet(
            f"{type(ob).__name__} "+"{ background-color: rgba("+values+"); }")
