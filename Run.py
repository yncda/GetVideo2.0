from PyQt5 import QtWidgets
# from UI import Ui_Dialog
from mainui import Ui_Dialog
import sys
import threading


class mywindow(QtWidgets.QDialog, Ui_Dialog):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)


def run():
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())

def cmd():
    a = Ui_Dialog()
    a.callcmd()

if __name__=="__main__":
    first_thread = threading.Thread(target=run)
    second_thread = threading.Thread(target=cmd)
    first_thread.start()
    second_thread.start()

