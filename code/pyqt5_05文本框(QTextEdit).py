# coding:utf-8
# pyqt5_05文本框(QTextEdit)
# author：Qinyuan

from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QVBoxLayout
from PyQt5.QtGui import QIcon
import sys

# 使用继承类
class myText(QWidget):
    def __init__(self):
        super().__init__()
        # 垂直方向上排列布局
        self.lay = QVBoxLayout()
        # 创建普通文本
        self.text1 = QTextEdit()
        # 创建HTML文本
        self.text2 = QTextEdit()
        # 运行初始化函数
        self.edit()
        
    # 文本框配置函数
    def edit(self):
        # 普通文本内容设置
        self.text1.setPlainText("@ 覃原学习PyQt5!\n"*20)
        # HTML文本内容设置
        self.text2.setHtml("<font color='green' size='10'><green>@关注覃原, 一起学习!</font>")
        # 文本框排列
        self.lay.addWidget(self.text1)
        self.lay.addWidget(self.text2)
        # 初始化界面
        self.setLayout(self.lay)
        
# 主函数
if __name__ == '__main__':
    # 创建app对象
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    # 创建窗口
    GUI = myText()
    # 设置窗口主题
    GUI.setWindowTitle("pyqt5_05文本框(QTextEdit)")
    # 显示
    GUI.show()
    sys.exit(app.exec_())