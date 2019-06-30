# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from Chapter.Chapter03.firstMainWin import *
# 是的，通过上面的这个import 也是可以很清楚的看到 在添加或是变化了文件结构之后，如何import想要的文件的
'''
这个程序就是简单地展示了一个很简单的图形化界面哈，是属于最基本的操作，没有什么好说的呢'''
# 这个类的父对象是 QMainWindow 说明在 Qt Designer中新建的是 MainWindow ，后面的那个参数就是
# 然后下面的这段程序完全就是套路了
# 新建一个类，类里面有一些固定的写法
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

# 这个地方就是新建 app，然后调用上面写好的类，上面写好的类，再调用其他的类，最后就能展示出来一个图形化界面了
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()  
    sys.exit(app.exec_())  
