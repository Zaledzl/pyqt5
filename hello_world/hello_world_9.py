'''
This program creates a checkable menu.
'''

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 让状态栏显示 Ready
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        # 创建一个 Menu
        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        # 用checkable选项创建一个能选中的菜单。
        viewStatAct = QAction('View statusbar', self, checkable=True)

        #在状态栏显示信息
        viewStatAct.setStatusTip('View statusbar')
        # 默认选中 True
        viewStatAct.setChecked(True)

        #  # 当执行这个指定的动作时，就触发了一个事件。
        viewStatAct.triggered.connect(self.toggleMenu)

        # 把新建的submenu添加到menu里面
        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self, state):

        # 依据选中状态切换状态栏的显示与否。
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())