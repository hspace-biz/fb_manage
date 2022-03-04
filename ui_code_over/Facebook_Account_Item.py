from ui_code_raw.Facebook_Account_Item import Ui_Facebook_Item
from main_utils.api import Facebook_Account
class Ui_Facebook_Item_Over(Ui_Facebook_Item):
    def setupUi(self, Facebook_Item):
        super().setupUi(Facebook_Item)
    def set_data(self,data:Facebook_Account):
        self.label_uid.setText(str(data.uid))
        self.label_name.setText(str(data.name))
        self.label_master_code.setText(str(data.master_code))
        self.label_usercode.setText(str(data.user_code))
        self.label_state.setText(str(data.state))
        self.label_last_time_action.setText(str(data.last_time_action))
        self.label_action_name.setText(str(data.last_action))
        self.label_last_time_update_friend.setText(str(data.last_time_update_friends))
        self.label_last_time_update_profile.setText(str(data.last_time_update_profile))
        self.label_last_time_update_state.setText(str(data.last_time_update_state))
        