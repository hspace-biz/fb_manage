from PyQt6 import QtWidgets
from ui_code_over.Manage_Facebook_Account import Ui_Manage_Facebook_Account_Over
from ui_code_over.Import_Cookies_Over import Import_Cookies_Over
import sys

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_Manage_Facebook_Account_Over()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()