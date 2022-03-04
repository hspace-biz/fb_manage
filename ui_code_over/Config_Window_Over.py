from ui_code_raw.Config_Window import Ui_Config
import requests
from main_utils import file

class Ui_Config_Over(Ui_Config):
    def setupUi(self, Config):
        super().setupUi(Config=Config)
        data = file.read_data_configs()
        if len(data.keys())>0:
            self.lineEdit_server.setText(data.get("ip"))
            self.lineEdit_server_port.setText(data.get("port"))
            self.lineEdit_User_Name.setText(data.get("username"))
            self.lineEdit_User_Pass.setText(data.get("password"))

        self.token = None
        self.s_key = None
        self.pushButton_Check.clicked[bool].connect(lambda x:self.check_connection())
        
    def check_connection(self):
        self.ip = self.lineEdit_server.text()
        self.port = self.lineEdit_server_port.text()
        self.user_name = self.lineEdit_User_Name.text()
        self.password = self.lineEdit_User_Pass.text()
        self.token = None
        self.s_key = None
        self.label_result.setText("Checking....")
        data = {
        "email": self.user_name,
        "password": self.password
        }
        try:
            _ip = self.ip.split(".")
            for __ip in _ip:
                __ip = int(__ip)
                if __ip<0 or __ip>255:
                    self.label_result.setText(f"0<={__ip}<=255")
                    self.set_color_label(self.label_result,250,0,0)
                    return
        except Exception as ex:
            self.label_result.setText("Error: {ex}")
            self.set_color_label(self.label_result,250,0,0)
            return
        self.url = f"http://{self.ip}:{self.port}"
        try:
            res = requests.get(url=self.url,timeout=10)
        except requests.exceptions.ConnectTimeout as ex:
            self.label_result.setText(f"Server timeout")
            self.set_color_label(self.label_result,250,0,0)
            return True
        except Exception as ex:
            self.label_result.setText(ex)
            self.set_color_label(self.label_result,250,0,0)
            return True
        
        res = requests.post(url=self.url+"/login",json=data)
        if res.status_code!=200:
            self.label_result.setText(f"Login failed.")
            self.set_color_label(self.label_result,250,0,0)
            return True
        try:
            res = res.json()
            print(res)
            if res.get("secret_key") is None:
                self.label_result.setText(f"secret_key not found")
                self.set_color_label(self.label_result,250,0,0)
                return True
            if res.get("token") is None:
                self.label_result.setText(f"token not found")
                self.set_color_label(self.label_result,250,0,0)
                return True
            if res.get("token").get("token_type") is None:
                self.label_result.setText(f"token_type not found")
                self.set_color_label(self.label_result,250,0,0)
                return True
            if res.get("token").get("access_token") is None:
                self.label_result.setText(f"access_token not found")
                self.set_color_label(self.label_result,250,0,0)
                return True
            if res.get("code") is None:
                self.label_result.setText(f"ma_tv not found")
                self.set_color_label(self.label_result,250,0,0)
                return True
            
            self.s_key = res.get("secret_key")
            self.token = res.get("token").get("token_type")+" "+res.get("token").get("access_token")
            self.code = res.get("code")
            self.label_result.setText("Ok")
            self.set_color_label(self.label_result,0,100,0)
        except Exception as ex:
            self.set_color_label(self.label_result,250,0,0)
            self.label_result.setText(ex)
            return True
        
        data = {
            "ip":self.ip,
            "port":self.port,
            "username":self.user_name,
            "password":self.password,
            "token":self.token,
            "s_key":self.s_key,
            "code":self.code,
        }
        file.save_data_configs(data = data)
        
        
    def set_color_button(self, ob, r, g, b):
        color = QtGui.QColor(r, g, b)
        alpha = 140
        values = "{r}, {g}, {b}, {a}".format(r=color.red(),
                                             g=color.green(),
                                             b=color.blue(),
                                             a=alpha
                                             )
        ob.setStyleSheet("QPushButton { background-color: rgba("+values+"); }")
        
    def set_color_label(self, ob, r, g, b):
        color = QtGui.QColor(r, g, b)
        alpha = 140
        values = "{r}, {g}, {b}, {a}".format(r=color.red(),
                                             g=color.green(),
                                             b=color.blue(),
                                             a=alpha
                                             )
        ob.setStyleSheet("QLabel { color: rgba("+values+"); }")