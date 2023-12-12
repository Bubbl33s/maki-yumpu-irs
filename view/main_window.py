from PyQt5 import uic, QtWidgets
from PyQt5.uic import loadUi

from controller.db_conn import Database
from controller.generar_pedido_tab import GenerarPedidoTab


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi("ui/main_window.ui", self)
        self.show()
        
        self.db = Database()
        
        self.btn_logout.clicked.connect(self.logout)
        self.tab_gp = GenerarPedidoTab(self)
        
    def logout(self):
        from view.login_window import LoginWindow
        
        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()
