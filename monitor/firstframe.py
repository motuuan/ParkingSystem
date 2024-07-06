from PyQt5 import QtWidgets, QtCore
from ui.fm import Ui_Dialog
from monitor.loginframe import LoginDialog


class FirstDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


    def on_resize(self, event):
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                            transformMode=QtCore.Qt.SmoothTransformation))


    def goin(self):
        self.loginframe = LoginDialog()
        self.loginframe.show()
        self.close()



