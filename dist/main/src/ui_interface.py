# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1370, 602)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(944, 602))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.menu = QWidget(self.leftMenu)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(46, 42))
        self.verticalLayout_2 = QVBoxLayout(self.menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 5, 0, 5)
        self.menuBtn = QPushButton(self.menu)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))
        self.menuBtn.setAutoRepeatDelay(302)
        self.menuBtn.setFlat(False)

        self.verticalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout.addWidget(self.menu, 0, Qt.AlignLeft|Qt.AlignTop)

        self.topBtnsWiget = QWidget(self.leftMenu)
        self.topBtnsWiget.setObjectName(u"topBtnsWiget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topBtnsWiget.sizePolicy().hasHeightForWidth())
        self.topBtnsWiget.setSizePolicy(sizePolicy)
        self.topBtnsWiget.setMinimumSize(QSize(178, 100))
        self.verticalLayout_3 = QVBoxLayout(self.topBtnsWiget)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.questionsBtn = QPushButton(self.topBtnsWiget)
        self.questionsBtn.setObjectName(u"questionsBtn")
        font = QFont()
        font.setPointSize(10)
        self.questionsBtn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/file-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.questionsBtn.setIcon(icon1)
        self.questionsBtn.setIconSize(QSize(24, 24))
        self.questionsBtn.setFlat(False)

        self.verticalLayout_3.addWidget(self.questionsBtn)

        self.reportsBtn = QPushButton(self.topBtnsWiget)
        self.reportsBtn.setObjectName(u"reportsBtn")
        self.reportsBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/archive.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reportsBtn.setIcon(icon2)
        self.reportsBtn.setIconSize(QSize(24, 24))
        self.reportsBtn.setAutoDefault(False)
        self.reportsBtn.setFlat(False)

        self.verticalLayout_3.addWidget(self.reportsBtn, 0, Qt.AlignLeft)

        self.workersBtn = QPushButton(self.topBtnsWiget)
        self.workersBtn.setObjectName(u"workersBtn")
        self.workersBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.workersBtn.setIcon(icon3)
        self.workersBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.workersBtn)

        self.analysisBtn = QPushButton(self.topBtnsWiget)
        self.analysisBtn.setObjectName(u"analysisBtn")
        self.analysisBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/pie-chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.analysisBtn.setIcon(icon4)
        self.analysisBtn.setIconSize(QSize(24, 24))
        self.analysisBtn.setFlat(False)

        self.verticalLayout_3.addWidget(self.analysisBtn)


        self.verticalLayout.addWidget(self.topBtnsWiget, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.bottomBtnsWidget = QWidget(self.leftMenu)
        self.bottomBtnsWidget.setObjectName(u"bottomBtnsWidget")
        sizePolicy.setHeightForWidth(self.bottomBtnsWidget.sizePolicy().hasHeightForWidth())
        self.bottomBtnsWidget.setSizePolicy(sizePolicy)
        self.bottomBtnsWidget.setMinimumSize(QSize(100, 100))
        self.verticalLayout_4 = QVBoxLayout(self.bottomBtnsWidget)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 5)
        self.prifileBtn = QPushButton(self.bottomBtnsWidget)
        self.prifileBtn.setObjectName(u"prifileBtn")
        self.prifileBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prifileBtn.setIcon(icon5)
        self.prifileBtn.setIconSize(QSize(24, 24))
        self.prifileBtn.setFlat(False)

        self.verticalLayout_4.addWidget(self.prifileBtn, 0, Qt.AlignLeft)

        self.settingsBtn = QPushButton(self.bottomBtnsWidget)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon6)
        self.settingsBtn.setIconSize(QSize(24, 24))
        self.settingsBtn.setFlat(False)

        self.verticalLayout_4.addWidget(self.settingsBtn, 0, Qt.AlignLeft)

        self.helpBtn = QPushButton(self.bottomBtnsWidget)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/help-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon7)
        self.helpBtn.setIconSize(QSize(24, 24))
        self.helpBtn.setFlat(False)

        self.verticalLayout_4.addWidget(self.helpBtn, 0, Qt.AlignLeft)

        self.infoBtn = QPushButton(self.bottomBtnsWidget)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setFont(font)
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon8)
        self.infoBtn.setIconSize(QSize(24, 24))
        self.infoBtn.setFlat(False)

        self.verticalLayout_4.addWidget(self.infoBtn, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.bottomBtnsWidget, 0, Qt.AlignBottom)

        self.topBtnsWiget.raise_()
        self.menu.raise_()
        self.bottomBtnsWidget.raise_()

        self.horizontalLayout.addWidget(self.leftMenu)

        self.centerMenu = QCustomSlideMenu(self.centralwidget)
        self.centerMenu.setObjectName(u"centerMenu")
        self.centerMenu.setMaximumSize(QSize(200, 16777215))
        self.centerMenu.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.centerMenu)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.widget = QWidget(self.centerMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(60, 5, 5, 5)
        self.closeLeftMenuBtn = QPushButton(self.widget)
        self.closeLeftMenuBtn.setObjectName(u"closeLeftMenuBtn")
        icon9 = QIcon()
        icon9.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeLeftMenuBtn.setIcon(icon9)
        self.closeLeftMenuBtn.setIconSize(QSize(24, 24))
        self.closeLeftMenuBtn.setAutoDefault(False)
        self.closeLeftMenuBtn.setFlat(True)

        self.horizontalLayout_2.addWidget(self.closeLeftMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.widget)

        self.centerMenuPages = QCustomQStackedWidget(self.centerMenu)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_6 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.widget_4 = QWidget(self.settingsPage)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_7 = QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_7.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.widget_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.themeList = QComboBox(self.frame)
        self.themeList.setObjectName(u"themeList")
        font2 = QFont()
        font2.setPointSize(11)
        self.themeList.setFont(font2)

        self.horizontalLayout_3.addWidget(self.themeList)


        self.verticalLayout_7.addWidget(self.frame)


        self.verticalLayout_6.addWidget(self.widget_4, 0, Qt.AlignTop)

        self.centerMenuPages.addWidget(self.settingsPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_9 = QVBoxLayout(self.helpPage)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.helpPage)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_18 = QVBoxLayout(self.widget_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(47, 16))

        self.verticalLayout_18.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.textEdit = QTextEdit(self.helpPage)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.verticalLayout_9.addWidget(self.textEdit)

        self.centerMenuPages.addWidget(self.helpPage)
        self.informationPage = QWidget()
        self.informationPage.setObjectName(u"informationPage")
        self.verticalLayout_8 = QVBoxLayout(self.informationPage)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.informationPage)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_19 = QVBoxLayout(self.widget_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_19.addWidget(self.label_4)


        self.verticalLayout_8.addWidget(self.widget_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.textEdit_2 = QTextEdit(self.informationPage)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.textEdit_2)

        self.centerMenuPages.addWidget(self.informationPage)

        self.verticalLayout_5.addWidget(self.centerMenuPages)


        self.horizontalLayout.addWidget(self.centerMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.verticalLayout_10 = QVBoxLayout(self.mainBody)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.mainBody)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.header)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 0, 5)
        self.logoWidget = QWidget(self.header)
        self.logoWidget.setObjectName(u"logoWidget")
        self.logoWidget.setMinimumSize(QSize(150, 0))
        self.horizontalLayout_11 = QHBoxLayout(self.logoWidget)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_7.addWidget(self.logoWidget)

        self.systemBtnsWidget = QFrame(self.header)
        self.systemBtnsWidget.setObjectName(u"systemBtnsWidget")
        self.systemBtnsWidget.setMinimumSize(QSize(150, 0))
        self.systemBtnsWidget.setFrameShape(QFrame.StyledPanel)
        self.systemBtnsWidget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.systemBtnsWidget)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.logoPic = QLabel(self.systemBtnsWidget)
        self.logoPic.setObjectName(u"logoPic")
        self.logoPic.setMaximumSize(QSize(45, 45))
        self.logoPic.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(9)
        self.logoPic.setFont(font3)
        self.logoPic.setPixmap(QPixmap(u"../Qss/icons/logo.png"))
        self.logoPic.setScaledContents(True)
        self.logoPic.setMargin(0)
        self.logoPic.setIndent(-1)

        self.horizontalLayout_6.addWidget(self.logoPic)

        self.logoName = QLabel(self.systemBtnsWidget)
        self.logoName.setObjectName(u"logoName")
        self.logoName.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift SemiBold"])
        font4.setPointSize(23)
        font4.setBold(True)
        self.logoName.setFont(font4)
        self.logoName.setMargin(5)

        self.horizontalLayout_6.addWidget(self.logoName)


        self.horizontalLayout_7.addWidget(self.systemBtnsWidget, 0, Qt.AlignHCenter)

        self.winBtnsWidget = QFrame(self.header)
        self.winBtnsWidget.setObjectName(u"winBtnsWidget")
        self.winBtnsWidget.setFrameShape(QFrame.StyledPanel)
        self.winBtnsWidget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.winBtnsWidget)
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.wrapBtn = QPushButton(self.winBtnsWidget)
        self.wrapBtn.setObjectName(u"wrapBtn")
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.wrapBtn.setIcon(icon10)
        self.wrapBtn.setIconSize(QSize(16, 16))
        self.wrapBtn.setFlat(True)

        self.horizontalLayout_8.addWidget(self.wrapBtn)

        self.changeWinBtn = QPushButton(self.winBtnsWidget)
        self.changeWinBtn.setObjectName(u"changeWinBtn")
        self.changeWinBtn.setLayoutDirection(Qt.LeftToRight)
        icon11 = QIcon()
        icon11.addFile(u":/feather/icons/feather/square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.changeWinBtn.setIcon(icon11)
        self.changeWinBtn.setFlat(True)

        self.horizontalLayout_8.addWidget(self.changeWinBtn)

        self.closeBtn = QPushButton(self.winBtnsWidget)
        self.closeBtn.setObjectName(u"closeBtn")
        icon12 = QIcon()
        icon12.addFile(u":/feather/icons/feather/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon12)
        self.closeBtn.setIconSize(QSize(16, 16))
        self.closeBtn.setFlat(True)

        self.horizontalLayout_8.addWidget(self.closeBtn)


        self.horizontalLayout_7.addWidget(self.winBtnsWidget, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.header, 0, Qt.AlignTop)

        self.mainContents = QWidget(self.mainBody)
        self.mainContents.setObjectName(u"mainContents")
        sizePolicy.setHeightForWidth(self.mainContents.sizePolicy().hasHeightForWidth())
        self.mainContents.setSizePolicy(sizePolicy)
        self.horizontalLayout_9 = QHBoxLayout(self.mainContents)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.mainPageCont = QWidget(self.mainContents)
        self.mainPageCont.setObjectName(u"mainPageCont")
        self.verticalLayout_11 = QVBoxLayout(self.mainPageCont)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.mainPages = QCustomQStackedWidget(self.mainPageCont)
        self.mainPages.setObjectName(u"mainPages")
        self.dataAnalysPage = QWidget()
        self.dataAnalysPage.setObjectName(u"dataAnalysPage")
        self.verticalLayout_12 = QVBoxLayout(self.dataAnalysPage)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.afiltersWidget = QWidget(self.dataAnalysPage)
        self.afiltersWidget.setObjectName(u"afiltersWidget")
        self.verticalLayout_49 = QVBoxLayout(self.afiltersWidget)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.widget_36 = QWidget(self.afiltersWidget)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_42 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label60 = QLabel(self.widget_36)
        self.label60.setObjectName(u"label60")
        self.label60.setMinimumSize(QSize(110, 25))
        self.label60.setMaximumSize(QSize(110, 25))
        font5 = QFont()
        font5.setPointSize(14)
        self.label60.setFont(font5)

        self.horizontalLayout_42.addWidget(self.label60)

        self.comboBox = QComboBox(self.widget_36)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 25))
        self.comboBox.setFont(font5)

        self.horizontalLayout_42.addWidget(self.comboBox)

        self.label_9 = QLabel(self.widget_36)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 25))
        self.label_9.setMaximumSize(QSize(150, 25))
        self.label_9.setFont(font5)

        self.horizontalLayout_42.addWidget(self.label_9)

        self.comboBox_2 = QComboBox(self.widget_36)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(200, 25))
        self.comboBox_2.setMaximumSize(QSize(200, 25))
        self.comboBox_2.setFont(font5)

        self.horizontalLayout_42.addWidget(self.comboBox_2)


        self.verticalLayout_49.addWidget(self.widget_36, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_38 = QWidget(self.afiltersWidget)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_43 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_20 = QLabel(self.widget_38)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(100, 25))
        self.label_20.setMaximumSize(QSize(60, 25))
        self.label_20.setFont(font5)

        self.horizontalLayout_43.addWidget(self.label_20, 0, Qt.AlignLeft)

        self.widget_46 = QWidget(self.widget_38)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setMinimumSize(QSize(120, 0))
        self.verticalLayout_59 = QVBoxLayout(self.widget_46)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.dateEdit = QDateEdit(self.widget_46)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(200, 30))
        self.dateEdit.setMaximumSize(QSize(200, 30))
        self.dateEdit.setFont(font1)

        self.verticalLayout_59.addWidget(self.dateEdit)


        self.horizontalLayout_43.addWidget(self.widget_46)

        self.label_25 = QLabel(self.widget_38)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(45, 25))
        self.label_25.setMaximumSize(QSize(45, 25))
        self.label_25.setFont(font5)

        self.horizontalLayout_43.addWidget(self.label_25, 0, Qt.AlignLeft)

        self.widget_47 = QWidget(self.widget_38)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setMinimumSize(QSize(120, 0))
        self.verticalLayout_60 = QVBoxLayout(self.widget_47)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.dateEdit_2 = QDateEdit(self.widget_47)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMinimumSize(QSize(160, 30))
        self.dateEdit_2.setMaximumSize(QSize(160, 30))
        self.dateEdit_2.setFont(font1)

        self.verticalLayout_60.addWidget(self.dateEdit_2)


        self.horizontalLayout_43.addWidget(self.widget_47)


        self.verticalLayout_49.addWidget(self.widget_38, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.afiltersWidget, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(self.dataAnalysPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 553, 392))
        self.verticalLayout_58 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.widget_37 = QWidget(self.scrollAreaWidgetContents)
        self.widget_37.setObjectName(u"widget_37")
        self.verticalLayout_51 = QVBoxLayout(self.widget_37)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_58.addWidget(self.widget_37)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.mainPages.addWidget(self.dataAnalysPage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.verticalLayout_14 = QVBoxLayout(self.reportsPage)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 5, 0)
        self.filtersWidget = QWidget(self.reportsPage)
        self.filtersWidget.setObjectName(u"filtersWidget")
        self.filtersWidget.setMinimumSize(QSize(0, 0))
        self.filtersWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_50 = QVBoxLayout(self.filtersWidget)
        self.verticalLayout_50.setSpacing(5)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.filtersWidget)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(815, 0))
        self.horizontalLayout_20 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_14)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(230, 0))
        self.widget_16.setMaximumSize(QSize(230, 16777215))
        self.horizontalLayout_22 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.clabel = QLabel(self.widget_16)
        self.clabel.setObjectName(u"clabel")
        self.clabel.setMinimumSize(QSize(70, 20))
        self.clabel.setMaximumSize(QSize(80, 20))
        self.clabel.setFont(font1)

        self.horizontalLayout_22.addWidget(self.clabel)

        self.candidateLineEdit = QLineEdit(self.widget_16)
        self.candidateLineEdit.setObjectName(u"candidateLineEdit")
        self.candidateLineEdit.setMinimumSize(QSize(150, 25))
        self.candidateLineEdit.setMaximumSize(QSize(150, 25))
        self.candidateLineEdit.setFont(font1)

        self.horizontalLayout_22.addWidget(self.candidateLineEdit)


        self.horizontalLayout_20.addWidget(self.widget_16, 0, Qt.AlignLeft)

        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(700, 0))
        self.horizontalLayout_21 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.dlabel = QLabel(self.widget_15)
        self.dlabel.setObjectName(u"dlabel")
        self.dlabel.setMinimumSize(QSize(115, 20))
        self.dlabel.setMaximumSize(QSize(115, 20))
        self.dlabel.setFont(font1)

        self.horizontalLayout_21.addWidget(self.dlabel)

        self.stlabel = QLabel(self.widget_15)
        self.stlabel.setObjectName(u"stlabel")
        self.stlabel.setMinimumSize(QSize(20, 20))
        self.stlabel.setMaximumSize(QSize(20, 20))
        self.stlabel.setFont(font1)

        self.horizontalLayout_21.addWidget(self.stlabel)

        self.startDateEdit = QDateEdit(self.widget_15)
        self.startDateEdit.setObjectName(u"startDateEdit")
        self.startDateEdit.setMinimumSize(QSize(110, 25))
        self.startDateEdit.setMaximumSize(QSize(110, 25))
        self.startDateEdit.setFont(font1)

        self.horizontalLayout_21.addWidget(self.startDateEdit)

        self.label_18 = QLabel(self.widget_15)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(30, 20))
        self.label_18.setMaximumSize(QSize(30, 20))
        self.label_18.setFont(font1)

        self.horizontalLayout_21.addWidget(self.label_18)

        self.endDateEdit = QDateEdit(self.widget_15)
        self.endDateEdit.setObjectName(u"endDateEdit")
        self.endDateEdit.setMinimumSize(QSize(110, 25))
        self.endDateEdit.setMaximumSize(QSize(110, 25))
        self.endDateEdit.setFont(font1)

        self.horizontalLayout_21.addWidget(self.endDateEdit)

        self.widget_39 = QWidget(self.widget_15)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setMinimumSize(QSize(265, 0))
        self.horizontalLayout_44 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_44.setSpacing(2)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.exportBtn = QPushButton(self.widget_39)
        self.exportBtn.setObjectName(u"exportBtn")
        self.exportBtn.setMinimumSize(QSize(130, 30))
        self.exportBtn.setMaximumSize(QSize(130, 30))
        self.exportBtn.setFont(font1)
        icon13 = QIcon()
        icon13.addFile(u":/feather/icons/feather/arrow-down-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exportBtn.setIcon(icon13)
        self.exportBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_44.addWidget(self.exportBtn)

        self.importBtn = QPushButton(self.widget_39)
        self.importBtn.setObjectName(u"importBtn")
        self.importBtn.setMinimumSize(QSize(130, 30))
        self.importBtn.setMaximumSize(QSize(130, 30))
        self.importBtn.setFont(font1)
        icon14 = QIcon()
        icon14.addFile(u":/feather/icons/feather/arrow-up-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.importBtn.setIcon(icon14)
        self.importBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_44.addWidget(self.importBtn)


        self.horizontalLayout_21.addWidget(self.widget_39)


        self.horizontalLayout_20.addWidget(self.widget_15, 0, Qt.AlignLeft)


        self.verticalLayout_50.addWidget(self.widget_14, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_13 = QWidget(self.filtersWidget)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 45))
        self.horizontalLayout_47 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_47.setSpacing(9)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_13)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 20))
        self.label_11.setMaximumSize(QSize(100, 20))
        self.label_11.setFont(font1)

        self.horizontalLayout_47.addWidget(self.label_11, 0, Qt.AlignVCenter)

        self.positionComboBox = QComboBox(self.widget_13)
        self.positionComboBox.setObjectName(u"positionComboBox")
        self.positionComboBox.setMinimumSize(QSize(200, 25))
        self.positionComboBox.setMaximumSize(QSize(200, 25))
        self.positionComboBox.setFont(font1)

        self.horizontalLayout_47.addWidget(self.positionComboBox)

        self.slabel = QLabel(self.widget_13)
        self.slabel.setObjectName(u"slabel")
        self.slabel.setMinimumSize(QSize(60, 20))
        self.slabel.setMaximumSize(QSize(60, 20))
        self.slabel.setFont(font1)

        self.horizontalLayout_47.addWidget(self.slabel, 0, Qt.AlignVCenter)

        self.statusesComboBox = QComboBox(self.widget_13)
        self.statusesComboBox.setObjectName(u"statusesComboBox")
        self.statusesComboBox.setMinimumSize(QSize(150, 25))
        self.statusesComboBox.setMaximumSize(QSize(150, 25))
        self.statusesComboBox.setFont(font1)

        self.horizontalLayout_47.addWidget(self.statusesComboBox)

        self.label60_2 = QLabel(self.widget_13)
        self.label60_2.setObjectName(u"label60_2")
        self.label60_2.setMinimumSize(QSize(200, 25))
        self.label60_2.setMaximumSize(QSize(200, 25))
        self.label60_2.setFont(font1)

        self.horizontalLayout_47.addWidget(self.label60_2, 0, Qt.AlignVCenter)

        self.scoreSortComboBox = QComboBox(self.widget_13)
        self.scoreSortComboBox.setObjectName(u"scoreSortComboBox")
        self.scoreSortComboBox.setMinimumSize(QSize(200, 25))
        self.scoreSortComboBox.setMaximumSize(QSize(200, 25))
        self.scoreSortComboBox.setFont(font1)

        self.horizontalLayout_47.addWidget(self.scoreSortComboBox)


        self.verticalLayout_50.addWidget(self.widget_13, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_14.addWidget(self.filtersWidget, 0, Qt.AlignTop)

        self.candidatesWidget = QWidget(self.reportsPage)
        self.candidatesWidget.setObjectName(u"candidatesWidget")
        self.verticalLayout_33 = QVBoxLayout(self.candidatesWidget)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 10, 0, 0)
        self.candidatesSscrollArea = QScrollArea(self.candidatesWidget)
        self.candidatesSscrollArea.setObjectName(u"candidatesSscrollArea")
        self.candidatesSscrollArea.setWidgetResizable(True)
        self.candidatesScrollAreaWidgetContents = QWidget()
        self.candidatesScrollAreaWidgetContents.setObjectName(u"candidatesScrollAreaWidgetContents")
        self.candidatesScrollAreaWidgetContents.setGeometry(QRect(0, 0, 953, 375))
        self.verticalLayout_40 = QVBoxLayout(self.candidatesScrollAreaWidgetContents)
        self.verticalLayout_40.setSpacing(5)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.candidatesVerticalLayout = QVBoxLayout()
        self.candidatesVerticalLayout.setObjectName(u"candidatesVerticalLayout")

        self.verticalLayout_40.addLayout(self.candidatesVerticalLayout)

        self.candidatesSscrollArea.setWidget(self.candidatesScrollAreaWidgetContents)

        self.verticalLayout_33.addWidget(self.candidatesSscrollArea)


        self.verticalLayout_14.addWidget(self.candidatesWidget)

        self.mainPages.addWidget(self.reportsPage)
        self.candidatePage = QWidget()
        self.candidatePage.setObjectName(u"candidatePage")
        self.verticalLayout_34 = QVBoxLayout(self.candidatePage)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.candidateHead = QWidget(self.candidatePage)
        self.candidateHead.setObjectName(u"candidateHead")
        self.horizontalLayout_23 = QHBoxLayout(self.candidateHead)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.candidateHead)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_35 = QVBoxLayout(self.widget_17)
        self.verticalLayout_35.setSpacing(5)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, -1, 0, 10)
        self.exitFromCandidateBtn = QPushButton(self.widget_17)
        self.exitFromCandidateBtn.setObjectName(u"exitFromCandidateBtn")
        self.exitFromCandidateBtn.setMinimumSize(QSize(85, 30))
        self.exitFromCandidateBtn.setMaximumSize(QSize(85, 30))
        self.exitFromCandidateBtn.setFont(font1)
        icon15 = QIcon()
        icon15.addFile(u":/feather/icons/feather/corner-up-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitFromCandidateBtn.setIcon(icon15)
        self.exitFromCandidateBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_35.addWidget(self.exitFromCandidateBtn)

        self.candidateLabel = QLabel(self.widget_17)
        self.candidateLabel.setObjectName(u"candidateLabel")
        self.candidateLabel.setMinimumSize(QSize(350, 25))
        self.candidateLabel.setMaximumSize(QSize(350, 25))
        font6 = QFont()
        font6.setPointSize(16)
        self.candidateLabel.setFont(font6)

        self.verticalLayout_35.addWidget(self.candidateLabel)


        self.horizontalLayout_23.addWidget(self.widget_17, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_18 = QWidget(self.candidateHead)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.statusLabel = QLabel(self.widget_18)
        self.statusLabel.setObjectName(u"statusLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(60)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy1)
        self.statusLabel.setMinimumSize(QSize(60, 0))
        self.statusLabel.setFont(font1)

        self.horizontalLayout_24.addWidget(self.statusLabel)


        self.horizontalLayout_23.addWidget(self.widget_18, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_34.addWidget(self.candidateHead)

        self.candidateContentWidget = QWidget(self.candidatePage)
        self.candidateContentWidget.setObjectName(u"candidateContentWidget")
        self.verticalLayout_36 = QVBoxLayout(self.candidateContentWidget)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.candidatScrollArea = QScrollArea(self.candidateContentWidget)
        self.candidatScrollArea.setObjectName(u"candidatScrollArea")
        self.candidatScrollArea.setWidgetResizable(True)
        self.candidateScrollAreaWidgetContents = QWidget()
        self.candidateScrollAreaWidgetContents.setObjectName(u"candidateScrollAreaWidgetContents")
        self.candidateScrollAreaWidgetContents.setGeometry(QRect(0, 0, 947, 366))
        self.verticalLayout_38 = QVBoxLayout(self.candidateScrollAreaWidgetContents)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.candidateVverticalLayout = QVBoxLayout()
        self.candidateVverticalLayout.setSpacing(0)
        self.candidateVverticalLayout.setObjectName(u"candidateVverticalLayout")
        self.candidateVverticalLayout.setContentsMargins(5, -1, -1, -1)
        self.widget_48 = QWidget(self.candidateScrollAreaWidgetContents)
        self.widget_48.setObjectName(u"widget_48")
        self.verticalLayout_61 = QVBoxLayout(self.widget_48)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.candidateFIOLabel = QLabel(self.widget_48)
        self.candidateFIOLabel.setObjectName(u"candidateFIOLabel")
        self.candidateFIOLabel.setMinimumSize(QSize(300, 40))
        self.candidateFIOLabel.setMaximumSize(QSize(16777215, 40))
        font7 = QFont()
        font7.setPointSize(20)
        self.candidateFIOLabel.setFont(font7)

        self.verticalLayout_61.addWidget(self.candidateFIOLabel)

        self.widget_22 = QWidget(self.widget_48)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.llabel = QLabel(self.widget_22)
        self.llabel.setObjectName(u"llabel")
        self.llabel.setMinimumSize(QSize(120, 0))
        self.llabel.setMaximumSize(QSize(165, 16777215))
        self.llabel.setFont(font2)

        self.horizontalLayout_29.addWidget(self.llabel)

        self.linkLabel = QLabel(self.widget_22)
        self.linkLabel.setObjectName(u"linkLabel")
        self.linkLabel.setMinimumSize(QSize(200, 0))
        self.linkLabel.setMaximumSize(QSize(150, 16777215))
        self.linkLabel.setFont(font2)

        self.horizontalLayout_29.addWidget(self.linkLabel)

        self.label110 = QLabel(self.widget_22)
        self.label110.setObjectName(u"label110")
        self.label110.setMinimumSize(QSize(45, 0))
        self.label110.setMaximumSize(QSize(55, 16777215))
        self.label110.setFont(font2)

        self.horizontalLayout_29.addWidget(self.label110)

        self.emailLabel = QLabel(self.widget_22)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setFont(font2)

        self.horizontalLayout_29.addWidget(self.emailLabel)


        self.verticalLayout_61.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.widget_48)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label52 = QLabel(self.widget_23)
        self.label52.setObjectName(u"label52")
        self.label52.setMaximumSize(QSize(110, 16777215))
        self.label52.setFont(font2)

        self.horizontalLayout_30.addWidget(self.label52)

        self.positionName = QLabel(self.widget_23)
        self.positionName.setObjectName(u"positionName")
        self.positionName.setFont(font2)

        self.horizontalLayout_30.addWidget(self.positionName)


        self.verticalLayout_61.addWidget(self.widget_23)

        self.widget_19 = QWidget(self.widget_48)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label53 = QLabel(self.widget_19)
        self.label53.setObjectName(u"label53")
        self.label53.setMaximumSize(QSize(90, 16777215))
        self.label53.setFont(font2)

        self.horizontalLayout_26.addWidget(self.label53)

        self.scoreLabel = QLabel(self.widget_19)
        self.scoreLabel.setObjectName(u"scoreLabel")
        self.scoreLabel.setFont(font2)

        self.horizontalLayout_26.addWidget(self.scoreLabel)


        self.verticalLayout_61.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.widget_48)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.recommendationText = QLabel(self.widget_20)
        self.recommendationText.setObjectName(u"recommendationText")
        self.recommendationText.setFont(font2)

        self.horizontalLayout_27.addWidget(self.recommendationText, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_61.addWidget(self.widget_20)

        self.questionnaryName = QLabel(self.widget_48)
        self.questionnaryName.setObjectName(u"questionnaryName")
        self.questionnaryName.setMinimumSize(QSize(300, 40))
        self.questionnaryName.setMaximumSize(QSize(300, 40))
        self.questionnaryName.setFont(font5)

        self.verticalLayout_61.addWidget(self.questionnaryName)

        self.answersWidget = QWidget(self.widget_48)
        self.answersWidget.setObjectName(u"answersWidget")
        self.verticalLayout_37 = QVBoxLayout(self.answersWidget)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_61.addWidget(self.answersWidget)


        self.candidateVverticalLayout.addWidget(self.widget_48, 0, Qt.AlignTop)


        self.verticalLayout_38.addLayout(self.candidateVverticalLayout)

        self.candidatScrollArea.setWidget(self.candidateScrollAreaWidgetContents)

        self.verticalLayout_36.addWidget(self.candidatScrollArea)


        self.verticalLayout_34.addWidget(self.candidateContentWidget)

        self.candidateBottom = QWidget(self.candidatePage)
        self.candidateBottom.setObjectName(u"candidateBottom")
        self.horizontalLayout_25 = QHBoxLayout(self.candidateBottom)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 8, 0, 0)
        self.rejectBtn = QPushButton(self.candidateBottom)
        self.rejectBtn.setObjectName(u"rejectBtn")
        self.rejectBtn.setMinimumSize(QSize(130, 30))
        self.rejectBtn.setMaximumSize(QSize(130, 30))
        self.rejectBtn.setFont(font1)
        icon16 = QIcon()
        icon16.addFile(u":/feather/icons/feather/thumbs-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rejectBtn.setIcon(icon16)
        self.rejectBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_25.addWidget(self.rejectBtn)

        self.acceptBtn = QPushButton(self.candidateBottom)
        self.acceptBtn.setObjectName(u"acceptBtn")
        self.acceptBtn.setMinimumSize(QSize(130, 30))
        self.acceptBtn.setMaximumSize(QSize(130, 30))
        self.acceptBtn.setFont(font1)
        icon17 = QIcon()
        icon17.addFile(u":/feather/icons/feather/thumbs-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.acceptBtn.setIcon(icon17)
        self.acceptBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_25.addWidget(self.acceptBtn)

        self.disagreeBtn = QPushButton(self.candidateBottom)
        self.disagreeBtn.setObjectName(u"disagreeBtn")
        self.disagreeBtn.setMinimumSize(QSize(130, 30))
        self.disagreeBtn.setMaximumSize(QSize(130, 30))
        self.disagreeBtn.setFont(font1)
        icon18 = QIcon()
        icon18.addFile(u":/feather/icons/feather/user-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.disagreeBtn.setIcon(icon18)
        self.disagreeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_25.addWidget(self.disagreeBtn)

        self.agreeBtn = QPushButton(self.candidateBottom)
        self.agreeBtn.setObjectName(u"agreeBtn")
        self.agreeBtn.setMinimumSize(QSize(130, 30))
        self.agreeBtn.setMaximumSize(QSize(130, 30))
        self.agreeBtn.setFont(font1)
        icon19 = QIcon()
        icon19.addFile(u":/feather/icons/feather/user-check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agreeBtn.setIcon(icon19)
        self.agreeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_25.addWidget(self.agreeBtn)


        self.verticalLayout_34.addWidget(self.candidateBottom, 0, Qt.AlignBottom)

        self.mainPages.addWidget(self.candidatePage)
        self.questionsPage = QWidget()
        self.questionsPage.setObjectName(u"questionsPage")
        self.verticalLayout_13 = QVBoxLayout(self.questionsPage)
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.addWidget = QWidget(self.questionsPage)
        self.addWidget.setObjectName(u"addWidget")
        self.addWidget.setMinimumSize(QSize(160, 45))
        self.addWidget.setMaximumSize(QSize(160, 45))
        self.horizontalLayout_5 = QHBoxLayout(self.addWidget)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.addQuestionaryBtn = QPushButton(self.addWidget)
        self.addQuestionaryBtn.setObjectName(u"addQuestionaryBtn")
        self.addQuestionaryBtn.setMinimumSize(QSize(150, 30))
        self.addQuestionaryBtn.setMaximumSize(QSize(150, 30))
        self.addQuestionaryBtn.setFont(font1)
        icon20 = QIcon()
        icon20.addFile(u":/font_awesome_regular/icons/font_awesome/regular/square-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addQuestionaryBtn.setIcon(icon20)
        self.addQuestionaryBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.addQuestionaryBtn)


        self.verticalLayout_13.addWidget(self.addWidget, 0, Qt.AlignRight)

        self.systemWidgets = QWidget(self.questionsPage)
        self.systemWidgets.setObjectName(u"systemWidgets")
        self.systemWidgets.setMinimumSize(QSize(0, 217))
        self.systemWidgets.setSizeIncrement(QSize(0, 217))
        self.verticalLayout_20 = QVBoxLayout(self.systemWidgets)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.labelSys = QLabel(self.systemWidgets)
        self.labelSys.setObjectName(u"labelSys")
        self.labelSys.setMinimumSize(QSize(0, 25))
        self.labelSys.setMaximumSize(QSize(16777215, 25))
        font8 = QFont()
        font8.setPointSize(17)
        self.labelSys.setFont(font8)

        self.verticalLayout_20.addWidget(self.labelSys)

        self.systemTemplates = QWidget(self.systemWidgets)
        self.systemTemplates.setObjectName(u"systemTemplates")
        self.horizontalLayout_12 = QHBoxLayout(self.systemTemplates)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.analystTemplateFrame = QFrame(self.systemTemplates)
        self.analystTemplateFrame.setObjectName(u"analystTemplateFrame")
        self.analystTemplateFrame.setMinimumSize(QSize(150, 150))
        self.analystTemplateFrame.setMaximumSize(QSize(250, 150))
        self.analystTemplateFrame.setFrameShape(QFrame.NoFrame)
        self.analystTemplateFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.analystTemplateFrame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label1 = QLabel(self.analystTemplateFrame)
        self.label1.setObjectName(u"label1")
        self.label1.setMinimumSize(QSize(0, 0))
        self.label1.setMaximumSize(QSize(16777215, 16777215))
        self.label1.setFont(font1)
        self.label1.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.label1, 0, Qt.AlignVCenter)

        self.label3 = QLabel(self.analystTemplateFrame)
        self.label3.setObjectName(u"label3")
        self.label3.setMinimumSize(QSize(0, 20))
        self.label3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_22.addWidget(self.label3, 0, Qt.AlignBottom)


        self.horizontalLayout_12.addWidget(self.analystTemplateFrame)

        self.backTemplateFrame = QFrame(self.systemTemplates)
        self.backTemplateFrame.setObjectName(u"backTemplateFrame")
        self.backTemplateFrame.setMinimumSize(QSize(0, 150))
        self.backTemplateFrame.setMaximumSize(QSize(250, 150))
        self.backTemplateFrame.setFrameShape(QFrame.StyledPanel)
        self.backTemplateFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.backTemplateFrame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label2 = QLabel(self.backTemplateFrame)
        self.label2.setObjectName(u"label2")
        self.label2.setMinimumSize(QSize(0, 0))
        self.label2.setFont(font1)
        self.label2.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.label2)

        self.label4 = QLabel(self.backTemplateFrame)
        self.label4.setObjectName(u"label4")
        self.label4.setMinimumSize(QSize(0, 20))
        self.label4.setMaximumSize(QSize(16777215, 20))
        self.label4.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_23.addWidget(self.label4, 0, Qt.AlignBottom)


        self.horizontalLayout_12.addWidget(self.backTemplateFrame)

        self.frontTemplateFrame = QFrame(self.systemTemplates)
        self.frontTemplateFrame.setObjectName(u"frontTemplateFrame")
        self.frontTemplateFrame.setMinimumSize(QSize(0, 150))
        self.frontTemplateFrame.setMaximumSize(QSize(250, 150))
        self.frontTemplateFrame.setFrameShape(QFrame.StyledPanel)
        self.frontTemplateFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frontTemplateFrame)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_7 = QLabel(self.frontTemplateFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setFont(font1)
        self.label_7.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.label_7)

        self.label_8 = QLabel(self.frontTemplateFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 20))
        self.label_8.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_24.addWidget(self.label_8, 0, Qt.AlignBottom)


        self.horizontalLayout_12.addWidget(self.frontTemplateFrame)


        self.verticalLayout_20.addWidget(self.systemTemplates, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.systemWidgets)

        self.usersWidgets = QWidget(self.questionsPage)
        self.usersWidgets.setObjectName(u"usersWidgets")
        self.verticalLayout_21 = QVBoxLayout(self.usersWidgets)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.labelUser = QLabel(self.usersWidgets)
        self.labelUser.setObjectName(u"labelUser")
        self.labelUser.setMinimumSize(QSize(310, 25))
        self.labelUser.setMaximumSize(QSize(310, 25))
        self.labelUser.setFont(font8)

        self.verticalLayout_21.addWidget(self.labelUser)

        self.usersTemplates = QWidget(self.usersWidgets)
        self.usersTemplates.setObjectName(u"usersTemplates")
        self.horizontalLayout_13 = QHBoxLayout(self.usersTemplates)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_21.addWidget(self.usersTemplates, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.usersWidgets, 0, Qt.AlignTop)

        self.mainPages.addWidget(self.questionsPage)
        self.employeesPage = QWidget()
        self.employeesPage.setObjectName(u"employeesPage")
        self.verticalLayout_17 = QVBoxLayout(self.employeesPage)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.efiltersWidget = QWidget(self.employeesPage)
        self.efiltersWidget.setObjectName(u"efiltersWidget")
        self.verticalLayout_39 = QVBoxLayout(self.efiltersWidget)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.widget_25 = QWidget(self.efiltersWidget)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMinimumSize(QSize(800, 0))
        self.widget_25.setMaximumSize(QSize(800, 16777215))
        self.horizontalLayout_31 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label54 = QLabel(self.widget_25)
        self.label54.setObjectName(u"label54")
        self.label54.setMinimumSize(QSize(50, 30))
        self.label54.setMaximumSize(QSize(50, 30))
        self.label54.setFont(font1)

        self.horizontalLayout_31.addWidget(self.label54)

        self.fioLineEdit = QLineEdit(self.widget_25)
        self.fioLineEdit.setObjectName(u"fioLineEdit")
        self.fioLineEdit.setMinimumSize(QSize(220, 25))
        self.fioLineEdit.setMaximumSize(QSize(220, 25))
        self.fioLineEdit.setFont(font1)

        self.horizontalLayout_31.addWidget(self.fioLineEdit)

        self.label_6 = QLabel(self.widget_25)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 30))
        self.label_6.setMaximumSize(QSize(100, 30))
        self.label_6.setFont(font1)

        self.horizontalLayout_31.addWidget(self.label_6)

        self.ePositionComboBox = QComboBox(self.widget_25)
        self.ePositionComboBox.setObjectName(u"ePositionComboBox")
        self.ePositionComboBox.setMinimumSize(QSize(170, 25))
        self.ePositionComboBox.setMaximumSize(QSize(170, 25))
        self.ePositionComboBox.setFont(font1)

        self.horizontalLayout_31.addWidget(self.ePositionComboBox)


        self.verticalLayout_39.addWidget(self.widget_25, 0, Qt.AlignTop)

        self.widget_24 = QWidget(self.efiltersWidget)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMinimumSize(QSize(0, 0))
        self.widget_24.setMaximumSize(QSize(800, 48))
        self.horizontalLayout_32 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.widget_21 = QWidget(self.widget_24)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(250, 0))
        self.widget_21.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label55 = QLabel(self.widget_21)
        self.label55.setObjectName(u"label55")
        self.label55.setMinimumSize(QSize(60, 30))
        self.label55.setMaximumSize(QSize(60, 30))
        self.label55.setFont(font1)

        self.horizontalLayout_28.addWidget(self.label55)

        self.eStatusComboBox = QComboBox(self.widget_21)
        self.eStatusComboBox.setObjectName(u"eStatusComboBox")
        self.eStatusComboBox.setMinimumSize(QSize(200, 25))
        self.eStatusComboBox.setMaximumSize(QSize(200, 25))
        self.eStatusComboBox.setFont(font1)

        self.horizontalLayout_28.addWidget(self.eStatusComboBox)


        self.horizontalLayout_32.addWidget(self.widget_21, 0, Qt.AlignHCenter)

        self.widget_40 = QWidget(self.widget_24)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMinimumSize(QSize(320, 0))
        self.widget_40.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_48 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label56 = QLabel(self.widget_40)
        self.label56.setObjectName(u"label56")
        self.label56.setMinimumSize(QSize(240, 30))
        self.label56.setMaximumSize(QSize(240, 30))
        self.label56.setFont(font1)

        self.horizontalLayout_48.addWidget(self.label56)

        self.eDateComboBox = QComboBox(self.widget_40)
        self.eDateComboBox.setObjectName(u"eDateComboBox")
        self.eDateComboBox.setMinimumSize(QSize(200, 25))
        self.eDateComboBox.setMaximumSize(QSize(200, 25))
        self.eDateComboBox.setFont(font1)

        self.horizontalLayout_48.addWidget(self.eDateComboBox)


        self.horizontalLayout_32.addWidget(self.widget_40, 0, Qt.AlignHCenter)


        self.verticalLayout_39.addWidget(self.widget_24, 0, Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.efiltersWidget, 0, Qt.AlignTop)

        self.employeesWidget = QWidget(self.employeesPage)
        self.employeesWidget.setObjectName(u"employeesWidget")
        self.verticalLayout_42 = QVBoxLayout(self.employeesWidget)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.employeesScrollArea = QScrollArea(self.employeesWidget)
        self.employeesScrollArea.setObjectName(u"employeesScrollArea")
        self.employeesScrollArea.setWidgetResizable(True)
        self.employeesScrollAreaWidgetContents = QWidget()
        self.employeesScrollAreaWidgetContents.setObjectName(u"employeesScrollAreaWidgetContents")
        self.employeesScrollAreaWidgetContents.setGeometry(QRect(0, 0, 947, 405))
        self.verticalLayout_43 = QVBoxLayout(self.employeesScrollAreaWidgetContents)
        self.verticalLayout_43.setSpacing(6)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.emloyeesVerticalLayout = QVBoxLayout()
        self.emloyeesVerticalLayout.setObjectName(u"emloyeesVerticalLayout")

        self.verticalLayout_43.addLayout(self.emloyeesVerticalLayout)

        self.employeesScrollArea.setWidget(self.employeesScrollAreaWidgetContents)

        self.verticalLayout_42.addWidget(self.employeesScrollArea)


        self.verticalLayout_17.addWidget(self.employeesWidget)

        self.mainPages.addWidget(self.employeesPage)
        self.employeePage = QWidget()
        self.employeePage.setObjectName(u"employeePage")
        self.verticalLayout_41 = QVBoxLayout(self.employeePage)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.emloyeeHeader = QWidget(self.employeePage)
        self.emloyeeHeader.setObjectName(u"emloyeeHeader")
        self.horizontalLayout_33 = QHBoxLayout(self.emloyeeHeader)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, 0, 0, 0)
        self.widget_26 = QWidget(self.emloyeeHeader)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMinimumSize(QSize(120, 85))
        self.verticalLayout_44 = QVBoxLayout(self.widget_26)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.exitFromEmployeeBtn = QPushButton(self.widget_26)
        self.exitFromEmployeeBtn.setObjectName(u"exitFromEmployeeBtn")
        self.exitFromEmployeeBtn.setMinimumSize(QSize(85, 30))
        self.exitFromEmployeeBtn.setMaximumSize(QSize(85, 30))
        self.exitFromEmployeeBtn.setIcon(icon15)
        self.exitFromEmployeeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_44.addWidget(self.exitFromEmployeeBtn)

        self.label57 = QLabel(self.widget_26)
        self.label57.setObjectName(u"label57")
        self.label57.setMinimumSize(QSize(250, 35))
        self.label57.setMaximumSize(QSize(250, 35))
        font9 = QFont()
        font9.setPointSize(15)
        self.label57.setFont(font9)

        self.verticalLayout_44.addWidget(self.label57)


        self.horizontalLayout_33.addWidget(self.widget_26, 0, Qt.AlignLeft)

        self.widget_43 = QWidget(self.emloyeeHeader)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setMinimumSize(QSize(190, 0))
        self.widget_43.setMaximumSize(QSize(190, 16777215))
        self.verticalLayout_32 = QVBoxLayout(self.widget_43)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.createUserBtn = QPushButton(self.widget_43)
        self.createUserBtn.setObjectName(u"createUserBtn")
        self.createUserBtn.setMinimumSize(QSize(175, 30))
        self.createUserBtn.setMaximumSize(QSize(175, 30))
        self.createUserBtn.setIcon(icon5)
        self.createUserBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_32.addWidget(self.createUserBtn)


        self.horizontalLayout_33.addWidget(self.widget_43, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_28 = QWidget(self.emloyeeHeader)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(150, 70))
        self.widget_28.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_45 = QVBoxLayout(self.widget_28)
        self.verticalLayout_45.setSpacing(3)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.employeeStatus = QLabel(self.widget_28)
        self.employeeStatus.setObjectName(u"employeeStatus")
        self.employeeStatus.setMinimumSize(QSize(0, 35))
        self.employeeStatus.setMaximumSize(QSize(16777215, 35))
        self.employeeStatus.setFont(font2)

        self.verticalLayout_45.addWidget(self.employeeStatus, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.is_userLabel = QLabel(self.widget_28)
        self.is_userLabel.setObjectName(u"is_userLabel")
        self.is_userLabel.setMinimumSize(QSize(0, 25))
        self.is_userLabel.setMaximumSize(QSize(80, 25))

        self.verticalLayout_45.addWidget(self.is_userLabel, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout_33.addWidget(self.widget_28, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_41.addWidget(self.emloyeeHeader, 0, Qt.AlignTop)

        self.employeeInfo = QWidget(self.employeePage)
        self.employeeInfo.setObjectName(u"employeeInfo")
        self.verticalLayout_46 = QVBoxLayout(self.employeeInfo)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 5, 0, 5)
        self.employeeScrollArea = QScrollArea(self.employeeInfo)
        self.employeeScrollArea.setObjectName(u"employeeScrollArea")
        self.employeeScrollArea.setWidgetResizable(True)
        self.employeeScrollAreaWidgetContents = QWidget()
        self.employeeScrollAreaWidgetContents.setObjectName(u"employeeScrollAreaWidgetContents")
        self.employeeScrollAreaWidgetContents.setGeometry(QRect(0, 0, 930, 487))
        self.verticalLayout_48 = QVBoxLayout(self.employeeScrollAreaWidgetContents)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.employeeVerticalLayout = QVBoxLayout()
        self.employeeVerticalLayout.setObjectName(u"employeeVerticalLayout")
        self.widget_27 = QWidget(self.employeeScrollAreaWidgetContents)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.widget_29 = QWidget(self.widget_27)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMinimumSize(QSize(345, 0))
        self.horizontalLayout_36 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_21 = QLabel(self.widget_29)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(70, 0))
        self.label_21.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_36.addWidget(self.label_21)

        self.employeeNameLineEdit = QLineEdit(self.widget_29)
        self.employeeNameLineEdit.setObjectName(u"employeeNameLineEdit")
        self.employeeNameLineEdit.setMinimumSize(QSize(250, 25))
        self.employeeNameLineEdit.setMaximumSize(QSize(250, 25))

        self.horizontalLayout_36.addWidget(self.employeeNameLineEdit)


        self.horizontalLayout_35.addWidget(self.widget_29, 0, Qt.AlignLeft)

        self.widget_30 = QWidget(self.widget_27)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMinimumSize(QSize(240, 0))
        self.horizontalLayout_37 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label58 = QLabel(self.widget_30)
        self.label58.setObjectName(u"label58")
        self.label58.setMinimumSize(QSize(75, 25))
        self.label58.setMaximumSize(QSize(75, 25))

        self.horizontalLayout_37.addWidget(self.label58)

        self.employeePositionComboBox = QComboBox(self.widget_30)
        self.employeePositionComboBox.setObjectName(u"employeePositionComboBox")
        self.employeePositionComboBox.setMinimumSize(QSize(140, 25))
        self.employeePositionComboBox.setMaximumSize(QSize(140, 25))

        self.horizontalLayout_37.addWidget(self.employeePositionComboBox)


        self.horizontalLayout_35.addWidget(self.widget_30, 0, Qt.AlignRight)


        self.employeeVerticalLayout.addWidget(self.widget_27, 0, Qt.AlignTop)

        self.widget_31 = QWidget(self.employeeScrollAreaWidgetContents)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMinimumSize(QSize(345, 0))
        self.horizontalLayout_38 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_22 = QLabel(self.widget_31)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(70, 25))
        self.label_22.setMaximumSize(QSize(70, 25))

        self.horizontalLayout_38.addWidget(self.label_22)

        self.employeeEmailLineEdit = QLineEdit(self.widget_31)
        self.employeeEmailLineEdit.setObjectName(u"employeeEmailLineEdit")
        self.employeeEmailLineEdit.setMinimumSize(QSize(250, 25))
        self.employeeEmailLineEdit.setMaximumSize(QSize(250, 25))

        self.horizontalLayout_38.addWidget(self.employeeEmailLineEdit)


        self.employeeVerticalLayout.addWidget(self.widget_31, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_32 = QWidget(self.employeeScrollAreaWidgetContents)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMinimumSize(QSize(345, 0))
        self.horizontalLayout_39 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_23 = QLabel(self.widget_32)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(70, 25))
        self.label_23.setMaximumSize(QSize(70, 25))

        self.horizontalLayout_39.addWidget(self.label_23)

        self.employeePhoneLineEdit = QLineEdit(self.widget_32)
        self.employeePhoneLineEdit.setObjectName(u"employeePhoneLineEdit")
        self.employeePhoneLineEdit.setMinimumSize(QSize(250, 25))
        self.employeePhoneLineEdit.setMaximumSize(QSize(250, 25))

        self.horizontalLayout_39.addWidget(self.employeePhoneLineEdit)


        self.employeeVerticalLayout.addWidget(self.widget_32, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_33 = QWidget(self.employeeScrollAreaWidgetContents)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_40 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_24 = QLabel(self.widget_33)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(70, 25))
        self.label_24.setMaximumSize(QSize(70, 25))

        self.horizontalLayout_40.addWidget(self.label_24)

        self.dateStart = QLabel(self.widget_33)
        self.dateStart.setObjectName(u"dateStart")
        self.dateStart.setMinimumSize(QSize(90, 25))
        self.dateStart.setMaximumSize(QSize(90, 25))

        self.horizontalLayout_40.addWidget(self.dateStart)

        self.label_26 = QLabel(self.widget_33)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(70, 25))
        self.label_26.setMaximumSize(QSize(70, 25))

        self.horizontalLayout_40.addWidget(self.label_26, 0, Qt.AlignLeft)

        self.dateFire = QLabel(self.widget_33)
        self.dateFire.setObjectName(u"dateFire")
        self.dateFire.setMinimumSize(QSize(90, 25))
        self.dateFire.setMaximumSize(QSize(90, 25))

        self.horizontalLayout_40.addWidget(self.dateFire)


        self.employeeVerticalLayout.addWidget(self.widget_33, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_34 = QWidget(self.employeeScrollAreaWidgetContents)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setMinimumSize(QSize(100, 0))
        self.horizontalLayout_41 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_28 = QLabel(self.widget_34)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(75, 0))
        self.label_28.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_41.addWidget(self.label_28)

        self.workedInCompany = QLabel(self.widget_34)
        self.workedInCompany.setObjectName(u"workedInCompany")
        self.workedInCompany.setMinimumSize(QSize(100, 25))
        self.workedInCompany.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_41.addWidget(self.workedInCompany)


        self.employeeVerticalLayout.addWidget(self.widget_34, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_35 = QWidget(self.employeeScrollAreaWidgetContents)
        self.widget_35.setObjectName(u"widget_35")
        self.verticalLayout_47 = QVBoxLayout(self.widget_35)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label59 = QLabel(self.widget_35)
        self.label59.setObjectName(u"label59")

        self.verticalLayout_47.addWidget(self.label59)

        self.skillsTextEdit = QTextEdit(self.widget_35)
        self.skillsTextEdit.setObjectName(u"skillsTextEdit")
        self.skillsTextEdit.setMinimumSize(QSize(340, 200))
        self.skillsTextEdit.setMaximumSize(QSize(340, 500))

        self.verticalLayout_47.addWidget(self.skillsTextEdit)


        self.employeeVerticalLayout.addWidget(self.widget_35)


        self.verticalLayout_48.addLayout(self.employeeVerticalLayout)

        self.employeeScrollArea.setWidget(self.employeeScrollAreaWidgetContents)

        self.verticalLayout_46.addWidget(self.employeeScrollArea)


        self.verticalLayout_41.addWidget(self.employeeInfo)

        self.employeeBottom = QWidget(self.employeePage)
        self.employeeBottom.setObjectName(u"employeeBottom")
        self.horizontalLayout_34 = QHBoxLayout(self.employeeBottom)
        self.horizontalLayout_34.setSpacing(5)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 7, 0, 0)
        self.widget_5 = QWidget(self.employeeBottom)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(120, 0))
        self.verticalLayout_15 = QVBoxLayout(self.widget_5)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.esaveChangesBtn = QPushButton(self.widget_5)
        self.esaveChangesBtn.setObjectName(u"esaveChangesBtn")
        self.esaveChangesBtn.setMinimumSize(QSize(110, 30))
        self.esaveChangesBtn.setMaximumSize(QSize(110, 30))
        icon21 = QIcon()
        icon21.addFile(u":/feather/icons/feather/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.esaveChangesBtn.setIcon(icon21)
        self.esaveChangesBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_15.addWidget(self.esaveChangesBtn)


        self.horizontalLayout_34.addWidget(self.widget_5, 0, Qt.AlignLeft)

        self.widget_6 = QWidget(self.employeeBottom)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(350, 0))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.firedBtn = QPushButton(self.widget_6)
        self.firedBtn.setObjectName(u"firedBtn")
        self.firedBtn.setMinimumSize(QSize(110, 30))
        self.firedBtn.setMaximumSize(QSize(110, 30))
        self.firedBtn.setIcon(icon18)
        self.firedBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.firedBtn)

        self.vacationBtn = QPushButton(self.widget_6)
        self.vacationBtn.setObjectName(u"vacationBtn")
        self.vacationBtn.setMinimumSize(QSize(110, 30))
        self.vacationBtn.setMaximumSize(QSize(110, 30))
        icon22 = QIcon()
        icon22.addFile(u":/feather/icons/feather/map.png", QSize(), QIcon.Normal, QIcon.Off)
        self.vacationBtn.setIcon(icon22)
        self.vacationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.vacationBtn)

        self.workingBtn = QPushButton(self.widget_6)
        self.workingBtn.setObjectName(u"workingBtn")
        self.workingBtn.setMinimumSize(QSize(110, 30))
        self.workingBtn.setMaximumSize(QSize(110, 30))
        self.workingBtn.setIcon(icon19)
        self.workingBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.workingBtn)


        self.horizontalLayout_34.addWidget(self.widget_6, 0, Qt.AlignRight)


        self.verticalLayout_41.addWidget(self.employeeBottom, 0, Qt.AlignBottom)

        self.mainPages.addWidget(self.employeePage)
        self.helloPage = QWidget()
        self.helloPage.setObjectName(u"helloPage")
        self.verticalLayout_16 = QVBoxLayout(self.helloPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_41 = QWidget(self.helloPage)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_31 = QVBoxLayout(self.widget_41)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label91 = QLabel(self.widget_41)
        self.label91.setObjectName(u"label91")
        self.label91.setFont(font8)

        self.verticalLayout_31.addWidget(self.label91)


        self.verticalLayout_16.addWidget(self.widget_41, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mainPages.addWidget(self.helloPage)
        self.questionnaryPage = QWidget()
        self.questionnaryPage.setObjectName(u"questionnaryPage")
        self.verticalLayout_25 = QVBoxLayout(self.questionnaryPage)
        self.verticalLayout_25.setSpacing(2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.questionnaryHead = QWidget(self.questionnaryPage)
        self.questionnaryHead.setObjectName(u"questionnaryHead")
        self.questionnaryHead.setMinimumSize(QSize(350, 0))
        self.questionnaryHead.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_26 = QVBoxLayout(self.questionnaryHead)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.exitFromQuestionBtn = QPushButton(self.questionnaryHead)
        self.exitFromQuestionBtn.setObjectName(u"exitFromQuestionBtn")
        self.exitFromQuestionBtn.setMinimumSize(QSize(85, 30))
        self.exitFromQuestionBtn.setMaximumSize(QSize(85, 30))
        self.exitFromQuestionBtn.setIcon(icon15)
        self.exitFromQuestionBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.exitFromQuestionBtn, 0, Qt.AlignLeft)

        self.questionnaryNameLabel = QLabel(self.questionnaryHead)
        self.questionnaryNameLabel.setObjectName(u"questionnaryNameLabel")
        self.questionnaryNameLabel.setMinimumSize(QSize(350, 25))
        self.questionnaryNameLabel.setMaximumSize(QSize(350, 25))
        self.questionnaryNameLabel.setFont(font1)

        self.verticalLayout_26.addWidget(self.questionnaryNameLabel)


        self.verticalLayout_25.addWidget(self.questionnaryHead, 0, Qt.AlignTop)

        self.questionContentWidget = QWidget(self.questionnaryPage)
        self.questionContentWidget.setObjectName(u"questionContentWidget")
        self.verticalLayout_27 = QVBoxLayout(self.questionContentWidget)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(5, 5, 5, 5)
        self.questionsScrollArea = QScrollArea(self.questionContentWidget)
        self.questionsScrollArea.setObjectName(u"questionsScrollArea")
        self.questionsScrollArea.setWidgetResizable(True)
        self.questionsScrollAreaWidgetContents = QWidget()
        self.questionsScrollAreaWidgetContents.setObjectName(u"questionsScrollAreaWidgetContents")
        self.questionsScrollAreaWidgetContents.setGeometry(QRect(0, 0, 376, 347))
        self.verticalLayout_29 = QVBoxLayout(self.questionsScrollAreaWidgetContents)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.questionsVerticalLayout = QVBoxLayout()
        self.questionsVerticalLayout.setSpacing(3)
        self.questionsVerticalLayout.setObjectName(u"questionsVerticalLayout")
        self.questionsVerticalLayout.setContentsMargins(5, -1, -1, -1)
        self.label11 = QLabel(self.questionsScrollAreaWidgetContents)
        self.label11.setObjectName(u"label11")
        self.label11.setMinimumSize(QSize(0, 25))
        self.label11.setMaximumSize(QSize(16777215, 25))
        self.label11.setFont(font5)

        self.questionsVerticalLayout.addWidget(self.label11, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_7 = QWidget(self.questionsScrollAreaWidgetContents)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 45))
        self.widget_7.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(120, 0))
        self.label_10.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_14.addWidget(self.label_10)

        self.cNameLineEdit = QLineEdit(self.widget_7)
        self.cNameLineEdit.setObjectName(u"cNameLineEdit")
        self.cNameLineEdit.setMinimumSize(QSize(250, 0))
        self.cNameLineEdit.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_14.addWidget(self.cNameLineEdit)


        self.questionsVerticalLayout.addWidget(self.widget_7, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_8 = QWidget(self.questionsScrollAreaWidgetContents)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 45))
        self.widget_8.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label6 = QLabel(self.widget_8)
        self.label6.setObjectName(u"label6")
        self.label6.setMinimumSize(QSize(120, 0))
        self.label6.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_17.addWidget(self.label6)

        self.cSernameLineEdit = QLineEdit(self.widget_8)
        self.cSernameLineEdit.setObjectName(u"cSernameLineEdit")
        self.cSernameLineEdit.setMinimumSize(QSize(250, 0))
        self.cSernameLineEdit.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_17.addWidget(self.cSernameLineEdit)


        self.questionsVerticalLayout.addWidget(self.widget_8, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_9 = QWidget(self.questionsScrollAreaWidgetContents)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 45))
        self.widget_9.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(120, 0))
        self.label_13.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_16.addWidget(self.label_13)

        self.cPatronimicLineEdit = QLineEdit(self.widget_9)
        self.cPatronimicLineEdit.setObjectName(u"cPatronimicLineEdit")
        self.cPatronimicLineEdit.setMinimumSize(QSize(250, 0))
        self.cPatronimicLineEdit.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_16.addWidget(self.cPatronimicLineEdit)


        self.questionsVerticalLayout.addWidget(self.widget_9, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_10 = QWidget(self.questionsScrollAreaWidgetContents)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 45))
        self.widget_10.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(120, 0))
        self.label_14.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_15.addWidget(self.label_14)

        self.cEmailLineEdit = QLineEdit(self.widget_10)
        self.cEmailLineEdit.setObjectName(u"cEmailLineEdit")
        self.cEmailLineEdit.setMinimumSize(QSize(250, 0))
        self.cEmailLineEdit.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_15.addWidget(self.cEmailLineEdit)


        self.questionsVerticalLayout.addWidget(self.widget_10, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_11 = QWidget(self.questionsScrollAreaWidgetContents)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 45))
        self.widget_11.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.widget_11)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(120, 0))
        self.label_15.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_18.addWidget(self.label_15)

        self.cPhoneLineEdit = QLineEdit(self.widget_11)
        self.cPhoneLineEdit.setObjectName(u"cPhoneLineEdit")
        self.cPhoneLineEdit.setMinimumSize(QSize(250, 0))
        self.cPhoneLineEdit.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_18.addWidget(self.cPhoneLineEdit)


        self.questionsVerticalLayout.addWidget(self.widget_11, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_12 = QWidget(self.questionsScrollAreaWidgetContents)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 45))
        self.widget_12.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_19 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget_12)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(120, 0))
        self.label_16.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_19.addWidget(self.label_16)

        self.cLinkLineEdit = QLineEdit(self.widget_12)
        self.cLinkLineEdit.setObjectName(u"cLinkLineEdit")
        self.cLinkLineEdit.setMinimumSize(QSize(250, 0))
        self.cLinkLineEdit.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_19.addWidget(self.cLinkLineEdit)


        self.questionsVerticalLayout.addWidget(self.widget_12, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_17 = QLabel(self.questionsScrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(110, 26))
        self.label_17.setMaximumSize(QSize(110, 26))
        self.label_17.setFont(font5)

        self.questionsVerticalLayout.addWidget(self.label_17)

        self.questionsBlock = QWidget(self.questionsScrollAreaWidgetContents)
        self.questionsBlock.setObjectName(u"questionsBlock")
        self.verticalLayout_30 = QVBoxLayout(self.questionsBlock)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)

        self.questionsVerticalLayout.addWidget(self.questionsBlock, 0, Qt.AlignTop)


        self.verticalLayout_29.addLayout(self.questionsVerticalLayout)

        self.questionsScrollArea.setWidget(self.questionsScrollAreaWidgetContents)

        self.verticalLayout_27.addWidget(self.questionsScrollArea)


        self.verticalLayout_25.addWidget(self.questionContentWidget)

        self.questionnaryBottom = QWidget(self.questionnaryPage)
        self.questionnaryBottom.setObjectName(u"questionnaryBottom")
        self.questionnaryBottom.setMinimumSize(QSize(120, 35))
        self.questionnaryBottom.setMaximumSize(QSize(120, 35))
        self.verticalLayout_28 = QVBoxLayout(self.questionnaryBottom)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.saveQuestionsBtn = QPushButton(self.questionnaryBottom)
        self.saveQuestionsBtn.setObjectName(u"saveQuestionsBtn")
        self.saveQuestionsBtn.setMinimumSize(QSize(110, 30))
        self.saveQuestionsBtn.setMaximumSize(QSize(110, 30))
        self.saveQuestionsBtn.setIcon(icon21)
        self.saveQuestionsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_28.addWidget(self.saveQuestionsBtn, 0, Qt.AlignRight)


        self.verticalLayout_25.addWidget(self.questionnaryBottom, 0, Qt.AlignRight|Qt.AlignBottom)

        self.mainPages.addWidget(self.questionnaryPage)

        self.verticalLayout_11.addWidget(self.mainPages)


        self.horizontalLayout_9.addWidget(self.mainPageCont)


        self.verticalLayout_10.addWidget(self.mainContents)

        self.footer = QWidget(self.mainBody)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 0, 0)
        self.sizeGrip = QFrame(self.footer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(30)
        sizePolicy2.setVerticalStretch(30)
        sizePolicy2.setHeightForWidth(self.sizeGrip.sizePolicy().hasHeightForWidth())
        self.sizeGrip.setSizePolicy(sizePolicy2)
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(15, 15))
        self.sizeGrip.setStyleSheet(u"")
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.sizeGrip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_10.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.reportsBtn.setDefault(False)
        self.centerMenuPages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.questionsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u043a\u0435\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.questionsBtn.setText(QCoreApplication.translate("MainWindow", u"   \u0410\u043d\u043a\u0435\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
#if QT_CONFIG(tooltip)
        self.reportsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u044b", None))
#endif // QT_CONFIG(tooltip)
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u"   \u041e\u0442\u0447\u0435\u0442\u044b", None))
#if QT_CONFIG(tooltip)
        self.workersBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.workersBtn.setText(QCoreApplication.translate("MainWindow", u"   \u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
#if QT_CONFIG(tooltip)
        self.analysisBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0441\u0432\u043e\u0434\u043a\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.analysisBtn.setText(QCoreApplication.translate("MainWindow", u"   \u0410\u043d\u0430\u043b\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0441\u0432\u043e\u0434\u043a\u0430", None))
#if QT_CONFIG(tooltip)
        self.prifileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.prifileBtn.setText(QCoreApplication.translate("MainWindow", u"   \u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"   \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"   \u041f\u043e\u043c\u043e\u0449\u044c", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"   \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
#if QT_CONFIG(tooltip)
        self.closeLeftMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.closeLeftMenuBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\" bgcolor=\"transparent\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0415\u0441\u043b\u0438 \u0443 \u0432\u0430\u0441 \u0432\u043e\u0437\u043d\u0438\u043a\u043b\u0438 \u0432\u043e\u043f\u0440\u043e\u0441\u044b, \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u0438 \u0438\u043b\u0438 \u043d\u0435\u043f\u043e\u043b\u0430\u0434\u043a\u0438 \u043f\u0440\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0438 \u0441\u0435"
                        "\u0440\u0432\u0438\u0441\u0430, \u043f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u043e\u0431\u0440\u0430\u0442\u0438\u0442\u0435\u0441\u044c \u0432 \u043d\u0430\u0448\u0443 \u0441\u043b\u0443\u0436\u0431\u0443 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0438. \u041c\u044b \u043f\u043e\u0441\u0442\u0430\u0440\u0430\u0435\u043c\u0441\u044f \u043f\u043e\u043c\u043e\u0447\u044c \u0432\u0430\u043c \u043a\u0430\u043a \u043c\u043e\u0436\u043d\u043e \u0441\u043a\u043e\u0440\u0435\u0435.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u042d"
                        "\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430: abramtsovav@ya.ru</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0435\u043b\u0435\u0444\u043e\u043d: +7 (988) 169-04-42</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0435\u0440\u0435\u0434 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u0435\u043c \u0443\u0442\u043e\u0447\u043d\u0438\u0442\u0435:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2014 \u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u044b</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; m"
                        "argin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2014 \u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043f\u0440\u0438\u0432\u0435\u043b\u0438 \u043a \u043e\u0448\u0438\u0431\u043a\u0435</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u2014 \u0421\u043a\u0440\u0438\u043d\u0448\u043e\u0442\u044b (\u0435\u0441\u043b\u0438 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041c\u044b \u0446\u0435\u043d\u0438\u043c \u0432\u0430\u0448\u0435 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u0435 \u0438 \u043f\u043e\u0441\u0442\u0430\u0440\u0430\u0435\u043c\u0441\u044f \u0440\u0435"
                        "\u0448\u0438\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441 \u0432 \u043a\u0440\u0430\u0442\u0447\u0430\u0439\u0448\u0438\u0435 \u0441\u0440\u043e\u043a\u0438.</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u00abHiHire\u00bb \u2014 \u0441\u0438\u0441\u0442\u0435\u043c\u0430 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0438 \u043f\u0440\u0438\u043d\u044f\u0442\u0438\u044f \u0440\u0435\u0448\u0435\u043d\u0438\u0439 \u0434\u043b\u044f HR-\u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441"
                        "\u0442\u0430</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u0435\u0440\u0441\u0438\u044f: 1.0<br />\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u0443\u0441\u043a\u0430: \u043c\u0430\u0439 2025</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e \u0432 \u0440\u0430\u043c\u043a\u0430\u0445 \u0434\u0438\u043f\u043b\u043e\u043c\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0435\u043a\u0442\u0430 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u043a\u043e\u0439 \u0433\u0440\u0443\u043f\u043f\u044b 43\u0418\u0421-21<br /><span style=\" font-weight:700;\">\u0410\u0431\u0440\u0430\u043c\u0446\u043e\u0432\u043e\u0439 \u0412\u0438\u043e\u043b\u0435\u0442\u0442\u043e\u0439 \u0412\u0438\u0442\u0430\u043b\u044c\u0435\u0432\u043d\u043e"
                        "\u0439</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c \u043f\u0440\u043e\u0435\u043a\u0442\u0430: <span style=\" font-weight:700;\">\u0413\u0430\u0432\u0440\u0438\u043b\u043e\u0432\u0430 \u041b.\u0410.</span><br />\u041e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0443\u0447\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0435: <span style=\" font-weight:700;\">\u0420\u0410\u041d\u0425\u0438\u0413\u0421, \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c 09.02.07 \u00ab\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u044b \u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435\u00bb</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; mar"
                        "gin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0426\u0435\u043b\u044c \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u2014 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0437\u0430\u0446\u0438\u044f \u0430\u043d\u043a\u0435\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u043e\u0432, \u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u0438 \u0430\u043d\u0430\u043b\u0438\u0437 \u0434\u0430\u043d\u043d\u044b\u0445 \u0441\u043e\u0431\u0435\u0441\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0439, \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0431\u0430\u0437\u043e\u0439 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432 \u0438 \u043a\u0430\u0434\u0440\u043e\u0432\u044b\u043c \u0440\u0435\u0437\u0435\u0440\u0432\u043e\u043c.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u0430\u0432\u043e\u043e\u0431\u043b\u0430"
                        "\u0434\u0430\u0442\u0435\u043b\u044c: \u041e\u041e\u041e \u00ab\u0411\u043e\u043b\u044c\u0448\u0430\u044f \u0422\u0440\u043e\u0439\u043a\u0430\u00bb</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u0441\u0435 \u043f\u0440\u0430\u0432\u0430 \u0437\u0430\u0449\u0438\u0449\u0435\u043d\u044b. \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0438 \u0440\u0430\u0441\u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0432\u043d\u0435 \u0443\u0447\u0435\u0431\u043d\u044b\u0445 \u0438 \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0445 \u043d\u0443\u0436\u0434 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438 \u0431\u0435\u0437 \u0441\u043e\u0433\u043b\u0430\u0441\u0438\u044f \u043f\u0440\u0430\u0432\u043e\u043e\u0431\u043b\u0430\u0434\u0430\u0442\u0435\u043b\u044f \u0437\u0430\u043f\u0440\u0435"
                        "\u0449\u0435\u043d\u043e.</p></body></html>", None))
        self.logoPic.setText("")
        self.logoName.setText(QCoreApplication.translate("MainWindow", u"HiHire B3", None))
#if QT_CONFIG(tooltip)
        self.wrapBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0440\u043d\u0443\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.wrapBtn.setText("")
#if QT_CONFIG(tooltip)
        self.changeWinBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0440\u0430\u0437\u043c\u0435\u0440", None))
#endif // QT_CONFIG(tooltip)
        self.changeWinBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label60.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0431\u043b\u043e\u043d \u0430\u043d\u043a\u0435\u0442\u044b", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u0441 ", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u" \u043f\u043e", None))
        self.clabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442", None))
        self.dlabel.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0438\u043d\u0442\u0435\u0440\u0432\u044c\u044e", None))
        self.stlabel.setText(QCoreApplication.translate("MainWindow", u"\u0441", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e", None))
        self.exportBtn.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.importBtn.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.slabel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label60_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e \u0431\u0430\u043b\u043b\u0430\u043c", None))
        self.exitFromCandidateBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.candidateLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0430\u0442\u0443\u0441\u0430", None))
        self.candidateFIOLabel.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u0430", None))
        self.llabel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0440\u0435\u0437\u044e\u043c\u0435:", None))
        self.linkLabel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0441\u044b\u043b\u043a\u0430", None))
        self.label110.setText(QCoreApplication.translate("MainWindow", u"Email: ", None))
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0447\u0442\u0430", None))
        self.label52.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.positionName.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.label53.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:", None))
        self.scoreLabel.setText(QCoreApplication.translate("MainWindow", u"20 \u0438\u0437 35", None))
        self.recommendationText.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u044f: ", None))
        self.questionnaryName.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.rejectBtn.setText(QCoreApplication.translate("MainWindow", u" \u041e\u0442\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.acceptBtn.setText(QCoreApplication.translate("MainWindow", u" \u041f\u0440\u0438\u0433\u043b\u0430\u0441\u0438\u0442\u044c", None))
        self.disagreeBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0430\u0437", None))
        self.agreeBtn.setText(QCoreApplication.translate("MainWindow", u" \u041f\u0440\u0438\u043d\u044f\u0442\u044c", None))
        self.addQuestionaryBtn.setText(QCoreApplication.translate("MainWindow", u"  \u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.labelSys.setText(QCoreApplication.translate("MainWindow", u"C\u0438\u0441\u0442\u0435\u043c\u043d\u044b\u0435 \u0448\u0430\u0431\u043b\u043e\u043d\u044b", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a", None))
        self.label3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441. \u0431\u0430\u043b\u043b\u043e\u0432: 19", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044d\u043a-\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a", None))
        self.label4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441. \u0431\u0430\u043b\u043b\u043e\u0432: 31", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0440\u043e\u043d\u0442-\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441. \u0431\u0430\u043b\u043b\u043e\u0432: 15", None))
