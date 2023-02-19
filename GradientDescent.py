# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GradientDescent.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setStyleSheet(u"background-color: rgb(255, 248, 214)")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 221, 31))
        font = QFont()
        font.setFamilies([u"Georgia"])
        font.setPointSize(24)
        self.label.setFont(font)
        self.featureslineEdit = QLineEdit(Form)
        self.featureslineEdit.setObjectName(u"featureslineEdit")
        self.featureslineEdit.setGeometry(QRect(70, 80, 241, 21))
        self.targetlineEdit = QLineEdit(Form)
        self.targetlineEdit.setObjectName(u"targetlineEdit")
        self.targetlineEdit.setGeometry(QRect(70, 120, 241, 21))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 58, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 58, 16))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 170, 151, 16))
        self.inputlineEdit = QLineEdit(Form)
        self.inputlineEdit.setObjectName(u"inputlineEdit")
        self.inputlineEdit.setGeometry(QRect(70, 210, 151, 21))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 210, 58, 16))
        self.predictButton = QPushButton(Form)
        self.predictButton.setObjectName(u"predictButton")
        self.predictButton.setGeometry(QRect(260, 200, 100, 32))
        self.predictButton.setStyleSheet(u"background-color:rgb(154, 192, 135)")
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 150, 371, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.resultLabel = QLabel(Form)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setGeometry(QRect(10, 260, 351, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Linear Regression", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"features", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"target", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"output prediction", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"input", None))
        self.predictButton.setText(QCoreApplication.translate("Form", u"predict", None))
        self.resultLabel.setText(QCoreApplication.translate("Form", u"Result: ", None))
    # retranslateUi

