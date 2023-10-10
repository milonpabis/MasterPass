# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
    QLabel, QListView, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.centralwidget.setMaximumSize(QSize(800, 600))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 80))
        self.frame.setMaximumSize(QSize(800, 80))
        self.frame.setStyleSheet(u"background-color: rgb(192, 255, 213);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.l_hello = QLabel(self.frame)
        self.l_hello.setObjectName(u"l_hello")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.l_hello.setFont(font)
        self.l_hello.setStyleSheet(u"color: rgb(80, 106, 89);")

        self.horizontalLayout.addWidget(self.l_hello)

        self.bt_add = QPushButton(self.frame)
        self.bt_add.setObjectName(u"bt_add")
        self.bt_add.setMinimumSize(QSize(60, 60))
        self.bt_add.setMaximumSize(QSize(60, 60))
        font1 = QFont()
        font1.setFamilies([u"Microsoft JhengHei"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.bt_add.setFont(font1)
        self.bt_add.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(192, 255, 213);\n"
"border: 1px solid rgb(80, 106, 89);\n"
"color: rgb(80, 106, 89);")

        self.horizontalLayout.addWidget(self.bt_add)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(800, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(174, 231, 193);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.groupBox.setFont(font2)
        self.groupBox.setStyleSheet(u"color: rgb(80, 106, 89);")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listView_passwords = QListView(self.groupBox)
        self.listView_passwords.setObjectName(u"listView_passwords")
        self.listView_passwords.setStyleSheet(u"background-color: rgb(192, 255, 213);")
        self.listView_passwords.setSpacing(70)
        self.listView_passwords.setUniformItemSizes(True)
        self.listView_passwords.setBatchSize(100)

        self.verticalLayout_2.addWidget(self.listView_passwords)


        self.horizontalLayout_2.addWidget(self.groupBox)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.l_hello.setText(QCoreApplication.translate("MainWindow", u"Hello, Username", None))
        self.bt_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Your Passwords", None))
    # retranslateUi

