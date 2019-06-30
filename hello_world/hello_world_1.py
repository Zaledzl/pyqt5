'''
This example shows an icon
in the titlebar of the window.
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

# 这是python的类，一个类里面有两个方法
# 面向对象编程最重要的三个部分是类(class)、数据和方法。我们创建了一个类的调用，这个类继承自QWidget。
# 这就意味着，我们调用了两个构造器，一个是这个类本身的，一个是这个类继承的。super()构造器方法返回父级的对象。__init__()方法是构造器的一个方法
class Example(QWidget):

    # 这个方法是构造方法
    def __init__(self):
        super().__init__()

        # 使用initUI()方法创建一个GUI
        self.initUI()

    # 三个方法都继承自QWidget类。setGeometry()有两个作用：把窗口放到屏幕上并且设置窗口大小。
    # 参数分别代表屏幕坐标的x、y和窗口大小的宽、高。也就是说这个方法是resize()和move()的合体。
    # 最后一个方法是添加了图标。先创建一个QIcon对象，然后接受一个路径作为参数显示图标
    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('a.jpg'))

        self.show()

# 应用和示例的对象创立，主循环开始
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())