import sys 	
from PyQt5 import QtWidgets 

'''
    【简介】
	第一个PyQt例子
   
    
'''
# 创建app是很有必要的  app= QtWidget.QApplication(sys.argv)
app = QtWidgets.QApplication(sys.argv)
# 创建一个QWidget
widget = QtWidgets.QWidget()
# 改变大小 设置标题的名称 显示
widget.resize(360, 360)
widget.setWindowTitle("hello, pyqt5")
widget.show()
sys.exit(app.exec_())
