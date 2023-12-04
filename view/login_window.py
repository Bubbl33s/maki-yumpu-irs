from PyQt5 import uic, QtWidgets


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        uic.loadUi("ui/login_window.ui", self)
        self.show()
