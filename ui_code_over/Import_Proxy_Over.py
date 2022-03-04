from distutils import text_file
from http.client import IM_USED
from ui_code_raw.Import_Proxy import Ui_ImportProxy
from PyQt6.QtWidgets import QWidget, QGroupBox, QVBoxLayout
from main_utils import api, define
from main_utils.proxy import Proxy
from ui_code_over.Proxy_Item_Over import Ui_Proxy_Item_Over


class ImportProxy_Over(Ui_ImportProxy):
    def setupUi(self, ImportProxy):
        super().setupUi(ImportProxy=ImportProxy)
        self.pushButton_Read.clicked[bool].connect(self.read)

        self.list_item = []

    def add_proxy_item(self,
                       proxy_str: str = None,
                       proxy_ip: str = None, proxy_port: str = None,
                       proxy_username: str = None, proxy_password: str = None
                       ):
        item = Ui_Proxy_Item_Over(proxy_str, 
                                  proxy_ip=proxy_ip, proxy_port=proxy_port,
                                  proxy_username=proxy_username, proxy_password=proxy_password
        )
        widget_item = QWidget(self.scrollAreaWidgetContents_list_proxy)
        item.setupUi(ImportProxy=widget_item)
        self.verticalLayout_list_proxy.addWidget(widget_item)

    def read(self):
        raw_text = self.plainTextEdit_Import_Proxy.toPlainText().replace(" ", "")
        lines = raw_text.split("\n")
        for line in lines:
            self.add_proxy_item(line)
            
