# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 150)
        Form.setMinimumSize(QSize(600, 150))
        Form.setMaximumSize(QSize(600, 150))
        Form.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_2 = QVBoxLayout(self.page_5)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.group_sitename = QGroupBox(self.page_5)
        self.group_sitename.setObjectName(u"group_sitename")
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        self.group_sitename.setFont(font)
        self.group_sitename.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.group_sitename)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.group_sitename)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.l_itemuser = QLabel(self.frame_4)
        self.l_itemuser.setObjectName(u"l_itemuser")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.l_itemuser.setFont(font1)
        self.l_itemuser.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.l_itemuser)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.group_sitename)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.l_itempassword = QLabel(self.frame_5)
        self.l_itempassword.setObjectName(u"l_itempassword")
        self.l_itempassword.setFont(font1)
        self.l_itempassword.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.l_itempassword)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.group_sitename)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(450, 0, 0, 0)
        self.bt_itemedit = QPushButton(self.frame_6)
        self.bt_itemedit.setObjectName(u"bt_itemedit")
        self.bt_itemedit.setMaximumSize(QSize(50, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setItalic(False)
        self.bt_itemedit.setFont(font2)

        self.horizontalLayout_6.addWidget(self.bt_itemedit)

        self.bt_itemdelete = QPushButton(self.frame_6)
        self.bt_itemdelete.setObjectName(u"bt_itemdelete")
        self.bt_itemdelete.setMaximumSize(QSize(50, 16777215))
        self.bt_itemdelete.setFont(font2)

        self.horizontalLayout_6.addWidget(self.bt_itemdelete)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.group_sitename)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout = QVBoxLayout(self.page_6)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.frame = QFrame(self.page_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 3, -1, 3)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label)

        self.le_editsite = QLineEdit(self.frame)
        self.le_editsite.setObjectName(u"le_editsite")
        self.le_editsite.setMaximumSize(QSize(400, 35))
        self.le_editsite.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.le_editsite)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 3, -1, 3)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.le_edituser = QLineEdit(self.frame_2)
        self.le_edituser.setObjectName(u"le_edituser")
        self.le_edituser.setMaximumSize(QSize(400, 35))
        self.le_edituser.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.le_edituser)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 3, -1, 3)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.le_editpassword = QLineEdit(self.frame_3)
        self.le_editpassword.setObjectName(u"le_editpassword")
        self.le_editpassword.setMaximumSize(QSize(400, 35))
        self.le_editpassword.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.le_editpassword)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_7 = QFrame(self.page_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(400, 0, 0, 0)
        self.bt_editsave = QPushButton(self.frame_7)
        self.bt_editsave.setObjectName(u"bt_editsave")
        self.bt_editsave.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.bt_editsave)

        self.bt_editcancel = QPushButton(self.frame_7)
        self.bt_editcancel.setObjectName(u"bt_editcancel")
        self.bt_editcancel.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.bt_editcancel)


        self.verticalLayout.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_6)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.group_sitename.setTitle(QCoreApplication.translate("Form", u"SiteName", None))
        self.l_itemuser.setText(QCoreApplication.translate("Form", u"Username", None))
        self.l_itempassword.setText(QCoreApplication.translate("Form", u"Password", None))
        self.bt_itemedit.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.bt_itemdelete.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.label.setText(QCoreApplication.translate("Form", u"Site Name", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Password", None))
        self.bt_editsave.setText(QCoreApplication.translate("Form", u"Save", None))
        self.bt_editcancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

