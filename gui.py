from UI.Login import Ui_Form
from UI.Passwords import Ui_MainWindow
from UI.Item import Ui_Form as Ui_Item
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

USER = ('1', '1')


class LoginPage(QWidget, Ui_Form):                                      # LOGIN PAGE

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
        widget.bt_editsave.pressed.connect(lambda: self.save_edit(widget))
        widget.bt_itemdelete.pressed.connect(lambda: self.delete_item(widget))
        self.model.appendRow(widget.item)
        self.listView_passwords.setIndexWidget(widget.item.index(), widget)

    def save_edit(self, widget: Item):
        site = widget.le_editsite.text()
        username = widget.le_edituser.text()
        password = widget.le_editpassword.text()
        old_site = widget.group_sitename.title()
        old_username = widget.l_itemuser.text()
        old_password = widget.l_itempassword.text()
        if widget.new:
            widget.new = False
            # add to database
            ...
        else:

            # update database
            ...

        widget.l_itemuser.setText(username)
        widget.l_itempassword.setText(password)
        widget.group_sitename.setTitle(site)
        widget.change_site(0)


    def delete_item(self, widget):
        self.model.removeRow(widget.item.row())
        # delete from database








