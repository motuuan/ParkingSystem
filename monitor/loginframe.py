from PyQt5 import QtWidgets
from ui.lm import Ui_Dialog
from monitor.mainmenu import MenuDialog

class LoginDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self.login_button_clicked)

        self.ui.findButton.clicked.connect(self.find_button_clicked)

    def login_button_clicked(self):
        username = self.ui.lineEdit1.text()
        password = self.ui.lineEdit2.text()

        # 验证用户名和密码
        if username == "admin" and password == "123456":
            self.menuframe = MenuDialog()
            self.menuframe.show()
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "登录失败", "用户名或密码错误！")

    def  find_button_clicked(self):
        QtWidgets.QMessageBox.information(self, "找回密码", "用户名：admin   密码：123456")




