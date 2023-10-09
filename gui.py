from UI.Login import Ui_Form
from UI.Passwords import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget

USER = ('user', 'password')


class LoginPage(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.l_mail.hide()
        self.le_mail.hide()
        self.l_message.hide()
        self.bt_cancel.hide()
        self.bt_signup.pressed.connect(self.debug_sign)
        self.bt_login.pressed.connect(self.debug_log)
        self.bt_cancel.pressed.connect(self.debug_cancel)

    def debug_sign(self):
        self.l_mail.show()
        self.le_mail.show()
        self.bt_cancel.show()
        self.bt_login.hide()
        self.l_message.hide()

    def debug_log(self):
        ...

    def debug_cancel(self):
        self.bt_cancel.hide()
        self.bt_login.show()
        self.le_mail.hide()
        self.l_mail.hide()


class Passwords(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.login_page = LoginPage()
        self.login_page.bt_login.pressed.connect(self.login_check)
        self.login_page.show()


    def login_check(self):
        typed_username = self.login_page.le_username.text()
        typed_password = self.login_page.le_password.text()
        if typed_username == USER[0] and typed_password == USER[1]:
            self.login_page.hide()
            self.show()
        else:
            self.login_page.le_password.setText('')
            self.login_page.le_username.setText('')
            self.login_page.l_message.show()

