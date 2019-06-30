# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from MainForm2 import Ui_MainWindow
from ChildrenForm2 import Ui_ChildrenForm
'''
思考一下这个逻辑哈
是这个样子的
这个就是一个普通的主窗口
然后又一个按钮，可以触发信号，然后让子窗口显示的哈'''


class MainForm(QMainWindow, Ui_MainWindow):
    # 这个是必要的，是个构造函数的哈
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        # self.child = children()生成子窗口实例self.child
        self.child = ChildrenForm()

        # 这个是不太重要的几个东西的 信号与槽 不过看这个的话，会对怎么写代码更加熟悉的
        # 菜单的点击事件，当点击关闭菜单时连接槽函数 close()
        self.fileCloseAction.triggered.connect(self.close)
        # 菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()
        self.fileOpenAction.triggered.connect(self.openMsg)

        # 可以的，现在就学会怎么添加子窗口了，可以的
        # 点击actionTst,子窗口就会显示在主窗口的MaingridLayout中
        self.addWinAction.triggered.connect(self.childShow)

    def childShow(self):
        # 添加子窗口
        # 中间的这个参数的话，是布局的名称呢
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files (*.txt)")
        # 在状态栏显示文件地址
        self.statusbar.showMessage(file)


class ChildrenForm(QWidget, Ui_ChildrenForm):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
