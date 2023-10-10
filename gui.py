import sqlite3

from UI.Login import Ui_Form
from UI.Passwords import Ui_MainWindow
from UI.Item import Ui_Form as Ui_Item
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLineEdit
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from db import DataBaseControl

USER = ('1', '1')


class LoginPage(QWidget, Ui_Form):                                      # LOGIN PAGE

    def __init__(self):
        super().__init__()
        self.register_mode = False
        self.setupUi(self)
        self.setWindowTitle("MasterSafe")
        self.l_mail.hide()
        self.le_mail.hide()
        self.bt_cancel.hide()
        self.bt_signup.pressed.connect(self.register_user_mode)
        self.bt_cancel.pressed.connect(self.login_user_mode)
        self.le_password.setEchoMode(QLineEdit.EchoMode.Password)



    def register_user_mode(self):
        self.register_mode = True
        self.style_register()
        self.le_password.setEchoMode(QLineEdit.EchoMode.Normal)

    def login_user_mode(self):
        self.register_mode = False
        self.le_mail.setText('')
        self.style_login()
        self.le_password.setEchoMode(QLineEdit.EchoMode.Password)


    def style_register(self):
        self.l_mail.show()
        self.le_mail.show()
        self.bt_cancel.show()
        self.bt_login.hide()
        self.label.setText("Master Safe")
        self.label.setStyleSheet("color: rgb(80, 106, 89);")
        self.le_password.setText("")
        self.le_username.setText("")

    def style_login(self):
        self.label.setText("Master Safe")
        self.label.setStyleSheet("color: rgb(80, 106, 89);")
        self.bt_cancel.hide()
        self.bt_login.show()
        self.le_mail.hide()
        self.l_mail.hide()
        self.le_username.setText("")
        self.le_password.setText("")



class Item(QWidget, Ui_Item):                                               # ITEM

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.item = QStandardItem()
        self.item.setSelectable(False)
        self.new = True
        self.bt_itemedit.pressed.connect(self.edit_start)
        self.bt_editcancel.pressed.connect(self.edit_cancel)

    def change_site(self, idx):
        self.stackedWidget.setCurrentIndex(idx)

    def edit_cancel(self):
        if self.new:
            self.bt_itemdelete.click()
        else:
            self.change_site(0)

    def edit_start(self):
        self.le_editsite.setText(self.group_sitename.title())
        self.le_edituser.setText(self.l_itemuser.text())
        self.le_editpassword.setText(self.l_itempassword.text())
        self.change_site(1)




class Passwords(QMainWindow, Ui_MainWindow):                                    # MAINPAGE

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("MasterSafe")
        self.current_user = None
        self.db = DataBaseControl()
        self.model = QStandardItemModel()
        self.listView_passwords.setModel(self.model)
        self.listView_passwords.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.bt_add.pressed.connect(self.add_item)


        self.login_page = LoginPage()
        self.login_page.bt_login.pressed.connect(self.login_check)
        self.login_page.bt_signup.pressed.connect(self.register_check)
        self.login_page.show()


    def register_check(self):
        if not self.login_page.register_mode:
            self.login_page.register_user_mode()
        else:
            # validate and if so -> database and login automatically
            email = self.login_page.le_mail.text()
            username = self.login_page.le_username.text()
            password = self.login_page.le_password.text()
            if username and password and email:
                try:
                    self.db.add_user(email, username, password)
                    self.current_user = username
                    self.load_user_data()
                    self.login_page.hide()
                    self.show()
                except sqlite3.IntegrityError:
                    self.login_page.label.setText("User exists!")
                    self.login_page.label.setStyleSheet("color: red;")



    def login_check(self):
        login_data = self.db.return_users()
        username = self.login_page.le_username.text()
        password = self.login_page.le_password.text()
        if (username, password) in login_data:
            self.current_user = username
            self.load_user_data()
            self.login_page.hide()
            self.show()
        else:
            self.login_page.le_password.setText('')
            self.login_page.le_username.setText('')
            self.login_page.label.setText('Incorrect!')
            self.login_page.label.setStyleSheet('color: red;')

    def load_user_data(self):
        data = self.db.return_data(self.current_user)
        self.l_hello.setText(f"Hello, {self.current_user}")
        for site, username, password in data:
            self.add_item(site, username, password)
        #print(data)

    def add_item(self, *args):
        widget = Item()
        widget.bt_editsave.pressed.connect(lambda: self.save_edit(widget))
        widget.bt_itemdelete.pressed.connect(lambda: self.delete_item(widget))
        self.model.appendRow(widget.item)
        self.listView_passwords.setIndexWidget(widget.item.index(), widget)
        if args:
            widget.new = False
            widget.group_sitename.setTitle(args[0])
            widget.l_itemuser.setText(args[1])
            widget.l_itempassword.setText(args[2])
            widget.stackedWidget.setCurrentIndex(0)
        else:
            self.listView_passwords.scrollToBottom()

    def save_edit(self, widget: Item):
        site = widget.le_editsite.text()
        login = widget.le_edituser.text()
        password = widget.le_editpassword.text()
        old_site = widget.group_sitename.title()
        old_login = widget.l_itemuser.text()
        old_password = widget.l_itempassword.text()
        if widget.new:
            print("new")
            widget.new = False
            # add to database

            self.db.add_password(self.current_user, site, login, password)
        else:
            print("old")
            # update database
            self.db.update_password(self.current_user, site, login, password, old_site, old_login, old_password)

        widget.l_itemuser.setText(login)
        widget.l_itempassword.setText(password)
        widget.group_sitename.setTitle(site)
        widget.change_site(0)


    def delete_item(self, widget):
        self.model.removeRow(widget.item.row())
        site = widget.group_sitename.title()
        login = widget.l_itemuser.text()
        password = widget.l_itempassword.text()
        self.db.delete_password(self.current_user, site, login, password)








