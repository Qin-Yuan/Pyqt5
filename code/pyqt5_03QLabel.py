# coding:utf-8
# pyqt5_03QLabel
# author：Qinyuan

####################
#  QLabel实例
####################
import sys
#                            app类        文本标签          布局      气泡提醒
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout,QToolTip
#                       常量库
from PyQt5.QtCore import Qt
#                       展示图片  调色板  图标  气泡提醒
from PyQt5.QtGui import QPixmap,QPalette,QIcon,QFont

# 继承QWidge类
class MyGui(QWidget):
    def __init__(self):
        # 初始化
        super().__init__()
        
    # 简单文本标签lab1，无超链接和关联函数
    def lab1(self):
        # 创建lab1标签
        lab1 = QLabel(self)
        # 设置文本内容
        lab1.setText("Eason专场")
        # 自动填充背景颜色
        lab1.setAutoFillBackground(True)
        # 使用QPalette调色板，设置背景颜色参数
        palette = QPalette()
        # 设置参数，注意这里Window中W是大写
        palette.setColor(QPalette.Window , Qt.blue)
        # 设置lab1背景参数
        lab1.setPalette(palette)
        # TextSelectableByMouse（鼠标选择文字），TextSelectableByKeyboard（键盘选择）
        lab1.setTextInteractionFlags(Qt.TextSelectableByMouse)
        # 设置在窗口中的位置,在水平中间
        lab1.setAlignment(Qt.AlignCenter)
        return lab1
    
    # 创建文本滑过触发标签，无超链接，有关联函数，当滑过标签时可以执行对应的函数
    def lab2(self):
        # 创建lab2的标签
        lab2 = QLabel(self)
        # 设置文本标签
        lab2.setText("<a href='#'> 覃原学PyQt5 </a>")
        # 将滑过触发标签与功能函数连接,注意这里使用linkHovered类
        lab2.linkHovered.connect(link_hovered)
        return lab2
    
    # 创建lab3图片标签，用于显示图片，无超连接、无关联函数 ，只显示图片信息
    def lab3(self):
        # 创建lab3
        lab3 = QLabel(self)
        # 设置位置
        lab3.setAlignment(Qt.AlignCenter)
        # 设置显示的图片
        lab3.setPixmap(QPixmap(r'PyQt5\ICO\show.jpg'))
        # 设置气泡提示的字体、大小
        QToolTip.setFont(QFont("KaiTi",13))
        # 气泡的内容
        lab3.setToolTip('这是陈奕迅！')
        return lab3
    
    # 创建lab4超链接点击文本标签，有超链接、无关联函数，可以通过点击文本进入链接
    def lab4(self):
        # 创建lab4
        lab4 = QLabel(self)
        # 设置超链接文本信息
        lab4.setText("<a href='https://baike.baidu.com/item/%E9%99%88%E5%A5%95%E8%BF%85/128029?fr=aladdin'> 点击了解更多Eason </a>")
        # 设置水平靠右对齐
        lab4.setAlignment(Qt.AlignRight)
        # 设置lab4允许访问超链接
        lab4.setOpenExternalLinks(True)
        return lab4

# 定义滑过对应的功能函数
def link_hovered():
        print("关注覃原，一起学习！")

#主函数
if __name__ == '__main__':
    # 创建一个app对象
    app = QApplication(sys.argv)
    # 设置图标
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    # 新建窗口
    GUI = MyGui()
    # 创建lab1
    lab1 = GUI.lab1()
    # 创建lab2
    lab2 = GUI.lab2()
    # 创建lab3
    lab3 = GUI.lab3()
    # 创建lab4
    lab4 = GUI.lab4()
    # 垂直布局，QHBoxLayout()是水平布局
    box = QVBoxLayout()
    # 控件中连入lab1
    box.addWidget(lab1)
    # 新建一个放置空间
    box.addStretch()
    box.addWidget(lab2)
    box.addStretch()
    box.addWidget(lab3)
    box.addStretch()
    box.addWidget(lab4)
    # 放置GUI标签
    GUI.setLayout(box)
    # 设置窗口标题
    GUI.setWindowTitle("QLable实例")
    # 显示窗口
    GUI.show()
    sys.exit(app.exec_())