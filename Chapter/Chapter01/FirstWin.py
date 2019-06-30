# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

# 这句话表明，这个程序只在这个地方可以运行，import到其他地方也不能运行的
if __name__ == '__main__':

    # 创建了app 是必要的  app = QApplication(sys.argv)
    app = QApplication(sys.argv)
    # 创建了一个按钮，并命名了按钮的显示名称
    btn = QPushButton("Hello PyQt5")
    # 这是一个连接函数，谁被怎样，然后连接，连接到一个函数    QCoreApplication.instance(),quit
    btn.clicked.connect(QCoreApplication.instance().quit)
    # 指定 大小，位置，展示
    btn.resize(400,100)
    btn.move(50,50)
    btn.show()
    # 这个程序在关闭之前一直保持运行
    sys.exit(app.exec_())
