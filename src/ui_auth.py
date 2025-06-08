# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_auth.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
class Ui_AuthWindow(object):
    def setupUi(self, AuthWindow):
        if not AuthWindow.objectName():
            AuthWindow.setObjectName(u"AuthWindow")
        AuthWindow.resize(944, 602)
        self.centralwidget = QWidget(AuthWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(830, 10, 100, 44))
        self.widget.setMinimumSize(QSize(100, 0))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 7, 0)
        self.wrapBtn = QPushButton(self.widget)
        self.wrapBtn.setObjectName(u"wrapBtn")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.wrapBtn.setIcon(icon)
        self.wrapBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.wrapBtn)

        self.closeBtn = QPushButton(self.widget)
        self.closeBtn.setObjectName(u"closeBtn")
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon1)
        self.closeBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.closeBtn)

        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(394, 44, 156, 62))
        self.header.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u"../Qss/icons/logo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_4 = QLabel(self.header)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setPointSize(25)
        self.label_4.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(384, 106, 175, 284))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(175, 0))
        self.widget_2.setFocusPolicy(Qt.NoFocus)
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 120, 0, 0)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignTop)

        self.loginLineEdit = QLineEdit(self.widget_2)
        self.loginLineEdit.setObjectName(u"loginLineEdit")
        self.loginLineEdit.setMinimumSize(QSize(0, 25))

        self.verticalLayout_2.addWidget(self.loginLineEdit, 0, Qt.AlignTop)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignTop)

        self.passwordLineEdit = QLineEdit(self.widget_2)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setMinimumSize(QSize(0, 25))

        self.verticalLayout_2.addWidget(self.passwordLineEdit, 0, Qt.AlignTop)

        self.loginBtn = QPushButton(self.widget_2)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(0, 25))

        self.verticalLayout_2.addWidget(self.loginBtn, 0, Qt.AlignTop)

        self.passwordRecoverLbl = QLabel(self.widget_2)
        self.passwordRecoverLbl.setObjectName(u"passwordRecoverLbl")
        font1 = QFont()
        font1.setUnderline(True)
        self.passwordRecoverLbl.setFont(font1)

        self.verticalLayout_2.addWidget(self.passwordRecoverLbl, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.passwordRecoverLbl.raise_()
        self.loginLineEdit.raise_()
        self.passwordLineEdit.raise_()
        self.loginBtn.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        AuthWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AuthWindow)

        QMetaObject.connectSlotsByName(AuthWindow)
    # setupUi

    def retranslateUi(self, AuthWindow):
        AuthWindow.setWindowTitle(QCoreApplication.translate("AuthWindow", u"Authorization", None))
        self.wrapBtn.setText("")
        self.closeBtn.setText("")
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("AuthWindow", u"HiHire", None))
        self.label_2.setText(QCoreApplication.translate("AuthWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_3.setText(QCoreApplication.translate("AuthWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.loginBtn.setText(QCoreApplication.translate("AuthWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.passwordRecoverLbl.setText(QCoreApplication.translate("AuthWindow", u"\u0417\u0430\u0431\u044b\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c?", None))
    # retranslateUi

