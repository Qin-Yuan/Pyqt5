# coding:utf-8
# pyqt5_17窗口绘图(QPainter)
# author：Qinyuan

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class  UI(QWidget):
    def __init__(self):
        super().__init__()
        self.text = "覃原学Pyqt5!"
        self.setWindowTitle("pyqt5_17窗口绘图(QPainter)")
        
    '''画笔函数，默认会执行paintEvent'''
    def paintEvent(self,event):
        p = QPainter(self)
        # 绘制必须放置在begin和end之间
        p.begin(self)
        # 定义绘制方法
        self.drawText(event,p)
        self.drawPoint(p)
        p.end()
    '''文本绘制'''
    def drawText(self,event,p):
        # 设置画笔颜色
        p.setPen(Qt.red)
        # 设置字体
        p.setFont(QFont('KaiTi',50))
        # 绘制文字, event.rect表示以(0,0)为基准点，放置窗口中间
        p.drawText(event.rect(),Qt.AlignCenter,self.text)
        # 绘制文字，起始点为(50,400)
        p.drawText(50,400,self.text)
    '''图形绘制（正弦函数）'''
    def drawPoint(self,p):
        p.setPen(Qt.blue)
        for i in range(2500):
            # 绘制正弦函数
            x = 100*(2*i/1000)+60
            y = -50*math.sin((x-60)*math.pi/50)+100
            # 绘制点云
            p.drawPoint(x,y)
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