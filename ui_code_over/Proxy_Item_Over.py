from distutils import text_file
from http.client import IM_USED

from Item.Cookie_Item import Cookie_Import_Item
from main_utils import api, define
from main_utils.proxy import Proxy
from PyQt6.QtWidgets import QGroupBox, QVBoxLayout, QWidget
from ui_code_raw.Proxy_Item import Ui_Proxy_Item


class Ui_Proxy_Item_Over(Ui_Proxy_Item):
    def __init__(self,
                 proxy_str: str = None,
                 proxy_ip: str = None, proxy_port: str = None,
                 proxy_username: str = None, proxy_password: str = None
                 ):
        self.proxy = Proxy(proxy_str=proxy_str, proxy_ip=proxy_ip, proxy_port=proxy_port,
                           proxy_username=proxy_username, proxy_password=proxy_password)

    def setupUi(self, ImportProxy):
        super().setupUi(ImportProxy)
        self.label_ip.setText(self.proxy.proxy_ip)
        self.label_port.setText(self.proxy.proxy_port)
        self.label_username.setText(self.proxy.proxy_username)
        self.label_password.setText(self.proxy.proxy_password)
