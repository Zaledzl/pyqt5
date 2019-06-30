# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow, QWidget , QFileDialog 
from MainForm import Ui_MainWindow  

class MainForm( QMainWindow , Ui_MainWindow):  
	def __init__(self):  
		super(MainForm,self).__init__()  
		self.setupUi(self)
		# 在菜单中添加了信息之后，如果想让其在操作后有所动作
		# 必须定义 信号和槽
		# 菜单的点击事件，当点击关闭菜单时连接槽函数 close()     
		self.fileCloseAction.triggered.connect(self.close)  
		# 菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()     
		self.fileOpenAction.triggered.connect(self.openMsg)    

	# 这里是打开文件的方法 下面有打开文件的命令
	def openMsg(self):  
		file,ok= QFileDialog.getOpenFileName(self,"打开","C:/","All Files (*);;Text Files (*.txt)") 
		# 在状态栏显示文件地址  		
		self.statusbar.showMessage(file)                   
    
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	win = MainForm()  
	win.show()  
	sys.exit(app.exec_()) 
