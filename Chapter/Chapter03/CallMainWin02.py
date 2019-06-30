# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from Chapter.Chapter03.MainWin02 import Ui_Form
'''
这个程序是展示了一个图片，我得去看看到底是怎么展示图片的了
emmmmmm 好吧 这个文件的命名都是有讲究的哈
这个文件的名称是 CallMainWindow02 那么，对应的py文件的话，就是MainWindow02的呀

在写代码的时候，类的名称可能会重复，所以在导入类的时候，一定要仔细写清楚导入的类 是 from 哪里的'''
class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
            
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()  
    sys.exit(app.exec_())  
