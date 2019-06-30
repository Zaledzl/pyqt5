'''
2019年6月26日21:14:42
通过这个 pyqt5 工程来学习 pyqt5
顺便作为未来写工程时候的参考
https://github.com/maicss/PyQt5-Chinese-tutorial/blob/master/hello_world.md
这里面的教程很棒，很感谢
'''
'''
In this example, we create a simple
window in PyQt5.
'''

# sys模块包含了与Python解释器和它的环境有关的函数
# 这里引入了PyQt5.QtWidgets模块，这个模块包含了基本的组件
import sys
from PyQt5.QtWidgets import QApplication, QWidget

#  一个python的文件有两种使用的方法，第一是直接作为脚本执行，第二是import到其他的python脚本中被调用（模块重用）执行。
#  因此if __name__ == 'main': 的作用就是控制这两种情况执行代码的过程，
#  在if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，而import到其他脚本中是不会被执行的。
if __name__ == '__main__':

    # 每个PyQt5应用都必须创建一个应用对象。sys.argv是一组命令行参数的列表。Python可以在shell里运行，这个参数提供对脚本控制的功能。
    app = QApplication(sys.argv)

   # QWidge控件是一个用户界面的基本控件，它提供了基本的应用构造器。默认情况下，构造器是没有父级的，没有父级的构造器被称为窗口（window）
    w = QWidget()

    # resize()方法能改变控件的大小，这里的意思是窗口宽250px，高150px
    w.resize(250, 150)

    # move()是修改控件位置的的方法。它把控件放置到屏幕坐标的(300, 300)的位置。注：屏幕坐标系的原点是屏幕的左上角
    w.move(300, 300)

    # 给这个窗口添加了一个标题，标题在标题栏展示（虽然这看起来是一句废话，但是后面还有各种栏，还是要注意一下，多了就蒙了）
    w.setWindowTitle('Simple')

    w.show()

    # 最后，我们进入了应用的主循环中，事件处理器这个时候开始工作。主循环从窗口上接收事件，并把事件传入到派发到应用控件里。
    # 当调用exit()方法或直接销毁主控件时，主循环就会结束。sys.exit()方法能确保主循环安全退出。外部环境能通知主控件怎么结束。
    # exec_()之所以有个下划线，是因为exec是一个Python的关键字
    # app.exec_()是指程序一直循环运行直到主窗口被关闭终止进程（如果没有这句话，程序运行时会一闪而过）
    sys.exit(app.exec_())