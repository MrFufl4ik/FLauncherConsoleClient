# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 400)
        Form.setMinimumSize(QSize(900, 400))
        Form.setMaximumSize(QSize(900, 400))
        Form.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255)\n"
"}")
        self.btnSendConsoleCommand = QPushButton(Form)
        self.btnSendConsoleCommand.setObjectName(u"btnSendConsoleCommand")
        self.btnSendConsoleCommand.setGeometry(QRect(740, 350, 151, 41))
        font = QFont()
        font.setFamilies([u"JetBrains Mono Medium"])
        font.setPointSize(14)
        self.btnSendConsoleCommand.setFont(font)
        self.btnSendConsoleCommand.setStyleSheet(u"QPushButton {\n"
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
        self.inputConsoleCommand = QLineEdit(Form)
        self.inputConsoleCommand.setObjectName(u"inputConsoleCommand")
        self.inputConsoleCommand.setGeometry(QRect(10, 350, 721, 41))
        self.inputConsoleCommand.setFont(font)
        self.inputConsoleCommand.setAutoFillBackground(False)
        self.inputConsoleCommand.setStyleSheet(u"QLineEdit {\n"
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
        self.textEditConsoleLog = QTextEdit(Form)
        self.textEditConsoleLog.setObjectName(u"textEditConsoleLog")
        self.textEditConsoleLog.setGeometry(QRect(10, 10, 881, 331))
        font1 = QFont()
        font1.setFamilies([u"JetBrains Mono Medium"])
        font1.setPointSize(11)
        self.textEditConsoleLog.setFont(font1)
        self.textEditConsoleLog.setStyleSheet(u"QTextEdit {\n"
"    color: white;\n"
"    background: rgb(0,0,0);\n"
"    border: 1px solid #333;\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"QTextEdit QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #1a1a1a;\n"
"    width: 12px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QTextEdit QScrollBar::handle:vertical {\n"
"    background: #333;\n"
"    min-height: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QTextEdit QScrollBar::add-line:vertical, \n"
"QTextEdit QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    height: 0;\n"
"}\n"
"\n"
"QTextEdit QScrollBar::add-page:vertical, \n"
"QTextEdit QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0433\u043e\u0440\u0438\u0437\u043e"
                        "\u043d\u0442\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 (\u0430\u043d\u0430\u043b\u043e\u0433\u0438\u0447\u043d\u044b\u0439) */\n"
"QTextEdit QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #1a1a1a;\n"
"    height: 12px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QTextEdit QScrollBar::handle:horizontal {\n"
"    background: #333;\n"
"    min-width: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QTextEdit QScrollBar::add-line:horizontal, \n"
"QTextEdit QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"    width: 0;\n"
"}\n"
"\n"
"QTextEdit QScrollBar::add-page:horizontal, \n"
"QTextEdit QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}")
        self.textEditConsoleLog.setReadOnly(True)
        self.textEditConsoleLog.setOverwriteMode(False)
        self.textEditConsoleLog.setAcceptRichText(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"FLauncherConsole", None))
        self.btnSendConsoleCommand.setText(QCoreApplication.translate("Form", u"send", None))
#if QT_CONFIG(shortcut)
        self.btnSendConsoleCommand.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.inputConsoleCommand.setPlaceholderText(QCoreApplication.translate("Form", u"give mrfufl4ik minecraft:diamond 64", None))
        self.textEditConsoleLog.setMarkdown("")
        self.textEditConsoleLog.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'JetBrains Mono Medium'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEditConsoleLog.setPlaceholderText("")
    # retranslateUi

