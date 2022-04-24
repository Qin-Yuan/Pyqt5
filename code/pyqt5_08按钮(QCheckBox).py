# coding:utf-8
# pyqt5_08按钮(QChckBox)
# author：Qinyuan

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QB_UI(QWidget):
    def __init__(self):
        super().__init__()
        # 水平布局
        self.lay = QHBoxLayout()
        self.lay1 = QHBoxLayout()
        # 垂直布局,最终的布局
        self.mainlay = QVBoxLayout()
        # 创建QGroupBox, 第一个盒子
        self.box = QGroupBox("问题1")
        # 设置盒子的边框，True/False
        self.box.setFlat(False)
        # 第二个盒子
        self.box1 = QGroupBox("问题2")
        self.box1.setFlat(False)
        # 窗口主题
        self.setWindowTitle("pyqt5_08按钮(QChckBox)")
        # 执行函数
        self.tb_set()
        self.tb_set1()
        # 窗口布局
        self.setLayout(self.mainlay)
        self.resize(400,100)
        
    '''第一个选择题盒子
    '''
    def tb_set(self):
        
        '''创建按钮选项 1
        '''
        tb1 = QCheckBox("A.选项一")
        # 设置复选框状态为选中
        tb1.setChecked(True)
        # 设置状态改变触发函数
        tb1.stateChanged.connect(lambda:self.do(tb1))
        self.lay.addWidget(tb1)
        
        '''创建按钮选项 2
        '''
        tb2 = QCheckBox("B.选项二")
        # 设置 toggled 信号
        tb2.toggled.connect(lambda:self.do(tb2))
        self.lay.addWidget(tb2)
        
        '''创建按钮选项 3
        '''
        tb3 = QCheckBox("C.选项三")
        # 设置为三种状态按钮选项
        tb3.setTristate(True)
        # 设置
        tb3.setCheckable(Qt.PartiallyChecked)
        # 设置状态改变触发函数
        tb3.stateChanged.connect(lambda:self.do(tb3))
        self.lay.addWidget(tb3)
        
        '''添加到groupBox里
        '''
        # 设置box盒子布局
        self.box.setLayout(self.lay)
        # 将盒子添加到主布局里
        self.mainlay.addWidget(self.box)
        
    '''第二个选择题盒子
    '''
    def tb_set1(self):
        
        '''创建按钮选项 1
        '''
        tb1 = QCheckBox("&A.选项一")
        # 设置复选框状态为选中
        tb1.setChecked(False)
        # 设置状态改变触发函数
        tb1.stateChanged.connect(lambda:self.do(tb1))
        self.lay1.addWidget(tb1)
        
        '''创建按钮选项 2
        '''
        tb2 = QCheckBox("&B.选项二")
        # 设置 toggled 信号
        tb2.toggled.connect(lambda:self.do(tb2))
        self.lay1.addWidget(tb2)
        
        '''创建按钮选项 3
        '''
        tb3 = QCheckBox("&C.选项三")
        # 设置为三种状态按钮选项
        tb3.setTristate(True)
        # 设置
        tb3.setCheckable(Qt.PartiallyChecked)
        # 设置状态改变触发函数
        tb3.stateChanged.connect(lambda:self.do(tb3))
        self.lay1.addWidget(tb3)
        
        '''添加到groupBox里
        '''
        # 设置box盒子布局
        self.box1.setLayout(self.lay1)
        # 将盒子添加到主布局里
        self.mainlay.addWidget(self.box1)
        
    # 触发功能函数
    def do(self,tb):
        # 输出按钮、值
        print(tb.text()," : ",tb.isChecked())
    
# 主函数
if  __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    GUI = QB_UI()
    GUI.show()
    sys.exit(app.exec_())