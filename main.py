import sys
from PyQt5.QtWidgets import QApplication

from view.login_window import LoginWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())
