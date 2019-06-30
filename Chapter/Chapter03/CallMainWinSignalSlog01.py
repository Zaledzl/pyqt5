import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Chapter.Chapter03.MainWinSignalSlog01 import Ui_Form

'''
这个是一个按钮，点击之后会自动关闭整个窗口
如果想迅速看 这个类是在哪里 可以 按住Ctrl 然后用鼠标左键点击
就会直接进入对应的类'''
class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())