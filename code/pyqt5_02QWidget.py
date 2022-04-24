# coding:utf-8
# pyqt5_02WQidget
# author：Qinyuan


#######################
# QWidget()创建一个窗口
#######################
'''
import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QIcon
# 每个pyqt5都需要一个QApplication对象
app = QApplication(sys.argv)
# 添加图标
app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
# 实例化QWidget类，即常见窗口
GUI = QWidget()
# 设置窗口的大小
GUI.resize(400,200)
# 设置窗口的位置
GUI.move(300,200)
# 设置窗口标题栏显示
GUI.setWindowTitle('覃原学pyqt5')
# 显示界面
GUI.show()
# 退出程序
sys.exit(app.exec_())
'''

#######################
#  显示气泡提示信息
#######################
import sys
from PyQt5.QtWidgets import QWidget,QToolTip,QApplication
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt

# 使用继承类QWidget
class my_ui(QWidget):
    def __init__(self):
        super().__init__()
        self.set()
    def set(self):
        # 设置气泡字体、大小等
        '''
        宋体 SimSun
        黑体 SimHei
        微软雅黑 Microsoft YaHei
        微软正黑体 Microsoft JhengHei
        新宋体 NSimSun
        新细明体 PMingLiU
        细明体 MingLiU
        标楷体 DFKai-SB
        仿宋 FangSong
        楷体 KaiTi
        仿宋_GB2312 FangSong_GB2312
        楷体_GB2312 KaiTi_GB2312
        '''
        QToolTip.setFont(QFont("KaiTi",10))
        # 气泡的内容
        self.setToolTip('气泡提醒')
        # 设置窗口大小、位置
        self.setGeometry(400,200,300,200)
        self.setWindowTitle("覃原学pyqt5")
# 主函数
if __name__ == '__main__':
    # 创建app对象
    app = QApplication(sys.argv)
    # 设置图标
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    # 创建窗口
    GUI = my_ui()
    # 显示
    GUI.show()
    # 关闭
    sys.exit(app.exec_())