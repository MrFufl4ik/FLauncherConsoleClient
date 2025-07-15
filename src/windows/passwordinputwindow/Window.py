# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password_input_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 110)
        Form.setMinimumSize(QSize(400, 110))
        Form.setMaximumSize(QSize(400, 110))
        self.btnOk = QPushButton(Form)
        self.btnOk.setObjectName(u"btnOk")
        self.btnOk.setGeometry(QRect(10, 60, 381, 41))
        font = QFont()
        font.setFamilies([u"JetBrains Mono Medium"])
        font.setPointSize(14)
        self.btnOk.setFont(font)
        self.btnOk.setStyleSheet(u"QPushButton {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #222;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #333;\n"
"    color: #999;\n"
"}")
        self.inputPassword = QLineEdit(Form)
        self.inputPassword.setObjectName(u"inputPassword")
        self.inputPassword.setGeometry(QRect(10, 10, 381, 41))
        self.inputPassword.setFont(font)
        self.inputPassword.setAutoFillBackground(False)
        self.inputPassword.setStyleSheet(u"QLineEdit {\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    selection-background-color: #444;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #333;\n"
"    color: #999;\n"
"    border: 1px solid #444;\n"
"}")
        self.inputPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"FLauncherConsole", None))
        self.btnOk.setText(QCoreApplication.translate("Form", u"ok", None))
#if QT_CONFIG(shortcut)
        self.btnOk.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.inputPassword.setPlaceholderText(QCoreApplication.translate("Form", u"password", None))
    # retranslateUi

