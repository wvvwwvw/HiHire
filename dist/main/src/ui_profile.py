# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_profile.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
class Ui_ProfileWindow(object):
    def setupUi(self, ProfileWindow):
        if not ProfileWindow.objectName():
            ProfileWindow.setObjectName(u"ProfileWindow")
        ProfileWindow.setEnabled(True)
        ProfileWindow.resize(800, 602)
        ProfileWindow.setMinimumSize(QSize(800, 0))
        ProfileWindow.setMaximumSize(QSize(800, 16777215))
        ProfileWindow.setMouseTracking(False)
        ProfileWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(ProfileWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 602))
        self.centralwidget.setMaximumSize(QSize(800, 16777215))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.leftMenuP = QWidget(self.centralwidget)
        self.leftMenuP.setObjectName(u"leftMenuP")
        self.leftMenuP.setMinimumSize(QSize(250, 0))
        self.leftMenuP.setMaximumSize(QSize(250, 16777215))
        self.leftMenuP.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftMenuP)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.back = QWidget(self.leftMenuP)
        self.back.setObjectName(u"back")
        self.back.setMinimumSize(QSize(46, 42))
        self.verticalLayout_2 = QVBoxLayout(self.back)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 5, 0, 5)

        self.verticalLayout.addWidget(self.back, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_4 = QWidget(self.leftMenuP)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.widget_4)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 150))
        self.frame.setMaximumSize(QSize(150, 150))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.profilePic = QLabel(self.frame)
        self.profilePic.setObjectName(u"profilePic")
        self.profilePic.setMinimumSize(QSize(140, 140))
        self.profilePic.setMaximumSize(QSize(140, 140))
        self.profilePic.setScaledContents(False)

        self.verticalLayout_3.addWidget(self.profilePic, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 100))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.roleLabel = QLabel(self.widget)
        self.roleLabel.setObjectName(u"roleLabel")

        self.verticalLayout_4.addWidget(self.roleLabel, 0, Qt.AlignHCenter)

        self.organizationLabel = QLabel(self.widget)
        self.organizationLabel.setObjectName(u"organizationLabel")

        self.verticalLayout_4.addWidget(self.organizationLabel, 0, Qt.AlignHCenter)

        self.fioLabel = QLabel(self.widget)
        self.fioLabel.setObjectName(u"fioLabel")

        self.verticalLayout_4.addWidget(self.fioLabel, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.widget, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_2 = QWidget(self.leftMenuP)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(100, 30))
        self.widget_2.setMaximumSize(QSize(100, 30))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.exitBtn = QPushButton(self.widget_2)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMinimumSize(QSize(100, 30))
        self.exitBtn.setMaximumSize(QSize(100, 30))
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/log-out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtn.setIcon(icon)
        self.exitBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.exitBtn)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.leftMenuP)

        self.leftBody = QWidget(self.centralwidget)
        self.leftBody.setObjectName(u"leftBody")
        self.leftBody.setMinimumSize(QSize(0, 0))
        self.leftBody.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.leftBody)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerProfile = QWidget(self.leftBody)
        self.headerProfile.setObjectName(u"headerProfile")
        self.headerProfile.setMaximumSize(QSize(550, 16777215))
        self.headerProfile.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.headerProfile)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 0, 5)
        self.logoWidget = QWidget(self.headerProfile)
        self.logoWidget.setObjectName(u"logoWidget")
        self.logoWidget.setMinimumSize(QSize(150, 0))
        self.horizontalLayout_11 = QHBoxLayout(self.logoWidget)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.logoPic = QLabel(self.logoWidget)
        self.logoPic.setObjectName(u"logoPic")
        self.logoPic.setMaximumSize(QSize(45, 45))
        self.logoPic.setSizeIncrement(QSize(0, 0))
        self.logoPic.setPixmap(QPixmap(u"../Qss/icons/logo.png"))
        self.logoPic.setScaledContents(True)
        self.logoPic.setMargin(0)
        self.logoPic.setIndent(-1)

        self.horizontalLayout_11.addWidget(self.logoPic, 0, Qt.AlignBottom)

        self.logoName = QLabel(self.logoWidget)
        self.logoName.setObjectName(u"logoName")
        self.logoName.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiBold"])
        font.setPointSize(20)
        font.setBold(True)
        self.logoName.setFont(font)
        self.logoName.setMargin(5)

        self.horizontalLayout_11.addWidget(self.logoName, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.logoWidget, 0, Qt.AlignRight)

        self.winBtnsWidgetP = QFrame(self.headerProfile)
        self.winBtnsWidgetP.setObjectName(u"winBtnsWidgetP")
        self.winBtnsWidgetP.setFrameShape(QFrame.StyledPanel)
        self.winBtnsWidgetP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.winBtnsWidgetP)
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.closeBtnP = QPushButton(self.winBtnsWidgetP)
        self.closeBtnP.setObjectName(u"closeBtnP")
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtnP.setIcon(icon1)
        self.closeBtnP.setIconSize(QSize(16, 16))
        self.closeBtnP.setFlat(True)

        self.horizontalLayout_8.addWidget(self.closeBtnP)


        self.horizontalLayout_7.addWidget(self.winBtnsWidgetP, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.headerProfile, 0, Qt.AlignTop)

        self.mainContentsProfile = QWidget(self.leftBody)
        self.mainContentsProfile.setObjectName(u"mainContentsProfile")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainContentsProfile.sizePolicy().hasHeightForWidth())
        self.mainContentsProfile.setSizePolicy(sizePolicy)
        self.mainContentsProfile.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_9 = QHBoxLayout(self.mainContentsProfile)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.mainProfileCont = QWidget(self.mainContentsProfile)
        self.mainProfileCont.setObjectName(u"mainProfileCont")
        self.mainProfileCont.setMinimumSize(QSize(0, 460))
        self.verticalLayout_11 = QVBoxLayout(self.mainProfileCont)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 35, 0, 65)
        self.firstnameWidget = QWidget(self.mainProfileCont)
        self.firstnameWidget.setObjectName(u"firstnameWidget")
        self.firstnameWidget.setMinimumSize(QSize(360, 45))
        self.firstnameWidget.setMaximumSize(QSize(360, 45))
        self.horizontalLayout_2 = QHBoxLayout(self.firstnameWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.firstnameWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(80, 0))
        self.label_5.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.label_5)

        self.firstnameLineEdit = QLineEdit(self.firstnameWidget)
        self.firstnameLineEdit.setObjectName(u"firstnameLineEdit")
        self.firstnameLineEdit.setMinimumSize(QSize(250, 30))
        self.firstnameLineEdit.setMaximumSize(QSize(250, 30))

        self.horizontalLayout_2.addWidget(self.firstnameLineEdit)


        self.verticalLayout_11.addWidget(self.firstnameWidget, 0, Qt.AlignLeft)

        self.lastnameWidget = QWidget(self.mainProfileCont)
        self.lastnameWidget.setObjectName(u"lastnameWidget")
        self.lastnameWidget.setMinimumSize(QSize(360, 45))
        self.lastnameWidget.setMaximumSize(QSize(360, 45))
        self.horizontalLayout_3 = QHBoxLayout(self.lastnameWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.lastnameWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 0))
        self.label_6.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.label_6)

        self.lastnameLineEdit = QLineEdit(self.lastnameWidget)
        self.lastnameLineEdit.setObjectName(u"lastnameLineEdit")
        self.lastnameLineEdit.setMinimumSize(QSize(250, 30))
        self.lastnameLineEdit.setMaximumSize(QSize(250, 30))

        self.horizontalLayout_3.addWidget(self.lastnameLineEdit)


        self.verticalLayout_11.addWidget(self.lastnameWidget, 0, Qt.AlignLeft)

        self.patronimicWidget = QWidget(self.mainProfileCont)
        self.patronimicWidget.setObjectName(u"patronimicWidget")
        self.patronimicWidget.setMinimumSize(QSize(360, 45))
        self.patronimicWidget.setMaximumSize(QSize(360, 45))
        self.horizontalLayout_5 = QHBoxLayout(self.patronimicWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.patronimicWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 0))
        self.label_7.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_5.addWidget(self.label_7)

        self.patronimicLineEdit = QLineEdit(self.patronimicWidget)
        self.patronimicLineEdit.setObjectName(u"patronimicLineEdit")
        self.patronimicLineEdit.setMinimumSize(QSize(250, 30))
        self.patronimicLineEdit.setMaximumSize(QSize(250, 30))

        self.horizontalLayout_5.addWidget(self.patronimicLineEdit)


        self.verticalLayout_11.addWidget(self.patronimicWidget, 0, Qt.AlignLeft)

        self.widget_5 = QWidget(self.mainProfileCont)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(360, 45))
        self.widget_5.setMaximumSize(QSize(360, 45))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label8 = QLabel(self.widget_5)
        self.label8.setObjectName(u"label8")
        self.label8.setMinimumSize(QSize(85, 0))
        self.label8.setMaximumSize(QSize(85, 16777215))
        self.label8.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.label8)

        self.phoneLineEdit = QLineEdit(self.widget_5)
        self.phoneLineEdit.setObjectName(u"phoneLineEdit")
        self.phoneLineEdit.setMinimumSize(QSize(250, 30))
        self.phoneLineEdit.setMaximumSize(QSize(250, 30))

        self.horizontalLayout_4.addWidget(self.phoneLineEdit)


        self.verticalLayout_11.addWidget(self.widget_5, 0, Qt.AlignLeft)

        self.widget_6 = QWidget(self.mainProfileCont)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(360, 45))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(85, 0))
        self.label_9.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_14.addWidget(self.label_9)

        self.emailLineEdit = QLineEdit(self.widget_6)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setMinimumSize(QSize(250, 30))
        self.emailLineEdit.setMaximumSize(QSize(250, 30))

        self.horizontalLayout_14.addWidget(self.emailLineEdit)


        self.verticalLayout_11.addWidget(self.widget_6, 0, Qt.AlignLeft|Qt.AlignTop)

        self.orgWidget = QWidget(self.mainProfileCont)
        self.orgWidget.setObjectName(u"orgWidget")
        self.orgWidget.setMinimumSize(QSize(480, 45))
        self.orgWidget.setMaximumSize(QSize(480, 45))
        self.horizontalLayout_6 = QHBoxLayout(self.orgWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.orgWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(85, 0))
        self.label_8.setMaximumSize(QSize(85, 80))

        self.horizontalLayout_6.addWidget(self.label_8)

        self.organizationComboBox = QComboBox(self.orgWidget)
        self.organizationComboBox.setObjectName(u"organizationComboBox")
        self.organizationComboBox.setMinimumSize(QSize(250, 30))
        self.organizationComboBox.setMaximumSize(QSize(250, 30))

        self.horizontalLayout_6.addWidget(self.organizationComboBox)


        self.verticalLayout_11.addWidget(self.orgWidget, 0, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.mainProfileCont, 0, Qt.AlignVCenter)


        self.verticalLayout_10.addWidget(self.mainContentsProfile, 0, Qt.AlignTop)

        self.operationsBtns = QWidget(self.leftBody)
        self.operationsBtns.setObjectName(u"operationsBtns")
        self.operationsBtns.setMaximumSize(QSize(800, 16777215))
        self.horizontalLayout_10 = QHBoxLayout(self.operationsBtns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.operationsBtns)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(120, 45))
        self.widget_3.setMaximumSize(QSize(120, 45))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.saveBtn = QPushButton(self.widget_3)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setMinimumSize(QSize(120, 30))
        self.saveBtn.setMaximumSize(QSize(120, 30))
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveBtn.setIcon(icon2)
        self.saveBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.saveBtn)


        self.horizontalLayout_10.addWidget(self.widget_3, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.operationsBtns, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.leftBody)

        ProfileWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProfileWindow)

        QMetaObject.connectSlotsByName(ProfileWindow)
    # setupUi

    def retranslateUi(self, ProfileWindow):
        ProfileWindow.setWindowTitle(QCoreApplication.translate("ProfileWindow", u"MainWindow", None))
        self.profilePic.setText("")
        self.roleLabel.setText(QCoreApplication.translate("ProfileWindow", u"Admin", None))
        self.organizationLabel.setText(QCoreApplication.translate("ProfileWindow", u"\u041e\u041e\u041e \"\u0411\u043e\u043b\u044c\u0448\u0430\u044f \u0422\u0440\u043e\u0439\u043a\u0430\"", None))
        self.fioLabel.setText(QCoreApplication.translate("ProfileWindow", u"Abramtsova Violetta", None))
        self.exitBtn.setText(QCoreApplication.translate("ProfileWindow", u"    \u0412\u044b\u0445\u043e\u0434  ", None))
        self.logoPic.setText("")
        self.logoName.setText(QCoreApplication.translate("ProfileWindow", u"HiHire B3", None))
#if QT_CONFIG(tooltip)
        self.closeBtnP.setToolTip(QCoreApplication.translate("ProfileWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtnP.setText("")
        self.label_5.setText(QCoreApplication.translate("ProfileWindow", u"\u0418\u043c\u044f", None))
        self.label_6.setText(QCoreApplication.translate("ProfileWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("ProfileWindow", u"\u041f\u0440\u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("ProfileWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e*", None))
        self.label8.setText(QCoreApplication.translate("ProfileWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_9.setText(QCoreApplication.translate("ProfileWindow", u"Email", None))
        self.label_8.setText(QCoreApplication.translate("ProfileWindow", u"\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.saveBtn.setText(QCoreApplication.translate("ProfileWindow", u"   \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

