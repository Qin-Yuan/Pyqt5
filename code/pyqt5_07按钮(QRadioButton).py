# coding:utf-8
# pyqt5_07按钮(QRadioButton)
# author：Qinyuan

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QR_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.lay = QHBoxLayout()
        # 创建按钮
        self.bt1_set()
        # 创建按钮
        self.setLayout(self.lay)
        # 设置窗口标题
        self.setWindowTitle("pyqt5_06按钮(QRadioButton)")
        # 设置窗口大小
        self.resize(200,150)
        
    def bt1_set(self):
        # 设置选择1组按钮的第一个选择
        self.bt1 = QRadioButton("男")
        # 设置能保存按钮状态
        self.bt1.setCheckable(True)
        # 设置 toggled 信号
        self.bt1.toggled.connect(lambda:self.DO1(self.bt1))
        self.lay.addWidget(self.bt1)
        
        # 设置选择1组按钮的第二个按钮
        self.bt2 = QRadioButton("女")
        # 设置能保持按钮状态
        self.bt2.setCheckable(True)
        # 设置 toggled  信号
        self.bt2.toggled.connect(lambda:self.DO1(self.bt2))
        self.lay.addWidget(self.bt2)
    
    # 触发关联函数
    def DO1(self,bt):
        # 判断组按钮此时选中的按钮
        if bt.text() == '男':
            # 判断是否被选择
            if bt.isChecked() == True:
                print("您选择的性别是：男")
            else:
                pass
        elif bt.text() == '女':
            # 判断是否被选择
            if bt.isChecked() == True:
                print("您选择的性别是：女")
            else:
                pass

# 主函数
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    GUI = QR_UI()
    GUI.show()
    sys.exit(app.exec_())