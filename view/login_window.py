from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

from view.main_window import MainWindow

from model.queries_login import LoginQuery


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        loadUi("ui/login_window.ui", self)
        self.show()
        
        self.queries = LoginQuery()
        
        self.btn_login.clicked.connect(self.validar_credenciales)
    
    def validar_credenciales(self):
        usuario = self.txt_user.text()
        password = self.txt_password.text()
        
        if self.queries.validar_credenciales(usuario, password):
            self.load_main_window(usuario)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Credenciales Incorrectas")
            msg.setText("El usuario o la contraseña son incorrectos.")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.exec_()
        
    def load_main_window(self, admin):
        self.main_window = MainWindow(admin)
        self.main_window.show()
        self.hide()
