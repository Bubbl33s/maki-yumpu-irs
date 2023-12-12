from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

from view.main_window import MainWindow


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        loadUi("ui/login_window.ui", self)
        self.show()
        
        self.btn_login.clicked.connect(self.load_main_window)
        
        
    def load_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.hide()
