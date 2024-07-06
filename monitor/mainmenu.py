from PyQt5 import QtWidgets
from ui.me import Ui_Dialog
from monitor.monitorframe1 import MonitorDialog1
from monitor.monitorframe2 import MonitorDialog2
from recorder.recordframe1 import RecordDialog1
from recorder.recordframe2 import RecordDialog2


class MenuDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


    def goin1(self):
        self.mf1 = MonitorDialog1(self)
        self.mf1.show()
        self.close()

    def goin2(self):
        self.mf2 = MonitorDialog2(self)
        self.mf2.show()
        self.close()
    def goin3(self):
        self.mf3 = RecordDialog1(self)
        self.mf3.show()
        self.close()
    def goin4(self):
        self.mf4 = RecordDialog2(self)
        self.mf4.show()
        self.close()


