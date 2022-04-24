# coding:utf-8
# pyqt5_28打印机(QPrinter)
# author：Qinyuan

from PyQt5.QtGui import QImage,QIcon,QPixmap, QPainter
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QSizePolicy,QAction
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog
from PyQt5.QtCore import Qt
import sys

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt5_28打印机(QPrinter)")
        self.set_main()
        self.resize(500,300)
        
    '''设置主窗口'''
    def set_main(self):
        self.imageLable = QLabel()
        self.imageLable.setSizePolicy(
            QSizePolicy.Ignored,QSizePolicy.Ignored
        )
        self.setCentralWidget(self.imageLable)
        self.image = QImage()
        # 创建一个QAction,工具按键
        self.printaction = QAction(QIcon("PyQt5\ICO\打印.ico"),self.tr("打印"),self)
        self.printaction.setShortcut("Ctrl+P")
        self.printaction.setStatusTip(self.tr("打印"))
        self.printaction.triggered.connect(self.do)
        # 创建一个菜单menu
        printmenu = self.menuBar().addMenu(self.tr("打印"))
        printmenu.addAction(self.printaction)
        # 创建一个工具栏
        filetoolBar = self.addToolBar("Print")
        filetoolBar.addAction(self.printaction)
        # 判断文件路径
        if self.image.load("./"):
            self.imageLable.setPixmap(QPixmap.fromImage(self.image))
            self.resize(self.image.width(),self.image.height())
    '''打印关联函数'''
    def do(self):
        printer = QPrinter()
        printdialog = QPrintDialog(printer,self)
        if printdialog.exec_():
            painter = QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(),Qt.KeepAspectRatio)
            painter.setViewport(rect.x(),rect.y(),size.width(),size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0,0,self.image)
            
if __name__ == '__main__':
    # 创建app对象
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    # 创建窗口
    GUI = UI()
    # 显示
    GUI.show()
    sys.exit(app.exec_())