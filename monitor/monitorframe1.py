from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from ui.mm1 import Ui_dialog
from monitor.video import Video
from recorder.recordframe1 import RecordDialog1

class MonitorDialog1(QDialog):
    def __init__(self,parent_window):
        super().__init__()
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        self.parent_window = parent_window
        self.th1 = Video('data/vd1.mp4')
        self.th1.send.connect(self.showimg)
        self.th1.start()



    def showimg(self, h, w, c, b, th_id,num,pnum,cartype):
        imgae = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(imgae)
        # 自动缩放
        width = self.ui.video1.width()
        height = self.ui.video1.height()
        scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
        self.ui.video1.setPixmap(scale_pix)
        # str(num) 类型转换
        self.ui.carnum1.setText(str(num))
        self.ui.carnum2.setText(str(pnum))
        self.ui.label_5.setText(str(cartype))

    def check_button_clicked(self):
        self.recordframe = RecordDialog1(self)
        self.recordframe.show()
        self.close()

    def back_to(self):
        self.close()
        self.parent_window.show()
