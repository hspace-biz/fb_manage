
from main_utils import api, define, qtable_utils
from main_utils.api import insert_cookie
from PyQt6.QtWidgets import QMainWindow, QWidget
from ui_code_raw.Import_Proxy import Ui_ImportProxy


class Ui_ImportProxy_over(Ui_ImportProxy):
    def setupUi(self, ImportProxy):
        super().setupUi(ImportProxy)
        self.pushButton_Read.clicked[bool].connect(self.read_input)
        self.pushButton_Insert.clicked[bool].connect(self.insert_to_db)
        self.api_data = []

    def insert_to_db(self):
        output_api = ""
        for item in self.api_data:
            result = api.insert_proxy(proxy=item, is_update=True)
            if result == define.ResultBase.PERMISSION_DENIED:
                output_api = "This account has no insert permission."
                return
            if result == define.ResultBase.OK:
                output_api += f"updated - {item.get('ip')}"+"\n"
            if result == define.ResultBase.ALREADY_EXISTS:
                output_api += f"exists - {item.get('ip')}"+"\n"

        self.plainTextEdit_result.setPlainText(output_api)

    def read_input(self):
        lines = self.plainTextEdit_Import_Proxy.toPlainText().split("\n")
        show_data = {
            "ip": [],
            "port": [],
            "user_name": [],
            "password": []
        }
        count = 0
        self.api_data = []
        for line in lines:
            line = line.split(":")
            if len(line) != 4:
                continue
            count += 1
            show_data["ip"].append(line[0])
            show_data["port"].append(line[1])
            show_data["user_name"].append(line[2])
            show_data["password"].append(line[3])
            self.api_data.append({
                "ip": line[0],
                "port": line[1],
                "user_name": line[2],
                "password": line[3]
            })
        self.label_count_proxy.setText(f"{count}")

        qtable_utils.setData(self.tableWidget_list_account, show_data)
