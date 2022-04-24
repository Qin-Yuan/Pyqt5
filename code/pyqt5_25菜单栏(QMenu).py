# coding:utf-8
# pyqt5_25菜单栏(QMenu)
# author：Qinyuan

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_main()
        self.setWindowTitle("pyqt5_25菜单栏(QMenu)")
        self.resize(400,200)
    
    def set_main(self):
        '''第一个下拉菜单'''
        bar = self.menuBar()
        file = bar.addMenu("文件")
        file.addAction("新建")
        save = QAction("保存",self)
        save.setShortcut("Ctrl+s")
        file.addAction(save)
        file.addAction("退出")
        file.triggered[QAction].connect(self.file_do)
        '''第二个下拉菜单'''
        bar = self.menuBar()
        edit = bar.addMenu("编辑")
        edit.addAction("复制")
        edit.addAction("粘贴")
        edit.triggered[QAction].connect(self.file_do)
        '''帮助下拉菜单'''
        bar = self.menuBar()
        help = bar.addMenu("帮助")
        help.addAction("关于")
        help.triggered[QAction].connect(self.file_do)
    # 处理函数
    def file_do(self,q):
        text = q.text()
        if text=="退出":
            self.close()
    
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