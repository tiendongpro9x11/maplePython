# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtGui ,QtCore
from mathTex2Pixmap import mathTex_to_QPixmap
import os
import sys
import toLatex
import m
from maple import maple
from paint import paintEvent
from replace2sqrt import re2sqrt

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

import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
mapleDir = ''
#Form step 1
class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8("Form"))
		Form.resize(754, 555)
		Form.setStyleSheet(_fromUtf8("background-color:  rgb(255, 255, 255);\n"))
		self.frame = QtGui.QFrame(Form)
		self.frame.setGeometry(QtCore.QRect(0, 70, 751, 221))
		self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtGui.QFrame.Raised)
		self.frame.setObjectName(_fromUtf8("frame"))
		self.gridLayoutWidget = QtGui.QWidget(self.frame)
		self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 50, 731, 151))
		self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
		self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setMargin(0)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget)
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
		self.pushButton_3 = QtGui.QPushButton(self.gridLayoutWidget)
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
		self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
		self.pushButton_4 = QtGui.QPushButton(self.gridLayoutWidget)
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)
		self.label = QtGui.QLabel(self.gridLayoutWidget)
		self.label.setObjectName(_fromUtf8("label"))
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1,QtCore.Qt.AlignHCenter)
		self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1,QtCore.Qt.AlignHCenter)
		self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1,QtCore.Qt.AlignHCenter)
		self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1,QtCore.Qt.AlignHCenter)
		##
		self.pushButton.setStyleSheet(_fromUtf8("background-color: black;color:white;"))
		self.pushButton_2.setStyleSheet(_fromUtf8("background-color: black;color:white;"))
		self.pushButton_3.setStyleSheet(_fromUtf8("background-color: black;color:white;"))
		self.pushButton_4.setStyleSheet(_fromUtf8("background-color: black;color:white;"))
		##
		s = r'$'+toLatex.py2tex("(a*x**2+b*x+c)/(d*x+e)")+'$' #add
		self.label.setPixmap(QtGui.QPixmap(mathTex_to_QPixmap(s,15))) #add
		s = r'$'+toLatex.py2tex("(a*x+b)/(c*x+d)")+'$'
		self.label_2.setPixmap(QtGui.QPixmap(mathTex_to_QPixmap(s,15)))
		s = r'$'+toLatex.py2tex("a*x**3+b*x**2+c*x+d")+'$' #add
		self.label_3.setPixmap(QtGui.QPixmap(mathTex_to_QPixmap(s,10))) #add
		s = r'$'+toLatex.py2tex("a*x**4+b*x**2+c")+'$'
		self.label_4.setPixmap(QtGui.QPixmap(mathTex_to_QPixmap(s,10)))
		##
		self.pushButton.clicked.connect(self.showdialog)
		##
		self.pushButton_5 = QtGui.QPushButton(Form)
		self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
		self.pushButton_5.setGeometry(QtCore.QRect(0, 0, 99, 40))
		self.pushButton_5.setStyleSheet(_fromUtf8("background-color: black;color:white;"))
		self.pushButton_5.clicked.connect(self.openfile)
		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		
		Form.setWindowTitle(_translate("Form", "Form", None))
		self.pushButton_3.setText(_translate("Form", "Select", None))
		self.pushButton_4.setText(_translate("Form", "Select", None))
		self.pushButton_2.setText(_translate("Form", "Select", None))
		self.pushButton.setText(_translate("Form", "Select", None))
		self.pushButton_5.setText(_translate("Form","Open file",None))
	def openfile(self):
		dlg = QtGui.QFileDialog()
		dlg.setFileMode(QtGui.QFileDialog.AnyFile)
		dlg.setFilter("Select Maple command line")
		filenames = QtCore.QStringList()
		if dlg.exec_():
			filenames = dlg.selectedFiles()
		a = [str(name) for name in filenames]
		mapleDir = a[0]
	#run dialog
	def showdialog(self):
		##xa nhau tu day
		r.hideF1()
		Form = QtGui.QDialog()
		ui = Ui_Dialog()
		ui.setupUi(Form)
		Form.show()
		Form.exec_()
#form dialog	
def getMapleDir():
	return mapleDir
