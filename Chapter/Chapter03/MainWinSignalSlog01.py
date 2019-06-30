# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinSignalSlog01.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# 这个类是被引用的
# 这个类下面写了两个方法的呢
# 信号和槽 可以写在逻辑文件里面，也可以写在界面文件里面的呀  但是一般来讲是要写在逻辑文件里面的
class Ui_Form(object):
    # 这个方法就是来做个界面的
    # 我现在明白了 这个方法的名称就是这个样子的呀  setupUi  在逻辑程序中是用到了的 self.setupUi(self)
    # 讲实话，我现在搞不太懂 这个Form参数是用来干嘛的，逻辑文件调用的时候，也没有输入参数过来的呀
    def setupUi(self, Form):
        # 这个是大窗口的标题的名称
        Form.setObjectName("Form")
        Form.resize(452, 296)
        # 这里参数用到了Form 就先不管了
        self.closeWinBtn = QtWidgets.QPushButton(Form)
        self.closeWinBtn.setGeometry(QtCore.QRect(150, 80, 121, 31))
        # 这个给button的命名
        self.closeWinBtn.setObjectName("closeWinBtn")
        # 这里用到了下面写的那个函数的呀
        # 搞不太懂这个 翻译 是什么意思，感觉以前学的时候也没用到的呀
        self.retranslateUi(Form)
        # self. 谁.动作.connect.（slot）
        # 槽函数如果是已经有了的话，那么就是直接调用就行了，没有的话，要自己写的
        self.closeWinBtn.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # emmmmm 这里用了QtCore.QCoreApplication.translate 这个很少见，先不管它
    # 不过在上面的那个类中用到了啊
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.closeWinBtn.setText(_translate("Form", "关闭窗口"))

