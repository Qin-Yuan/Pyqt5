# coding:utf-8
# pyqt5_13对话框(QMessageBox)
# author：Qinyuan

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt5_13对话框(QMessageBox)")
        self.lay = QVBoxLayout()
        self.resize(300,200)
        self.set_item()
        self.setLayout(self.lay)
        
    '''创建下拉列表'''
    def set_item(self):
        # 创建 QComboBox 下拉列表框
        cb = QComboBox()
        # 添加下拉列表值
        cb.addItems(['提示','提问','警告','错误','关于'])
        # 当用户选中一个下拉选项时触发信号 
        cb.activated.connect(lambda:self.set_QM(cb))
        self.lay.addWidget(cb)
        
    '''弹框弹出处理函数'''
    def set_QM(self,cb):
        # 将按钮类型存放在元组中
        button = (  QMessageBox.Ok,
                    QMessageBox.Cancel,
                    QMessageBox.Yes,
                    QMessageBox.No,
                    QMessageBox.Abort,
                    QMessageBox.Retry,
                    QMessageBox.Ignore)
        if cb.currentText()=='提示':
            QMessageBox.information(self,'提示',"覃原学pyqt5",button[0]|button[1],button[0])
        elif cb.currentText()=='提问':
            QMessageBox.question(self,'提问',"覃原学pyqt5",button[2]|button[3],button[2])
        elif cb.currentText()=='警告':
            QMessageBox.warning(self,'警告',"覃原学pyqt5",button[2]|button[3],button[2])
        elif cb.currentText()=='错误':
            QMessageBox.critical(self,'错误',"覃原学pyqt5",button[2]|button[3],button[2])
        elif cb.currentText()=='关于':
            QMessageBox.about(self,'关于',"覃原学pyqt5")
            
if __name__ == '__main__':
    app =QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    GUI = UI()
    GUI.show()
    sys.exit(app.exec_())