class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName(_fromUtf8("Dialog"))
		Dialog.resize(508, 166)
		Dialog.setStyleSheet(_fromUtf8("background-color:  rgb(255, 255, 255);"))
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(100, 110, 351, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.gridLayoutWidget = QtGui.QWidget(Dialog)
		self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 20, 361, 76))
		self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
		self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setMargin(0)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
		self.lineEdit_2 = QtGui.QLineEdit(self.gridLayoutWidget)
		self.lineEdit_3 = QtGui.QLineEdit(self.gridLayoutWidget)
		self.lineEdit_4 = QtGui.QLineEdit(self.gridLayoutWidget)
		self.lineEdit_5 = QtGui.QLineEdit(self.gridLayoutWidget)
		self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
		self.gridLayout.addWidget(self.lineEdit_5, 0, 4, 1, 1)
		
		self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
		self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
		
		self.lineEdit.setStyleSheet(_fromUtf8("border-color: black;"))
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
		
		self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
		self.gridLayout.addWidget(self.lineEdit_3, 0, 2, 1, 1)
		
		self.lineEdit_4.setStyleSheet(_fromUtf8("border-color: black;"))
		self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
		self.gridLayout.addWidget(self.lineEdit_4, 0, 3, 1, 1)
		self.label = QtGui.QLabel(self.gridLayoutWidget)
		self.label.setObjectName(_fromUtf8("label"))
		self.gridLayout.addWidget(self.label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
		self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
		self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
		self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
		self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
		self.label_5.setStyleSheet(_fromUtf8("border-color: black;"))
		self.label_5.setObjectName(_fromUtf8("label_5"))
		self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

		self.buttonBox.accepted.connect(self.f1)
		self.buttonBox.rejected.connect(self.f2)

		self.buttonBox.setStyleSheet(_fromUtf8("background-color: black;color:white;"))

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
		self.label.setText(_translate("Dialog", "a", None))
		self.label_2.setText(_translate("Dialog", "b", None))
		self.label_3.setText(_translate("Dialog", "c", None))
		self.label_4.setText(_translate("Dialog", "d", None))
		self.label_5.setText(_translate("Dialog", "e", None))
	def f2(self):
		r.showF1()
	#event click OK	
	def f1(self):
		l = []
		if not self.lineEdit.text().isEmpty():
			shots = int(self.lineEdit.text())
			if not isclose(shots,0):
				l.append(shots)
		if not self.lineEdit_2.text().isEmpty():
			shots = int(self.lineEdit_2.text())
			l.append(shots)
		if not self.lineEdit_3.text().isEmpty():
			shots = int(self.lineEdit_3.text())
			l.append(shots)
		if not self.lineEdit_4.text().isEmpty():
			shots = int(self.lineEdit_4.text())
			if not isclose(shots,0):
				l.append(shots)
		if not self.lineEdit_5.text().isEmpty():
			shots = int(self.lineEdit_5.text())
			l.append(shots)
		if len(l) < 5:
			print "Input again."
			r.showF1()
		else:
			exe(l)
			
#run after click ok
def exe(l):

	r.hideF1()
	if l[0] > 0:
		style_g = 1
	elif l[0] < 0:
		style_g = 2
	s = '(('+str(l[0])+')*x^2+('+str(l[1])+')*x+('+str(l[2])+'))/(('+str(l[3])+')*x+('+str(l[4])+'))' #y = (x^2+x+1)/(x+1)
	par1 = maple(s+';') #loai bo so 1
	par1 = par1.replace("^","**") #chuyen ve python
	listGui2 = [] #tao mot mang de luu cac Latex
	listGui3 = []
	par1 = r'$y='+toLatex.py2tex(par1)+r'$'

	listGui2.append(par1) #0

	
	# par = -l[4]*1.0/l[3] #-e/d
	par_0 = toLatex.py2tex(maple('solve(('+str(l[3])+')*x+('+str(l[4])+'));'))
	listGui3.append(r'$'+par_0+r'$') #GUI #1
	par1 = r'$R\backslash\left\{'+par_0+r'\right\}$'
	listGui2.append(par1) #1
	#connect 
	
	X = 'r:=rem('+str(l[0])+'*x^2+('+str(l[1])+')*x+('+str(l[2])+'),'+str(l[3])+'*x+('+str(l[4])+'),x,\'q\'):q;'
	par1 = maple(X) #get q
	s1 = par1
	par1 = par1.replace("^","**")
	#phep chia da thuc
	par2 = maple("rem("+str(l[0])+"*x^2+("+str(l[1])+")*x+("+str(l[2])+"),"+str(l[3])+"*x+("+str(l[4])+"),x,\'q\')/("+str(l[3])+"*x+("+str(l[4])+")):simplify(%);")

	par3 = r'$y='+toLatex.py2tex(par1)+r'$' #phan nguyen
	par1 = r'$y='+toLatex.py2tex(par1)+r'+'+toLatex.py2tex(par2)+r'$'
	par4 = r'$\lim_{x\to\infty}('+toLatex.py2tex(par2)+r')=0$' #phan du
	listGui2.append(par1) #2

	par1 = r'$\lim_{x\to -\infty }y=-\infty$'
	listGui2.append(par1) #3
	par1 = r'$\lim_{x\to+\infty }y=+\infty$'
	listGui2.append(par1) #4


	par1 = r'$\lim_{x\to('+par_0+r')^{-} }y=-\infty$'
	listGui2.append(par1) #5
	par1 = r'$\lim_{x\to('+par_0+r')^{+} }y=+\infty$'
	listGui2.append(par1) #6
	par1 = r'$x='+par_0+r'$'
	listGui2.append(par1) #7
	par1 = r'$x\to('+par_0+r')^{-}$'
	listGui2.append(par1) #8
	par1 = r'$x\to('+par_0+r')^{+}$'
	listGui2.append(par1) #9

	listGui2.append(par4) #10
	listGui2.append(par3) #11

	par1 = maple("simplify(diff("+s+",x));")
	par2 = par1.split(")/") # y' par2:=[(x^2+x+1,(x+1)^2] thieu ')'
	par_2 = par2
	# par_2[0] = par_2[0] + ')' # them ) #error
	par1 = par1.replace("^","**")
	par2 = par2[0]+')' #par2 := (x^2+x+1)
	par2 = maple('solve('+par2+');')
	par2 = par2.split(',')
	# with open(os.getcwd()+"/file.log","w") as F:
	# 	for x in listGui2:
	# 		F.write("Run-300: "+str(x)+"\n")
	#print "p"+par2[0]
	par_3 = maple('if type(evalf('+par2[0]+'),float) then 0 else 1 fi;')  #co nghiem hay ko
	#print "p"+par_3
	if int(par_3) != 1: #neu co nghiem
		par_1 = maple('if evalf('+par2[0]+') < evalf('+par2[1]+') then 1 else 0 fi;') ##sap xep nghiem x1 < x2

		if int(par_1) == 1:
			par3 = maple('simplify('+par2[0]+');') #nghiem 1
			par4 = maple('simplify('+par2[1]+');') #nghiem 2
		elif int(par_1) == 0 :
			par3 = maple('simplify('+par2[1]+');') #nghiem 1
			par4 = maple('simplify('+par2[0]+');') #nghiem 2
		# x1,x2 -> y(x)
		par5 = maple("x:="+par3+":expand("+s+");")
		par5 = re2sqrt(par5)
		
		par5 = r'$'+toLatex.py2tex(par5)+r'$'
		listGui3.append(par5) #GUI3 #2
		
		par5 = maple("x:="+par4+":expand("+s+");")
		par5 = re2sqrt(par5)
		
		par5 = r'$'+toLatex.py2tex(par5)+r'$'
		listGui3.append(par5) #GUI3 #3
	##
	# with open(os.getcwd()+"/file.log","w") as F:
	# 	for x in listGui3:
	# 		F.write("Run-300: "+str(x)+"\n")
	par1 = r'$'+toLatex.py2tex(par1)+r'$'
	listGui2.append(par1) #12
	#giai phuogn trinh dao ham
	subcontent = ''
	if int(par_3) != 1:#neu phuong trinh co nghiem
		style_s = 1
		if par3.find("^(1/2)") != -1: #nghiem co chua dau can
			par3 = re2sqrt(par3)
		par3 = r'$'+toLatex.py2tex(par3)+r'$'
		listGui2.append(par3) #13
		listGui3.append(par3) #GUI3 #4

		if par4.find("^(1/2)") != -1: #tuong tu
			par4 = re2sqrt(par4)
		par4 = r'$'+toLatex.py2tex(par4)+r'$'
		listGui2.append(par4) #14
		listGui3.append(par4) #GUI3 #5
		subcontent = '$y\'=0 \Leftrightarrow$ x={0} hoac x={1}'.format(listGui2[13],listGui2[14])
	else : #phuong trinh vo nghiem
		style_s = 2
		par_2[0] = par_2[0] + ')'
		par1 = maple('rem('+par_2[0]+','+par_2[1]+',x,\'q\'):q;')
		par1 = r'$'+toLatex.py2tex(par1)+r'$'
		par2 = maple('rem('+par_2[0]+','+par_2[1]+',x,\'q\')/'+par_2[1]+':simplify(%);')
		par2 = par2.replace("^","**")
		par2 = r'$'+toLatex.py2tex(par2)+r'$'
		if style_g==1:
			cpa = '>'
		else :
			cpa = '<'
		subcontent = r"y'={0} + {1} {2} 0 với mọi $x \neq {3}$".format(par1,par2,cpa,par_0)
	
	with open(os.getcwd()+"/file.log","w") as F:
		for x in listGui2:
			F.write("Run-362: "+str(x)+"\n")
	
	content_t = r'''\documentclass[17pt]{extarticle}
\setlength{\parindent}{0pt}
\usepackage[utf8]{vietnam}
\usepackage[paperheight=6in,paperwidth=8.5in,margin=2pt]{geometry}
\begin{document}
\everymath{\displaystyle}
'''
	content = r'''$\star$ Khảo sát và vẽ đồ thì hàm số: \\
{0}\\
 Hàm số đã cho có tập xác định là: {1}\\
 Sự biến thiên của hàm số:\\
	Ta viết hàm số dưới dạng: {2}\\
 Ta có: \\
{3} va {4}\\
 Vì {5} và {6} nên đường thẳng {7} là đường thẳng\\
tiệm cận đứng của đồ thị đã cho khi {8} và khi {9}\\
 Vì {10} nên đường thẳng {11} là tiệm cận xiên của\\
 đồ thị hàm số đã cho khi $x\to+\infty$ và $x\to-\infty$\\
$\star$ Bảng biến thiên:\\
 Ta có: y'={12} \\
	{13} \\
'''.format(listGui2[0],listGui2[1],listGui2[2],listGui2[3],listGui2[4],listGui2[5],listGui2[6],listGui2[7],listGui2[8],listGui2[9],listGui2[10],listGui2[11],listGui2[12],subcontent)
	##
	with open(os.getcwd()+"/latex.tex","w") as F:
		F.write(content_t+content+"\end{document}")
	os.system("pdflatex "+os.getcwd()+"/latex.tex")
	##
	r.setUI2(paintEvent(QtGui.QWidget,listGui3,style_s,style_g))
	r.showF2()
	#write on run graph
	with open(os.getcwd()+"/rungrap.mpl","w") as F:
		content_F = r'''
plotsetup(default):
interface(plotdevice):
plotsetup(tek,kermit):
plotsetup(ps,plotoutput=`plot.ps`,plotoptions=`portrait, noborder, width=1000, height=500`):
plotsetup(x11):
plotsetup(maplet):
plot([{0},{1}],x,color=["Red","Red"]);
'''.format(s,s1)
		F.write(content_F)
	
class MainWindows(object):
	def run(self):
		self.app = QtGui.QApplication(sys.argv)
		self.F = QtGui.QWidget()
		self.ui = Ui_Form()
		self.ui.setupUi(self.F)
		self.F2 = QtGui.QWidget()
		self.ui2 = m.Ui_Form()
		self.ui2.setupUi(self.F2)
		
		self.F.show()
	def setUI2(self,k):
		self.ui2.setpix(k)
	def hideF1(self):
		self.F.hide()
	def showF1(self):
		self.F.show()
	def showF2(self):
		self.F2.show()
	def getapp(self):
		return self.app
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
	return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

if __name__ == "__main__":
	r = MainWindows()
	r.run()
	sys.exit(r.getapp().exec_())