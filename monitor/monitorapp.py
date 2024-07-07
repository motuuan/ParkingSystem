from PyQt5.QtWidgets import QApplication
from monitor.firstframe import FirstDialog
import sys


class MonitorApp(QApplication):
    def __init__(self):
        super(MonitorApp, self).__init__(sys.argv)
        self.dialog = FirstDialog()
        self.dialog.show()