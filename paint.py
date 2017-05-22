import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from mathTex2Pixmap import mathTex_to_QPixmap

def paintEvent(QWidget,control,style_s=1,style_g=1):
	# size = 1
	# QGraphicsScene scene;
	img = QImage(500,200,QImage.Format_ARGB32_Premultiplied)
	qp = QPainter()
	qp.begin(img)
	qp.setPen(QColor(Qt.black))
	
	# qp.setColor(QColor(Qt.black))
	brush = QBrush(Qt.SolidPattern)
	brush.setColor(QColor(Qt.white))
	qp.setBrush(brush)
	qp.setPen(QColor(Qt.white))
	qp.drawRect(0,0,500,200)

	pen = QPen(Qt.black, 2, Qt.SolidLine)
	qp.setPen(pen)
	# qp.setPen(QColor(Qt.black))
	# style_s = 1 #dao ham co nghiem 
	# style_s = 2 #dao ham vo nghiem
	# style_g = 1 #dang do thi a > 0
	# style_g = 2 #dang do thi a  < 0
	A=(10,50)
	D=(490,80)
	E=(60,20)
	F=(60,180)
	qp.drawLine(A[0],A[1],D[0],A[1])#AB
	qp.drawLine(A[0],D[1],D[0],D[1])#CD
	qp.drawLine(E[0],E[1],F[0],F[1])#EF
	I=((D[0]+E[0])/2,A[1])
	
	qp.setPen(QColor(Qt.black))
	qp.drawLine(I[0]-1,I[1],I[0]-1,F[1])
	qp.drawLine(I[0]+1,I[1],I[0]+1,F[1])
	qp.setFont(QFont('Arial', 10))
	posx = ((A[0]+E[0])/2,(A[1]+E[1])/2+10)
	qp.drawText(posx[0],posx[1], "x")
	qp.drawText(posx[0],posx[1]+D[1]-A[1], "y\'")
	qp.drawText(posx[0],posx[1]+D[1]-A[1]+(-D[1]+F[1])/2, "y")
	##drawpixmap
	latex = control[0] #1
	# latex = r'$\sqrt{2}$'
	qp.drawPixmap(I[0]-3,posx[1]-20,mathTex_to_QPixmap(latex,10)) #khong xac dinh
	latex = r'-$\infty$'
	qp.drawPixmap(E[0]+3,posx[1]-10,mathTex_to_QPixmap(latex,10)) # - Vo cung
	if style_s==1:
		latex = r'-$\infty$'
		if style_g==1:
			qp.drawPixmap(E[0]+3,F[1]-10,mathTex_to_QPixmap(latex,10)) #type 1
			qp.drawPixmap(I[0]-25,F[1]-10,mathTex_to_QPixmap(latex,10))
		elif style_g==2:
			latex = r'+$\infty$'
			qp.drawPixmap(E[0]+3,D[1]+10,mathTex_to_QPixmap(latex,10)) #type 2
			qp.drawPixmap(I[0]-25,D[1]+10,mathTex_to_QPixmap(latex,10))
	elif style_s==2:
		latex = r'-$\infty$'
		if style_g==1:
			qp.drawPixmap(E[0]+3,F[1]-10,mathTex_to_QPixmap(latex,10)) #type 1
			latex = r'+$\infty$'
			qp.drawPixmap(I[0]-25,D[1]+10,mathTex_to_QPixmap(latex,10))
		elif style_g==2:
			latex = r'+$\infty$'
			qp.drawPixmap(E[0]+3,D[1]+10,mathTex_to_QPixmap(latex,10))
			latex = r'-$\infty$'
			qp.drawPixmap(I[0]-25,F[1]-10,mathTex_to_QPixmap(latex,10))

	latex = r'+$\infty$'
	qp.drawPixmap(D[0]-18,posx[1]-10,mathTex_to_QPixmap(latex,10)) # + Vo cung
	if style_s==1:
		latex = r'+$\infty$'
		if style_g==2:
			latex = r'-$\infty$'
			qp.drawPixmap(I[0],F[1]-10,mathTex_to_QPixmap(latex,10)) #type 2
			qp.drawPixmap(D[0]-18,F[1]-10,mathTex_to_QPixmap(latex,10)) #bang line 3
		elif style_g==1:
			qp.drawPixmap(I[0],D[1]+10,mathTex_to_QPixmap(latex,10)) #type 1
			qp.drawPixmap(D[0]-18,D[1]+10,mathTex_to_QPixmap(latex,10)) #bang line 3
	elif style_s==2:
		
		if style_g==1:
			latex = r'-$\infty$'
			qp.drawPixmap(I[0],F[1]-10,mathTex_to_QPixmap(latex,10))
			latex = r'+$\infty$'
			qp.drawPixmap(D[0]-18,D[1]+10,mathTex_to_QPixmap(latex,10))
		elif style_g==2:
			latex = r'+$\infty$'
			qp.drawPixmap(I[0],D[1]+10,mathTex_to_QPixmap(latex,10))
			latex = r'-$\infty$'
			qp.drawPixmap(D[0]-18,F[1]-10,mathTex_to_QPixmap(latex,10))

	midXIE = (I[0]+E[0])/2
	midXID = (I[0]+D[0])/2
	if style_s==1:
		latex = control[3] #4
		qp.drawPixmap(midXIE-10,posx[1]-20,mathTex_to_QPixmap(latex,10)) # x1
	if style_s==1:
		latex = control[1] #2
		if style_g==1:
			qp.drawPixmap(midXIE-10,D[1]+2,mathTex_to_QPixmap(latex,10)) #type 1 MIN
		elif style_g==2:
			qp.drawPixmap(midXIE-10,F[1]-15,mathTex_to_QPixmap(latex,10))#type 2 MIN
	if style_s==1:
		latex = control[4] #3
		qp.drawPixmap(midXID-10,posx[1]-20,mathTex_to_QPixmap(latex,10)) # x2
	if style_s==1:
		latex = control[2] #1
		if style_g==1:
			qp.drawPixmap(midXID-10,F[1]-15,mathTex_to_QPixmap(latex,10)) #type 1 MAX
		elif style_g==2:
			qp.drawPixmap(midXID-10,D[1]+2,mathTex_to_QPixmap(latex,10)) #type 2 MAX
	##
	if style_s==1:
		qp.drawText(midXIE,posx[1]+D[1]-A[1],"0") #so 0
		qp.drawText(midXID,posx[1]+D[1]-A[1],"0") #so 0
	elif style_s==2:
		if style_g==1:
			qp.drawText(midXIE,posx[1]+D[1]-A[1],"+") #dau +
			qp.drawText(midXID,posx[1]+D[1]-A[1],"+") #dau +
		elif style_g==2:
			qp.drawText(midXIE,posx[1]+D[1]-A[1],"-") #dau +
			qp.drawText(midXID,posx[1]+D[1]-A[1],"-") #dau +
	##
	if style_s==1:
		if style_g==1:
			qp.drawText((midXIE+E[0])/2,posx[1]+D[1]-A[1],"+") #+
			qp.drawText((midXIE+I[0])/2,posx[1]+D[1]-A[1],"-") #-
			qp.drawText((midXID+I[0])/2,posx[1]+D[1]-A[1],"-") #-
			qp.drawText((midXID+D[0])/2,posx[1]+D[1]-A[1],"+") #+
		elif style_g==2:
			qp.drawText((midXIE+E[0])/2,posx[1]+D[1]-A[1],"-") #+
			qp.drawText((midXIE+I[0])/2,posx[1]+D[1]-A[1],"+") #-
			qp.drawText((midXID+I[0])/2,posx[1]+D[1]-A[1],"+") #-
			qp.drawText((midXID+D[0])/2,posx[1]+D[1]-A[1],"-") #+
	##draw arrow
	pen = QPen(Qt.black, 2, Qt.SolidLine)
	qp.setPen(pen)
	move = I[0] - F[0]

	if style_s==1:
		if style_g==1:
			#1
			qp.drawLine(F[0]+25,F[1]-15,midXIE-10,D[1]+30)
			qp.drawLine(midXIE-10,D[1]+30,midXIE-18,D[1]+30)
			qp.drawLine(midXIE-10,D[1]+30,midXIE-12,D[1]+38)
			#2
			qp.drawLine(midXIE+20,D[1]+30,I[0]-30,F[1]-15)
			qp.drawLine(I[0]-30,F[1]-15,I[0]-38,F[1]-15)
			qp.drawLine(I[0]-30,F[1]-15,I[0]-30,F[1]-23)
			#3
			move = I[0]-midXIE+10
			qp.drawLine(midXIE+20+move,D[1]+30,I[0]-30+move,F[1]-15)
			qp.drawLine(I[0]-30+move,F[1]-15,I[0]-38+move,F[1]-15)
			qp.drawLine(I[0]-30+move,F[1]-15,I[0]-30+move,F[1]-23)
			#4
			move = D[0]-midXIE
			qp.drawLine(F[0]+25+move,F[1]-15,midXIE-10+move,D[1]+30)
			qp.drawLine(midXIE-10+move,D[1]+30,midXIE-18+move,D[1]+30)
			qp.drawLine(midXIE-10+move,D[1]+30,midXIE-12+move,D[1]+38)
		elif style_g==2:
			#1
			move = I[0]- midXIE
			qp.drawLine(midXIE+20-move,D[1]+30,I[0]-30-move,F[1]-15)
			qp.drawLine(I[0]-30-move,F[1]-15,I[0]-38-move,F[1]-15)
			qp.drawLine(I[0]-30-move,F[1]-15,I[0]-30-move,F[1]-23)
			#2
			qp.drawLine(F[0]+25+move,F[1]-15,midXIE-10+move,D[1]+30)
			qp.drawLine(midXIE-10+move,D[1]+30,midXIE-18+move,D[1]+30)
			qp.drawLine(midXIE-10+move,D[1]+30,midXIE-12+move,D[1]+38)
			#3
			move = I[0]-E[0]
			qp.drawLine(F[0]+25+move,F[1]-15,midXIE-10+move,D[1]+30)
			qp.drawLine(midXIE-10+move,D[1]+30,midXIE-18+move,D[1]+30)
			qp.drawLine(midXIE-10+move,D[1]+30,midXIE-12+move,D[1]+38)
			#4
			qp.drawLine(midXIE+20+move,D[1]+30,I[0]-30+move,F[1]-15)
			qp.drawLine(I[0]-30+move,F[1]-15,I[0]-38+move,F[1]-15)
			qp.drawLine(I[0]-30+move,F[1]-15,I[0]-30+move,F[1]-23)
	elif style_s==2:
		if style_g==1:
			qp.drawLine(F[0]+25,F[1]-15,I[0]-30,D[1]+20)
			qp.drawLine(I[0]-30,D[1]+20,I[0]-38,D[1]+20)
			qp.drawLine(I[0]-30,D[1]+20,I[0]-33,D[1]+28)
			move = D[0]-I[0]
			qp.drawLine(F[0]+25+move,F[1]-15,I[0]-30+move,D[1]+20)
			qp.drawLine(I[0]-30+move,D[1]+20,I[0]-38+move,D[1]+20)
			qp.drawLine(I[0]-30+move,D[1]+20,I[0]-33+move,D[1]+28)
		elif style_g==2:
			qp.drawLine(E[0]+25,D[1]+25,I[0]-35,F[1]-15)
			qp.drawLine(I[0]-35,F[1]-15,I[0]-43,F[1]-13)
			qp.drawLine(I[0]-35,F[1]-15,I[0]-39,F[1]-23)
			move = D[0]-I[0]
			qp.drawLine(E[0]+25+move,D[1]+25,I[0]-35+move,F[1]-15)
			qp.drawLine(I[0]-35+move,F[1]-15,I[0]-43+move,F[1]-13)
			qp.drawLine(I[0]-35+move,F[1]-15,I[0]-39+move,F[1]-23)
	qp.end()
	img.save("im.png")
	return img