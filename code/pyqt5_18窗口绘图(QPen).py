# coding:utf-8
# pyqt5_18窗口绘图(QPen)
# author：Qinyuan

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt5_18窗口绘图(QPen)")
        # 设置窗口位置、窗口大小
        self.setGeometry(300,300,280,270)
    
    '''绘制图执行函数'''
    def paintEvent(self,event):
        p = QPainter()
        # 在 begin 和 end 之间进行绘制
        p.begin(self)
        self.draw(p)
        p.end()
    '''绘制功能函数'''
    def draw(self,p):
        '''初始化为直线'''
        # 创建绘制笔, 参数分别为画笔颜色、粗细、风格(这里是直线)
        pen = QPen(Qt.black,3,Qt.SolidLine)
        # 将pen设置为p的画笔风格
        p.setPen(pen)
        # 绘制，参数：x轴位置、起点y轴、长度、终点y轴
        p.drawLine(20,40,250,40)
        '''绘制均衡虚线'''
        pen.setStyle(Qt.DashLine)
        p.setPen(pen)
        p.drawLine(20,80,250,80)
        '''绘制短横+点线'''
        pen.setStyle(Qt.DashDotLine)
        p.setPen(pen)
        p.drawLine(20,120,250,120)
        '''绘制点线'''
        pen.setStyle(Qt.DotLine)
        # 设置画笔颜色
        pen.setColor(Qt.red)
        p.setPen(pen)
        p.drawLine(20,160,250,160)
        '''绘制短横+双点线'''
        pen.setStyle(Qt.DashDotDotLine)
        p.setPen(pen)
        p.drawLine(20,200,250,200)
        '''自定义绘制线'''
        pen.setStyle(Qt.CustomDashLine)
        # 自定义风格，参数：线长、间隔、线长、间隔
        pen.setDashPattern([1,3,4,10])
        p.setPen(pen)
        p.drawLine(20,240,250,240)
# 主函数
if __name__ == '__main__':
    # 创建app对象
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    # 创建窗口
    GUI = UI()
    # 显示
    GUI.show()
    sys.exit(app.exec_())