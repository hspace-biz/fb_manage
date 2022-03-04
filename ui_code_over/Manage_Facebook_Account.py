from ui_code_raw.Manage_Facebook_Account import Ui_Manage_Facebook_Account
from ui_code_over.Facebook_Account_Item import Ui_Facebook_Item_Over
from PyQt6.QtWidgets import QWidget
from main_utils.api import get_list_facebook_account,login
from main_utils.define import ResultBase

class Ui_Manage_Facebook_Account_Over(Ui_Manage_Facebook_Account):
    def setupUi(self, Manage_Facebook_Account):
        super().setupUi(Manage_Facebook_Account)
        result,data =login()
        if result.is_ok:
            pass
        else:
           self.label_result_api.setText(result.msg+": "+str(data))
           return
        
        result,data = get_list_facebook_account()
        self.list_item = []
        
        if result.is_ok:
            self.list_account = data
            for account in self.list_account:
                self.add_item(data=account)
            data = "Ok"
        else:
            self.list_account = []
            
        self.label_result_api.setText(result.msg+": "+str(data))
        
            
    def add_item(self,data:dict):
        item = Ui_Facebook_Item_Over()
        widget_item = QWidget(self.scrollArea_list_facebook_account)
        item.setupUi(widget_item)
        item.set_data(data = data)
        self.verticalLayout_list_facebook_account.addWidget(widget_item)
        self.list_item.append(item)