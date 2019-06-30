'''
This program creates a toolbar.
The toolbar has one action, which
terminates the application, if triggered.
'''

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 和上面的菜单栏差不多，这里使用了一个行为对象，这个对象绑定了一个标签，一个图标和一个快捷键。
        # 这些行为被触发的时候，会调用QtGui.QMainWindow的quit方法退出应用。
        exitAct = QAction(QIcon('a.jpg'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        # 把工具栏展示出来
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())