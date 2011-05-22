# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sun May 22 00:18:26 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
  _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
  _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName(_fromUtf8("MainWindow"))
    MainWindow.resize(710, 598)
    self.centralwidget = QtGui.QWidget(MainWindow)
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
    self.gridLayout_2.setMargin(0)
    self.gridLayout_2.setHorizontalSpacing(0)
    self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
    self.label = QtGui.QLabel(self.centralwidget)
    self.label.setMinimumSize(QtCore.QSize(0, 100))
    self.label.setStyleSheet(_fromUtf8("QLabel {\n"
"  padding: 10px;\n"
"  font-size: 30px;\n"
"  background-color: rgb(103, 152, 203);\n"
"  color: white;\n"
"}"))
    self.label.setObjectName(_fromUtf8("label"))
    self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
    self.contentWidget = QtGui.QStackedWidget(self.centralwidget)
    self.contentWidget.setObjectName(_fromUtf8("contentWidget"))
    self.content1 = QtGui.QWidget()
    self.content1.setObjectName(_fromUtf8("content1"))
    self.gridLayout_3 = QtGui.QGridLayout(self.content1)
    self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
    self.frame_2 = QtGui.QFrame(self.content1)
    self.frame_2.setObjectName(_fromUtf8("frame_2"))
    self.gridLayout_5 = QtGui.QGridLayout(self.frame_2)
    self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
    self.label_2 = QtGui.QLabel(self.frame_2)
    self.label_2.setTextFormat(QtCore.Qt.RichText)
    self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
    self.label_2.setWordWrap(True)
    self.label_2.setObjectName(_fromUtf8("label_2"))
    self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
    self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
    self.contentWidget.addWidget(self.content1)
    self.content2 = QtGui.QWidget()
    self.content2.setObjectName(_fromUtf8("content2"))
    self.gridLayout_4 = QtGui.QGridLayout(self.content2)
    self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
    self.frame_3 = QtGui.QFrame(self.content2)
    self.frame_3.setObjectName(_fromUtf8("frame_3"))
    self.gridLayout_6 = QtGui.QGridLayout(self.frame_3)
    self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
    self.label_3 = QtGui.QLabel(self.frame_3)
    self.label_3.setTextFormat(QtCore.Qt.RichText)
    self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
    self.label_3.setWordWrap(True)
    self.label_3.setObjectName(_fromUtf8("label_3"))
    self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)
    self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1)
    self.contentWidget.addWidget(self.content2)
    self.content3 = QtGui.QWidget()
    self.content3.setObjectName(_fromUtf8("content3"))
    self.gridLayout_8 = QtGui.QGridLayout(self.content3)
    self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
    self.frame_4 = QtGui.QFrame(self.content3)
    self.frame_4.setObjectName(_fromUtf8("frame_4"))
    self.gridLayout_7 = QtGui.QGridLayout(self.frame_4)
    self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
    self.verticalLayout = QtGui.QVBoxLayout()
    self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
    self.label_4 = QtGui.QLabel(self.frame_4)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
    self.label_4.setSizePolicy(sizePolicy)
    self.label_4.setTextFormat(QtCore.Qt.RichText)
    self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
    self.label_4.setWordWrap(True)
    self.label_4.setObjectName(_fromUtf8("label_4"))
    self.verticalLayout.addWidget(self.label_4)
    self.gridLayout_7.addLayout(self.verticalLayout, 0, 0, 1, 1)
    self.partitionList = QtGui.QTreeWidget(self.frame_4)
    self.partitionList.setIndentation(0)
    self.partitionList.setRootIsDecorated(False)
    self.partitionList.setItemsExpandable(False)
    self.partitionList.setAnimated(True)
    self.partitionList.setObjectName(_fromUtf8("partitionList"))
    self.partitionList.header().setCascadingSectionResizes(True)
    self.partitionList.header().setSortIndicatorShown(True)
    self.gridLayout_7.addWidget(self.partitionList, 1, 0, 1, 1)
    self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)
    self.contentWidget.addWidget(self.content3)
    self.content4 = QtGui.QWidget()
    self.content4.setObjectName(_fromUtf8("content4"))
    self.gridLayout_12 = QtGui.QGridLayout(self.content4)
    self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
    self.frame_6 = QtGui.QFrame(self.content4)
    self.frame_6.setObjectName(_fromUtf8("frame_6"))
    self.gridLayout_11 = QtGui.QGridLayout(self.frame_6)
    self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
    self.verticalLayout_2 = QtGui.QVBoxLayout()
    self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
    self.label_6 = QtGui.QLabel(self.frame_6)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
    self.label_6.setSizePolicy(sizePolicy)
    self.label_6.setTextFormat(QtCore.Qt.RichText)
    self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
    self.label_6.setWordWrap(True)
    self.label_6.setObjectName(_fromUtf8("label_6"))
    self.verticalLayout_2.addWidget(self.label_6)
    self.gridLayout_11.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
    self.swapList = QtGui.QTreeWidget(self.frame_6)
    self.swapList.setIndentation(0)
    self.swapList.setRootIsDecorated(False)
    self.swapList.setItemsExpandable(False)
    self.swapList.setAnimated(True)
    self.swapList.setObjectName(_fromUtf8("swapList"))
    self.swapList.header().setCascadingSectionResizes(True)
    self.swapList.header().setSortIndicatorShown(True)
    self.gridLayout_11.addWidget(self.swapList, 1, 0, 1, 1)
    self.gridLayout_12.addWidget(self.frame_6, 0, 0, 1, 1)
    self.contentWidget.addWidget(self.content4)
    self.content5 = QtGui.QWidget()
    self.content5.setObjectName(_fromUtf8("content5"))
    self.gridLayout_9 = QtGui.QGridLayout(self.content5)
    self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
    self.frame_5 = QtGui.QFrame(self.content5)
    self.frame_5.setObjectName(_fromUtf8("frame_5"))
    self.gridLayout_10 = QtGui.QGridLayout(self.frame_5)
    self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
    self.diskSpaceWarning = QtGui.QLabel(self.frame_5)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.diskSpaceWarning.sizePolicy().hasHeightForWidth())
    self.diskSpaceWarning.setSizePolicy(sizePolicy)
    self.diskSpaceWarning.setTextFormat(QtCore.Qt.RichText)
    self.diskSpaceWarning.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
    self.diskSpaceWarning.setWordWrap(True)
    self.diskSpaceWarning.setObjectName(_fromUtf8("diskSpaceWarning"))
    self.gridLayout_10.addWidget(self.diskSpaceWarning, 0, 0, 1, 1)
    self.gridLayout_9.addWidget(self.frame_5, 0, 0, 1, 1)
    self.contentWidget.addWidget(self.content5)
    self.content6 = QtGui.QWidget()
    self.content6.setObjectName(_fromUtf8("content6"))
    self.gridLayout_14 = QtGui.QGridLayout(self.content6)
    self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
    self.frame_7 = QtGui.QFrame(self.content6)
    self.frame_7.setObjectName(_fromUtf8("frame_7"))
    self.gridLayout_13 = QtGui.QGridLayout(self.frame_7)
    self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
    self.diskSpaceWarning_2 = QtGui.QLabel(self.frame_7)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.diskSpaceWarning_2.sizePolicy().hasHeightForWidth())
    self.diskSpaceWarning_2.setSizePolicy(sizePolicy)
    self.diskSpaceWarning_2.setTextFormat(QtCore.Qt.RichText)
    self.diskSpaceWarning_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
    self.diskSpaceWarning_2.setWordWrap(True)
    self.diskSpaceWarning_2.setObjectName(_fromUtf8("diskSpaceWarning_2"))
    self.gridLayout_13.addWidget(self.diskSpaceWarning_2, 0, 0, 1, 1)
    spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.gridLayout_13.addItem(spacerItem, 1, 0, 1, 1)
    self.horizontalLayout_2 = QtGui.QHBoxLayout()
    self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
    spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_2.addItem(spacerItem1)
    self.midoriButton = QtGui.QToolButton(self.frame_7)
    self.midoriButton.setText(_fromUtf8(""))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/midori.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.midoriButton.setIcon(icon)
    self.midoriButton.setIconSize(QtCore.QSize(64, 64))
    self.midoriButton.setCheckable(True)
    self.midoriButton.setObjectName(_fromUtf8("midoriButton"))
    self.horizontalLayout_2.addWidget(self.midoriButton)
    self.operaButton = QtGui.QToolButton(self.frame_7)
    self.operaButton.setText(_fromUtf8(""))
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/opera.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.operaButton.setIcon(icon1)
    self.operaButton.setIconSize(QtCore.QSize(64, 64))
    self.operaButton.setCheckable(True)
    self.operaButton.setObjectName(_fromUtf8("operaButton"))
    self.horizontalLayout_2.addWidget(self.operaButton)
    self.chromeButton = QtGui.QToolButton(self.frame_7)
    self.chromeButton.setText(_fromUtf8(""))
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/google-chrome.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.chromeButton.setIcon(icon2)
    self.chromeButton.setIconSize(QtCore.QSize(64, 64))
    self.chromeButton.setCheckable(True)
    self.chromeButton.setObjectName(_fromUtf8("chromeButton"))
    self.horizontalLayout_2.addWidget(self.chromeButton)
    self.epiphanyButton = QtGui.QToolButton(self.frame_7)
    self.epiphanyButton.setText(_fromUtf8(""))
    icon3 = QtGui.QIcon()
    icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/epiphany.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.epiphanyButton.setIcon(icon3)
    self.epiphanyButton.setIconSize(QtCore.QSize(64, 64))
    self.epiphanyButton.setCheckable(True)
    self.epiphanyButton.setObjectName(_fromUtf8("epiphanyButton"))
    self.horizontalLayout_2.addWidget(self.epiphanyButton)
    self.firefoxButton = QtGui.QToolButton(self.frame_7)
    self.firefoxButton.setText(_fromUtf8(""))
    icon4 = QtGui.QIcon()
    icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/firefox.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.firefoxButton.setIcon(icon4)
    self.firefoxButton.setIconSize(QtCore.QSize(64, 64))
    self.firefoxButton.setCheckable(True)
    self.firefoxButton.setAutoRepeat(True)
    self.firefoxButton.setObjectName(_fromUtf8("firefoxButton"))
    self.horizontalLayout_2.addWidget(self.firefoxButton)
    self.noBrowserButton = QtGui.QToolButton(self.frame_7)
    self.noBrowserButton.setText(_fromUtf8(""))
    icon5 = QtGui.QIcon()
    icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.noBrowserButton.setIcon(icon5)
    self.noBrowserButton.setIconSize(QtCore.QSize(64, 64))
    self.noBrowserButton.setCheckable(True)
    self.noBrowserButton.setObjectName(_fromUtf8("noBrowserButton"))
    self.horizontalLayout_2.addWidget(self.noBrowserButton)
    spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_2.addItem(spacerItem2)
    self.gridLayout_13.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
    self.gridLayout_14.addWidget(self.frame_7, 0, 0, 1, 1)
    self.contentWidget.addWidget(self.content6)
    self.gridLayout_2.addWidget(self.contentWidget, 1, 0, 1, 1)
    self.frame = QtGui.QFrame(self.centralwidget)
    self.frame.setObjectName(_fromUtf8("frame"))
    self.gridLayout = QtGui.QGridLayout(self.frame)
    self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
    self.horizontalLayout = QtGui.QHBoxLayout()
    self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    self.cancelButton = QtGui.QPushButton(self.frame)
    self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
    self.horizontalLayout.addWidget(self.cancelButton)
    spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout.addItem(spacerItem3)
    self.backButton = QtGui.QPushButton(self.frame)
    self.backButton.setEnabled(False)
    self.backButton.setObjectName(_fromUtf8("backButton"))
    self.horizontalLayout.addWidget(self.backButton)
    self.forwardButton = QtGui.QPushButton(self.frame)
    self.forwardButton.setObjectName(_fromUtf8("forwardButton"))
    self.horizontalLayout.addWidget(self.forwardButton)
    self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
    self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 1)
    MainWindow.setCentralWidget(self.centralwidget)

    self.retranslateUi(MainWindow)
    self.contentWidget.setCurrentIndex(0)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Induction Linux Setup", None, QtGui.QApplication.UnicodeUTF8))
    self.label.setText(QtGui.QApplication.translate("MainWindow", "Induction Linux Setup", None, QtGui.QApplication.UnicodeUTF8))
    self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to the Induction Linux Setup guide.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When you are ready to begin, click the &quot;<span style=\" font-weight:600;\">Start</span>&quot; button below.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is the setup guide allow you to configure some basic system settings before the installation begins, including:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The user interface style.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The default web browser.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The default account\'s credentials.</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click &quot;<span style=\" font-weight:600;\">Forward</span>&quot; to begin the installation process.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Induction Linux needs a partition to install itself onto.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select one below:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    self.partitionList.setSortingEnabled(True)
    self.partitionList.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Label", None, QtGui.QApplication.UnicodeUTF8))
    self.partitionList.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Size", None, QtGui.QApplication.UnicodeUTF8))
    self.partitionList.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
    self.partitionList.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Identifier", None, QtGui.QApplication.UnicodeUTF8))
    self.partitionList.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "UUID", None, QtGui.QApplication.UnicodeUTF8))
    self.label_6.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It is recommended that you have a Swap partition. A Swap partition is used as if it were RAM, but not in every case. In case you don\'t have enough RAM to run the applications you need, Linux uses the Swap partition as RAM.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Note that Swap space is <span style=\" font-style:italic;\">not</span> as fast as normal RAM. It is much, much slower, but it gets the job done.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    self.swapList.setSortingEnabled(True)
    self.swapList.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Label", None, QtGui.QApplication.UnicodeUTF8))
    self.swapList.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Size", None, QtGui.QApplication.UnicodeUTF8))
    self.swapList.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
    self.swapList.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Identifier", None, QtGui.QApplication.UnicodeUTF8))
    self.swapList.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "UUID", None, QtGui.QApplication.UnicodeUTF8))
    self.diskSpaceWarning.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Induction Linux needs at least <span style=\" font-weight:600;\">2.5GB</span> of disk space to function properly.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The partition that you have selected currently has a size of <span style=\" font-weight:600;\">{{disk_space}}</span>, which leaves you with a total of <span style=\" font-weight:600;\">{{useable_space}}</span> for personal files and additional software.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Are you sure that you want to continue with the installation? If you\'d like to change the install partition, press the &quot;<span style=\" font-weight:600;\">Back</span>&quot; button until you reach the installation destination step.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    self.diskSpaceWarning_2.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu LGC Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Since There are many different types of people, there are many types of web browsers available to install for Induction Linux.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\';\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\">Choose from some of the most common ones listed below (don\'t choose a web browser if your desired browser isn\'t listed here, as it can be installed once the system is running).</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    self.midoriButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Extremely leightweight Midori web browser", None, QtGui.QApplication.UnicodeUTF8))
    self.operaButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Fast and feature-packed Opera", None, QtGui.QApplication.UnicodeUTF8))
    self.chromeButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Google Chrome, the fastest web browser", None, QtGui.QApplication.UnicodeUTF8))
    self.epiphanyButton.setToolTip(QtGui.QApplication.translate("MainWindow", "GNOME\'s default Epiphany web browser", None, QtGui.QApplication.UnicodeUTF8))
    self.firefoxButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Firefox, the most customizable", None, QtGui.QApplication.UnicodeUTF8))
    self.noBrowserButton.setToolTip(QtGui.QApplication.translate("MainWindow", "No web browser", None, QtGui.QApplication.UnicodeUTF8))
    self.cancelButton.setText(QtGui.QApplication.translate("MainWindow", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
    self.backButton.setText(QtGui.QApplication.translate("MainWindow", "&Back", None, QtGui.QApplication.UnicodeUTF8))
    self.forwardButton.setText(QtGui.QApplication.translate("MainWindow", "&Start", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
