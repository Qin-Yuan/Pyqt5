import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import Ui_page_1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_page_1.Ui_page_1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

