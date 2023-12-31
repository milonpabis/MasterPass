# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 450)
        Form.setMinimumSize(QSize(700, 450))
        Form.setMaximumSize(QSize(700, 450))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 80))
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setStyleSheet(u"background-color: rgb(192, 255, 213);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe Print"])
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(80, 106, 89);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(174, 231, 193);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(147, 70, 250, 70)
        self.l_mail = QLabel(self.frame_2)
        self.l_mail.setObjectName(u"l_mail")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.l_mail.setFont(font1)
        self.l_mail.setStyleSheet(u"color: rgb(80, 106, 89);\n"
"background-color: rgb(174, 231, 193);\n"
"border-radius: 10px;\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.l_mail, 1, 0, 1, 1)

        self.le_username = QLineEdit(self.frame_2)
        self.le_username.setObjectName(u"le_username")
        self.le_username.setMinimumSize(QSize(200, 30))
        self.le_username.setMaximumSize(QSize(200, 30))
        self.le_username.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.le_username.setFont(font2)
        self.le_username.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(80, 106, 89);")

        self.gridLayout.addWidget(self.le_username, 0, 2, 1, 1)

        self.l_username = QLabel(self.frame_2)
        self.l_username.setObjectName(u"l_username")
        self.l_username.setMinimumSize(QSize(100, 0))
        self.l_username.setMaximumSize(QSize(100, 16777215))
        self.l_username.setFont(font1)
        self.l_username.setStyleSheet(u"color: rgb(80, 106, 89);\n"
"background-color: rgb(192, 255, 213);\n"
"border-radius: 10px;\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.l_username, 0, 0, 1, 1)

        self.l_password = QLabel(self.frame_2)
        self.l_password.setObjectName(u"l_password")
        self.l_password.setMinimumSize(QSize(100, 0))
        self.l_password.setMaximumSize(QSize(100, 16777215))
        self.l_password.setFont(font1)
        self.l_password.setStyleSheet(u"color: rgb(80, 106, 89);\n"
"background-color: rgb(153, 203, 170);\n"
"border-radius: 10px;\n"
"border: 1px solid black;")

        self.gridLayout.addWidget(self.l_password, 2, 0, 1, 1)

        self.le_mail = QLineEdit(self.frame_2)
        self.le_mail.setObjectName(u"le_mail")
        self.le_mail.setMinimumSize(QSize(200, 30))
        self.le_mail.setMaximumSize(QSize(200, 30))
        self.le_mail.setFont(font2)
        self.le_mail.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(80, 106, 89);")

        self.gridLayout.addWidget(self.le_mail, 1, 2, 1, 1)

        self.le_password = QLineEdit(self.frame_2)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setMinimumSize(QSize(200, 30))
        self.le_password.setMaximumSize(QSize(200, 30))
        self.le_password.setSizeIncrement(QSize(0, 0))
        self.le_password.setFont(font2)
        self.le_password.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(80, 106, 89);")

        self.gridLayout.addWidget(self.le_password, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 100))
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setStyleSheet(u"background-color: rgb(153, 203, 170);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(240, -1, 240, 50)
        self.bt_cancel = QPushButton(self.frame_3)
        self.bt_cancel.setObjectName(u"bt_cancel")
        self.bt_cancel.setMaximumSize(QSize(100, 35))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.bt_cancel.setFont(font3)
        self.bt_cancel.setStyleSheet(u"QPushButton {color: rgb(80, 106, 89);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:hover {color: rgb(80, 106, 89);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:pressed {color: rgb(80, 106, 89);\n"
"background-color: rgb(192, 255, 213);\n"
"border-radius: 10px;\n"
"border: 1px solid black; }")

        self.horizontalLayout_2.addWidget(self.bt_cancel)

        self.bt_login = QPushButton(self.frame_3)
        self.bt_login.setObjectName(u"bt_login")
        self.bt_login.setMaximumSize(QSize(100, 35))
        self.bt_login.setFont(font3)
        self.bt_login.setStyleSheet(u"QPushButton {color: rgb(80, 106, 89);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:hover {color: rgb(80, 106, 89);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:pressed {color: rgb(80, 106, 89);\n"
"background-color: rgb(192, 255, 213);\n"
"border-radius: 10px;\n"
"border: 1px solid black; }")

        self.horizontalLayout_2.addWidget(self.bt_login)

        self.bt_signup = QPushButton(self.frame_3)
        self.bt_signup.setObjectName(u"bt_signup")
        self.bt_signup.setMaximumSize(QSize(100, 35))
        self.bt_signup.setFont(font3)
        self.bt_signup.setStyleSheet(u"QPushButton {color: rgb(80, 106, 89);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:hover {color: rgb(80, 106, 89);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 1px solid black; }\n"
"\n"
"QPushButton:pressed {color: rgb(80, 106, 89);\n"
"background-color: rgb(192, 255, 213);\n"
"border-radius: 10px;\n"
"border: 1px solid black; }")

        self.horizontalLayout_2.addWidget(self.bt_signup)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Master Safe", None))
        self.l_mail.setText(QCoreApplication.translate("Form", u"E-mail", None))
        self.l_username.setText(QCoreApplication.translate("Form", u"Username", None))
        self.l_password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.bt_cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.bt_login.setText(QCoreApplication.translate("Form", u"Log In", None))
        self.bt_signup.setText(QCoreApplication.translate("Form", u"Sign Up", None))
    # retranslateUi