#if QT_CONFIG(tooltip)
        self.labelUser.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0431\u043e\u043b\u0435\u0435 3", None))
#endif // QT_CONFIG(tooltip)
        self.labelUser.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0435 \u0448\u0430\u0431\u043b\u043e\u043d\u044b", None))
        self.label54.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label55.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label56.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e \u0434\u0430\u0442\u0435 \u043f\u0440\u0438\u0451\u043c\u0430", None))
        self.exitFromEmployeeBtn.setText(QCoreApplication.translate("MainWindow", u" \u041d\u0430\u0437\u0430\u0434", None))
        self.label57.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a", None))
        self.createUserBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.employeeStatus.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.is_userLabel.setText(QCoreApplication.translate("MainWindow", u"hr-\u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None))
        self.label58.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430\u0435\u0442 \u0441", None))
        self.dateStart.setText(QCoreApplication.translate("MainWindow", u"\u0434\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u043e\u043b\u0435\u043d", None))
        self.dateFire.setText(QCoreApplication.translate("MainWindow", u"\u0434\u0430\u0442\u0430 \u0443\u0432\u043e\u043b\u044c\u043d\u0435\u043d\u0438\u044f", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.workedInCompany.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442 \u0441 \u0434\u0430\u0442\u044b \u043f\u0440\u0438\u0435\u043c\u0430", None))
        self.label59.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0432\u044b\u043a\u0438", None))
        self.esaveChangesBtn.setText(QCoreApplication.translate("MainWindow", u" \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.firedBtn.setText(QCoreApplication.translate("MainWindow", u" \u0423\u0432\u043e\u043b\u0435\u043d", None))
        self.vacationBtn.setText(QCoreApplication.translate("MainWindow", u" \u0412 \u043e\u0442\u043f\u0443\u0441\u043a\u0435", None))
        self.workingBtn.setText(QCoreApplication.translate("MainWindow", u" \u0420\u0430\u0431\u043e\u0442\u0430\u0435\u0442", None))
        self.label91.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c!", None))
        self.exitFromQuestionBtn.setText(QCoreApplication.translate("MainWindow", u"  \u0412\u044b\u0439\u0442\u0438", None))
        self.questionnaryNameLabel.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0430\u043d\u043a\u0435\u0442\u044b", None))
        self.label11.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.label6.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e*", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0440\u0435\u0437\u044e\u043c\u0435", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u0432\u044c\u044e", None))
        self.saveQuestionsBtn.setText(QCoreApplication.translate("MainWindow", u"  \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

