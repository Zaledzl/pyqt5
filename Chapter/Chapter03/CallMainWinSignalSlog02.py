# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from Chapter.Chapter03.MainWinSignalSlog02 import Ui_Form
from PyQt5.QtCore import pyqtSignal , Qt 
'''
怎么说呢，感觉这个小程序的话，是麻雀虽小，五脏俱全的感觉啊
实现的功能还是很多的呀，是的，可以学到很多东西的呀
感觉这个的难度比较大，所以说，还是结合书来看吧'''
# 在类里面定义的所有的函数，都要有
class MyMainWindow(QMainWindow, Ui_Form):
	# 这里是 使用 pyqtSignal 来定义信号的  信号可以传递多个参数
	helpSignal = pyqtSignal(str)
	printSignal = pyqtSignal(list)
	# 声明一个多重载版本的信号，包括了一个带int和str类型参数的信号，以及带str参数的信号
	previewSignal = pyqtSignal([int,str],[str])
	
	def __init__(self, parent=None):    
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)
		# 这个也是构造方法 直接调用了 不然全写在 __init__里面会显得很混乱的
		self.initUI()

	# 这个方法呢，就是连接了信号和槽的哈
	# 就是说明了在请么情况下调用什么函数的哈 现在是越来越清楚了 包括代码的意思和各部分之间的层次逻辑结构
	# 这个文件的 信号和槽 都是手动编写的
	def initUI(self):
		# 这里的 信号和槽 都是自己定义的 如果使用了多重在版本的信号，要在这里指明的哈
		# 这里只是说明了 什么信号和什么槽链接，但是并没有说明这个信号是要谁来发送的
		self.helpSignal.connect(self.showHelpMessage)
		self.printSignal.connect(self.printPaper)
		self.previewSignal[str].connect(self.previewPaper)
		self.previewSignal[int,str].connect(self.previewPaperWithArgs)  

		# 这里的 信号是默认的有的信号  槽 是自己定义的函数
		self.printButton.clicked.connect(self.emitPrintSignal)
		self.previewButton.clicked.connect(self.emitPreviewSignal)

	# 发射预览信号
	# 是的，这个的信号的参数可以不同，这个就是 信号的重载了
	#  这个就是手动定义 信号发射条件
	# 这个例子和教程真的是很棒了哈
	def emitPreviewSignal(self):
		if self.previewStatus.isChecked() == True:
			self.previewSignal[int,str].emit(1080," Full Screen")
		elif self.previewStatus.isChecked() == False:
			self.previewSignal[str].emit("Preview")

	# 发射打印信号
	def emitPrintSignal(self):
		# 这是获取了值之后，把字符串拼接起来了哈
		pList = []
		pList.append(self.numberSpinBox.value() )
		pList.append(self.styleCombo.currentText())
		self.printSignal.emit(pList)
		
	def printPaper(self,list):
		self.resultLabel.setText("打印: "+"份数："+ str(list[0]) +" 纸张："+str(list[1]))

	def previewPaperWithArgs(self,style,text):
		self.resultLabel.setText(str(style)+text)		

	def previewPaper(self,text):
		self.resultLabel.setText(text)  

	# 重载点击键盘事件
	def keyPressEvent(self, event):
		# 判断
		if event.key() == Qt.Key_F1:
			# 当什么的时候，emit这个信号 emit的时候，带了参数
			# 然后参数就可以传递到槽函数了
			self.helpSignal.emit("help message")

	# 显示帮助消息
	def showHelpMessage(self,message):
		# 这里是说，父对象.更具体的对象.操作（操作信息）
		self.resultLabel.setText(message)
		self.statusBar().showMessage(message)

# 这个是基本的老套路
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	win = MyMainWindow()  
	win.show()  
	sys.exit(app.exec_())  
