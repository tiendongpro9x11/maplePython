# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt Designer/NULL.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import popplerqt4
from maple import maple

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s
try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8("Form"))
		Form.resize(840, 680)
		Form.setStyleSheet(_fromUtf8("background-color:  rgb(255, 255, 255);"))
		self.area = QtGui.QScrollArea(Form)
		self.area.setGeometry(QtCore.QRect(10,10,800,500))

		self.label = QtGui.QLabel(self.area)
		self.label.setText(_fromUtf8(""))
		self.label.setObjectName(_fromUtf8("label"))


		self.label_2 = QtGui.QLabel(Form)
		self.label_2.setObjectName(_fromUtf8("label"))
		self.label_2.setGeometry(QtCore.QRect(10, 490, 500, 200))

		self.pushButton = QtGui.QPushButton(Form)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.pushButton.setGeometry(QtCore.QRect(700, 560, 99, 40))
		self.pushButton.setStyleSheet(_fromUtf8("background-color: black;color:white;"))
		self.pushButton.clicked.connect(self.showgraph)
		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)
		
	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate("Form", "Form", None))
		self.pushButton.setText(_translate("Form", "Show Graph", None))
	def setpix(self,y):
		self.readpdffile()
		self.label_2.setPixmap(QtGui.QPixmap(y))
	def showgraph(self):
		with open(os.getcwd()+"/linkmaple.txt") as F:
			MAPLEDIR = F.readline()
		os.system(MAPLEDIR+" "+os.getcwd()+"/rungrap.mpl")

	def readpdffile(self):
		doc = popplerqt4.Poppler.Document.load(os.getcwd()+"/latex.pdf")
		doc.setRenderHint(popplerqt4.Poppler.Document.Antialiasing)
		doc.setRenderHint(popplerqt4.Poppler.Document.TextAntialiasing)
		page = doc.page(0)
		image = page.renderToImage(75,75)
		self.label.setPixmap(QtGui.QPixmap.fromImage(image))
		self.area.setWidget(self.label)