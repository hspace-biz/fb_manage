
from main_utils import api, define
from PyQt6.QtWidgets import QMainWindow, QWidget
from ui_code_raw.Import_Proxy import Ui_ImportProxy

from ui_code_over.Config_Window_Over import Ui_Config_Over
from ui_code_over.Proxy_Item_Over import Ui_Proxy_Item_Over


class ImportProxy_Over(Ui_ImportProxy):
    def setupUi(self, ImportProxy):
        super().setupUi(ImportProxy=ImportProxy)
        self.actionServer.triggered[bool].connect(self.open_config)
        self.actionProxy_manager.triggered[bool].connect(
            self.open_Manage_Proxy)
        self.pushButton_Read.clicked[bool].connect(self.read)
        self.list_item = []

    def set_Manage_Proxy(self, window):
        self.Manage_Proxy = window

    def open_Manage_Proxy(self):
        self.manager_Proxy_Window = QMainWindow()
        self.Manage_Proxy.setupUi(self.manager_Proxy_Window)
        self.manager_Proxy_Window.show()

    def open_config(self):
        self.ui_Config_Over = QWidget()
        self._ui_Config_Over = Ui_Config_Over()
        self._ui_Config_Over.setupUi(self.ui_Config_Over)
        self.ui_Config_Over.show()

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
