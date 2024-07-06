from PyQt5.QtWidgets import QDialog
from ui.rm2 import Ui_Dialog

class RecordDialog2(QDialog):
    # ... 其他代码 ...
    def __init__(self,parent_window):
        super().__init__()
        self.ui2 = Ui_Dialog()
        self.ui2.setupUi(self)
        self.parent_window = parent_window
        self.showtxt('data/RecordOut.txt')

    def showtxt(self, file_path):
        try:
            with open(file_path, 'r') as file:
                text = file.read()
                self.ui2.plainTextEdit.setPlainText(text)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def back_to(self):
        self.close()
        self.parent_window.show()
