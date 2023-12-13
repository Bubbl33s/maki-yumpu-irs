from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

from model.db_conn import Database
from controller.generar_pedido_tab import GenerarPedidoTab
from controller.rastrear_pedido_tab import RastrearPedidoTab


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi("ui/main_window.ui", self)
        self.show()
        
        self.db = Database()
        self.tab_gp = GenerarPedidoTab(self)
        self.tab_rp = RastrearPedidoTab(self)
        
        self.btn_logout.clicked.connect(self.logout)

        
    def logout(self):
        from view.login_window import LoginWindow
        
        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()

    def closeEvent(self, event):
        self.logout()
        event.accept()
        