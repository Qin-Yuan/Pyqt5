# coding:utf-8
# pyqt5_19窗口绘图(QBrush)
# author：Qinyuan

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt5_19窗口绘图(QBrush)")
        # 设置窗口位置、窗口大小
        self.setGeometry(300,300,400,270)
    '''Qt参数
    NoBrush = 0 # type: 'Qt.BrushStyle' 无图案
    SolidPattern = 1 # type: 'Qt.BrushStyle' 实心图案
    Dense1Pattern = 2 # type: 'Qt.BrushStyle' 密实图案1
    Dense2Pattern = 3 # type: 'Qt.BrushStyle' 密实图案2
    Dense3Pattern = 4 # type: 'Qt.BrushStyle' 密实图案3
    Dense4Pattern = 5 # type: 'Qt.BrushStyle' 密实图案4
    Dense5Pattern = 6 # type: 'Qt.BrushStyle' 密实图案5
    Dense6Pattern = 7 # type: 'Qt.BrushStyle' 密实图案6
    Dense7Pattern = 8 # type: 'Qt.BrushStyle' 密实图案7
    HorPattern = 9 # type: 'Qt.BrushStyle' 水平线图案
    VerPattern = 10 # type: 'Qt.BrushStyle' 垂直线图案
    CrossPattern = 11 # type: 'Qt.BrushStyle' 十字线图案
    BDiagPattern = 12 # type: 'Qt.BrushStyle' 左斜线图案
    FDiagPattern = 13 # type: 'Qt.BrushStyle' 右倾线图案
    DiagCrossPattern = 14 # type: 'Qt.BrushStyle' 倾斜十字线图案
    LinearGradientPattern = 15 # type: 'Qt.BrushStyle' 线性渐变图案
    RadialGradientPattern = 16 # type: 'Qt.BrushStyle' 径向渐变图案
    ConicalGradientPattern = 17 # type: 'Qt.BrushStyle' 圆锥渐变图案
    TexturePattern = 24 # type: 'Qt.BrushStyle' 纹理图案
    '''
    '''绘制图执行函数'''
    def paintEvent(self,event):
        p = QPainter()
        # 在 begin 和 end 之间进行绘制
        p.begin(self)
        self.draw(p)
        p.end()
    '''绘制功能函数'''
    def draw(self,p):
        '''1\实心团，也可以直接填写对应的值1 '''
        brush = QBrush(Qt.SolidPattern)
        p.setBrush(brush)
        p.drawRect(10,15,90,60)
        
        '''2\密实图案1 '''
        brush = QBrush(Qt.Dense1Pattern)
        p.setBrush(brush)
        p.drawRect(130,15,90,60)
        
        '''3\密实图案2 '''
        brush = QBrush(Qt.Dense2Pattern)
        p.setBrush(brush)
        p.drawRect(250,15,90,60)
        
        '''4\密实图案3 '''
        brush = QBrush(Qt.Dense3Pattern)
        p.setBrush(brush)
        p.drawRect(10,105,90,60)
        
        '''5\倾斜十字线图案 重叠在4上 '''
        brush = QBrush(Qt.DiagCrossPattern)
        p.setBrush(brush)
        p.drawRect(10,105,90,60)
        
        '''6\ 密实图案5'''
        brush = QBrush(Qt.Dense5Pattern)
        p.setBrush(brush)
        p.drawRect(130,105,90,60)
        
        '''7\密实图案6 '''
        brush = QBrush(Qt.Dense6Pattern)
        p.setBrush(brush)
        p.drawRect(250,105,90,60)
        
        '''8\水平线图案 '''
        brush = QBrush(Qt.HorPattern)
        p.setBrush(brush)
        p.drawRect(10,195,90,60)
        
        '''9\垂直线图案 '''
        brush = QBrush(Qt.VerPattern)
        p.setBrush(brush)
        p.drawRect(130,195,90,60)
        
        '''10\左斜线图案 '''
        brush = QBrush(Qt.BDiagPattern)
        p.setBrush(brush)
        p.drawRect(250,195,90,60)
    
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