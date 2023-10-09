from UI.Login import Ui_Form
from UI.Passwords import Ui_MainWindow
from UI.Item import Ui_Form as Ui_Item
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

USER = ('1', '1')


class LoginPage(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.l_mail.hide()
        self.le_mail.hide()
        self.bt_cancel.hide()
        self.bt_signup.pressed.connect(self.style_sign)
        self.bt_cancel.pressed.connect(self.style_cancel)

    def style_sign(self):
        self.l_mail.show()
        self.le_mail.show()
        self.bt_cancel.show()
        self.bt_login.hide()
        self.label.setText("Master Safe")
        self.label.setStyleSheet("color: black;")

    def style_cancel(self):
        self.bt_cancel.hide()
        self.bt_login.show()
        self.le_mail.hide()
        self.l_mail.hide()


class Passwords(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = QStandardItemModel()
        self.listView_passwords.setModel(self.model)
        self.listView_passwords.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.bt_add.pressed.connect(self.add_item)


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
            self.login_page.label.setText('Incorrect!')
            self.login_page.label.setStyleSheet('color: red;')


    def add_item(self):
        widget = Item()
        self.model.appendRow(widget.item)
        self.listView_passwords.setIndexWidget(widget.item.index(), widget)



class Item(QWidget, Ui_Item):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.item = QStandardItem()
        self.item.setSelectable(False)
        self.new = True

