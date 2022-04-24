# coding:utf-8
# pyqt5_06按钮(QPushButton)
# author：Qinyuan

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class UI(QWidget):
    def __init__(self):
        super().__init__()
        # 创建垂直布局
        self.lay = QVBoxLayout()
        self.bt1_set()
        self.bt2_set()
        self.bt3_set()
        self.bt4_set()
        self.setWindowTitle("pyqt5_06按钮(QPushButton)")
        self.setLayout(self.lay)
    
    '''按钮1，普通文本按钮控件，切换按钮值并保持被按下后状态
    '''
    def bt1_set(self):
        # 创建按钮控件
        self.bt1 = QPushButton("text")
        # 设置按钮被选中
        self.bt1.setCheckable(True)
        # 在按钮状态之间切换
        self.bt1.toggle()
        # 当鼠标左键被按下，执行关联函数
        self.bt1.clicked.connect(lambda:self.p2(self.bt1))
        # 输出按钮的状态检测
        self.bt1.clicked.connect(self.p1)
        # 布局
        self.lay.addWidget(self.bt1)
        
    '''按钮2，带图标按钮,不切换按钮值，不保持被按下后的状态
    '''
    def bt2_set(self):
        # 创建按钮控件
        self.bt2 = QPushButton("Eason")
        # 设置按钮被选中
        # self.bt2.setCheckable(True)
        # 设置图标
        self.bt2.setIcon(QIcon(QPixmap(r"PyQt5\ICO\show.jpg")))
        # 当按钮被按下时，触发关联函数
        self.bt2.clicked.connect(lambda:self.p2(self.bt2))
        # 布局
        self.lay.addWidget(self.bt2)
        
    '''按钮3，不可按下按钮
    '''
    def bt3_set(self):
        # 创建按钮控件
        self.bt3 = QPushButton("无法选中")
        # 设置按钮不能被按下
        self.bt3.setEnabled(False)
        # 布局
        self.lay.addWidget(self.bt3)
        
    '''按钮4，默认状态为True按钮,设置Alt+E退出快捷键
    '''
    def bt4_set(self):
        # 创建按钮控件
        self.bt4 = QPushButton("&Exit")
        # 设置按钮默认状态太为True
        self.bt4.setDefault(True)
        # 当按钮被按下，触发关联函数
        self.bt4.clicked.connect(self.exit)
        self.lay.addWidget(self.bt4)
        
    # 输出显示按钮的按下和释放
    def p1(self):
        if self.bt1.isChecked():
            print("text 按钮打开！")
        else :
            print("text 按钮关闭！")
    # 输出当前被按下的按钮
    def p2(self,data):
        print("%s 被按下" % data.text())
    # 关闭程序
    def exit(self):
        print("关闭程序")
        sys.exit()
        
# 主函数
if __name__ == '__main__':
    app =  QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    GUI = UI()
    GUI.resize(300,200)
    GUI.show()
    sys.exit(app.exec_())