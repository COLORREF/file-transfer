# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileDownload.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, LineEdit, ProgressBar,
    SimpleCardWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(374, 159)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.SimpleCardWidget = SimpleCardWidget(Form)
        self.SimpleCardWidget.setObjectName(u"SimpleCardWidget")
        self.verticalLayout = QVBoxLayout(self.SimpleCardWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.SimpleCardWidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.urlEdit = LineEdit(self.widget)
        self.urlEdit.setObjectName(u"urlEdit")

        self.gridLayout_2.addWidget(self.urlEdit, 1, 1, 1, 1)

        self.BodyLabel_3 = BodyLabel(self.widget)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.gridLayout_2.addWidget(self.BodyLabel_3, 3, 0, 1, 1)

        self.BodyLabel_2 = BodyLabel(self.widget)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.gridLayout_2.addWidget(self.BodyLabel_2, 2, 0, 1, 1)

        self.savePathEdit = LineEdit(self.widget)
        self.savePathEdit.setObjectName(u"savePathEdit")

        self.gridLayout_2.addWidget(self.savePathEdit, 2, 1, 1, 1)

        self.ProgressBar = ProgressBar(self.widget)
        self.ProgressBar.setObjectName(u"ProgressBar")

        self.gridLayout_2.addWidget(self.ProgressBar, 3, 1, 1, 1)

        self.BodyLabel = BodyLabel(self.widget)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.gridLayout_2.addWidget(self.BodyLabel, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)


        self.gridLayout.addWidget(self.SimpleCardWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u8fdb\u5ea6", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"URL", None))
    # retranslateUi

