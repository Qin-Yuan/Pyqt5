# coding:utf-8
# pyqt5_01主窗口
# author：Qinyuan

#######################
#   QMainWindow主窗口
#######################
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

#使用继承类
class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        # 继承类初始化
        super(MainWindow,self).__init__(parent)
        # 设置窗口尺寸大小
        self.resize(500,300)
        # 获得状态栏对象
        self.status = self.statusBar()
        # 状态栏对象获取成功后，设置底部消息提示，后面的参数代表显示 5s
        self.status.showMessage("Pyqt5_01窗口",5000)
        # 窗口标题设置
        self.setWindowTitle("覃原学PyQt5")
        
# 主函数显示
if __name__ == '__main__':
    # 每一个pyqt5程序都需要一个QApplication()对象，sys.argv是一个命令行参数列表
    UI = QApplication(sys.argv)
    # 设置图标，使用相对路径
    UI.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    # 创建窗口
    form = MainWindow()
    # 显示窗口，并等待手动关闭或程序异常
    form.show()
    # 持续显示直到手动关闭,程序运行结束exec()返回0,然后关闭整个程序
    sys.exit(UI.exec())

#############################
#   QDesktopWidget()窗口居中
#############################
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
from PyQt5.QtGui import QIcon
#继承主窗口类
class m_window(QMainWindow):
    def __init__(self,parent=None):
        # 类初始化
        super(m_window,self).__init__(parent)
        # 设置窗口尺寸大小
        self.resize(500,300)
        # 获得状态栏对象
        self.status = self.statusBar()
        # 状态栏对象获取成功后，设置底部消息提示，后面的参数代表显示 5s
        self.status.showMessage("pyqt5_窗口居中",5000)
        # 设置窗口标题
        self.setWindowTitle("覃原学Pyqt5")
        # 执行窗口移动居中函数
        self.center()
    # 窗口居中函数
    def center(self):
        # 获取显示屏的尺寸大小
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口的尺寸
        size = self.geometry()
        # 将窗口移动到中间位置，即获取显示屏的尺寸，通过计算窗口尺寸得到中心位置
        self.move((screen.width()-size.width())/2,(screen.height()-size.height()/2))
# 主函数
if __name__ == '__main__':
    # 每一个pyqt5程序都需要一个QApplication()对象，sys.argv是一个命令行参数列表
    UI = QApplication(sys.argv)
    # 设置图标，使用相对路径
    UI.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    # 创建窗口
    GUI = m_window()
    # 显示窗口,并会一直等待关闭，或者出现异常
    GUI.show()
    # 持续显示直到手动关闭,程序运行结束exec()返回0,然后关闭整个程序
    sys.exit(UI.exec())