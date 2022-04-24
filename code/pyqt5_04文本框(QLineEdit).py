# coding:utf-8
# pyqt5_04文本框(QLineEdit)
# author：Qinyuan

############################
#   QLineEdit()单行文本输入
############################
import sys,time
from typing import Text
from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout
from PyQt5.QtGui import QIcon,QIntValidator,QDoubleValidator,QRegExpValidator,QFont
from PyQt5.QtCore import Qt

# 继承类QWidget
class LineEdit(QWidget):
    def __init__(self):
        super().__init__()
        
    '''创建简单文本框，只控制文件显示格式，不限制输入内容
    '''
    def edit1(self):
        # 实例化表单布局
        lay = QFormLayout()
        
        '''正常显示输入的字符'''
        Normal = QLineEdit()
        # 文本框前的标题
        lay.addRow('Normal',Normal)
        # 设置浮现文字
        Normal.setPlaceholderText("正常显示")
        # 设置输入显示效果
        Normal.setEchoMode(QLineEdit.Normal)
        
        '''不显示任何输入的字符，比如密码输入，并且会保密密码长度'''
        NoECho = QLineEdit()
        # 文本框前的标题
        lay.addRow('NoECho',NoECho)
        # 设置浮现文字
        NoECho.setPlaceholderText("绝对保密")
        # 设置输入显示效果
        NoECho.setEchoMode(QLineEdit.NoEcho)
        
        '''显示与平台相关的密码掩码字符，不会显示实际输入的字符'''
        Password = QLineEdit()
        # 文本框前的标题
        lay.addRow('Password',Password)
        # 设置浮现文字
        Password.setPlaceholderText("掩码字符")
        # 设置输入显示效果
        Password.setEchoMode(QLineEdit.Password)
        
        '''在编辑时显示字符，负责显示密码类型的输入'''
        PasswordEcho = QLineEdit()
        # 文本框前的标题
        lay.addRow('PasswordEchoOnEdit',PasswordEcho)
        # 设置浮现文字
        PasswordEcho.setPlaceholderText("编辑时显示")
        # 设置输入显示效果
        PasswordEcho.setEchoMode(QLineEdit.PasswordEchoOnEdit) 
        
        # 返回表单布局
        return lay
    
    '''添加验证器控制输入数据类型
    '''
    def edit2(self):
        # 实例化表单布局
        lay = QFormLayout()
        
        '''正常显示输入的字符'''
        Normal = QLineEdit()
        # 文本框前的标题
        lay.addRow('任何数据',Normal)
        # 设置浮现文字
        Normal.setPlaceholderText("可以输入任何数据")
        # 设置输入显示效果
        Normal.setEchoMode(QLineEdit.Normal)
        
        '''只能输入整数'''
        IntEdit = QLineEdit()
        # 文本框前的标题
        lay.addRow('整数',IntEdit)
        # 设置浮现文字
        IntEdit.setPlaceholderText("只能输入整数")
        # 设置输入显示效果
        # IntEdit.setEchoMode(QLineEdit.NoEcho)
        # 整数输入
        intrange = QIntValidator(self)
        # 设置整数输入范围
        intrange.setRange(1,99)
        # 设置文本框校验器
        IntEdit.setValidator(intrange)
        
        '''只能输入浮点数'''
        DoubleEdit = QLineEdit()
        # 文本框前的标题
        lay.addRow('浮点数',DoubleEdit)
        # 设置浮现文字
        DoubleEdit.setPlaceholderText("只能输入浮点数")
        # 设置输入显示效果
        # DoubleEdit.setEchoMode(QLineEdit.Password)
        # 浮点数输入
        doublerange = QDoubleValidator(self)
        # 设置范围
        doublerange.setRange(-360,360)
        doublerange.setNotation(QDoubleValidator.StandardNotation)
        # 设置精确小数点后两位
        doublerange.setDecimals(2)
        # 设置文本框校验器
        DoubleEdit.setValidator(doublerange)
        
        '''字母和数字'''
        RegEdit = QLineEdit()
        # 文本框前的标题
        lay.addRow('字母和数字',RegEdit)
        # 设置浮现文字
        RegEdit.setPlaceholderText("输入字母和数字")
        # 设置输入显示效果
        # PasswordEcho.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        # 设置正则表达式
        r = QRegExp("[a-zA-Z0-9]+$")
        # 创建校验对象
        regrange = QRegExpValidator(self)
        # 设置正则范围
        regrange.setRegExp(r)
        # 设置文本框校验器
        RegEdit.setValidator(regrange)
        
        # 返回表单布局
        return lay
    
    '''输入掩码,固定输入格式
    '''
    def edit3(self):
        # 实例化表单
        lay = QFormLayout()
        
        # 创建4个文本框
        IP = QLineEdit()
        MAC = QLineEdit()
        DATA = QLineEdit()
        LICE = QLineEdit()
        
        # IP地址掩码,0会消失用下划线代替
        IP.setInputMask('000.000.000.000;_')
        # MAC地址掩码
        MAC.setInputMask('HH:HH:HH:HH:HH:HH;_')
        # 日期掩码
        DATA.setInputMask('0000-00-00')
        # 许可证掩码
        LICE.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')
        
        # 表单布局文本框
        lay.addRow("IP地址",IP)
        lay.addRow("MAC地址",MAC)
        lay.addRow("日期",DATA)
        lay.addRow("许可证",LICE)
        
        # 返回布局
        return lay
    
    '''综合运用，制作一个创建新用户界面
    '''
    def edit4(self):
        # 创建表单布局
        lay = QFormLayout()
        
        '''
        用户名设置文本框
        允许输入任何字符，居中
        '''
        name = QLineEdit()
        lay.addRow("用户名", name)                  # 文本框标题
        name.setPlaceholderText("请输入用户名")     # 浮现文字
        name.setMaxLength(8)                       # 最大输入字符
        name.setAlignment(Qt.AlignCenter)          # 位置居中
        name.setFont(QFont("KaiTi",10))            # 设置字体
        
        '''
        手机号设置文本框
        使用掩码格式，只允许输入0~9,位置居中
        '''
        tel = QLineEdit()
        lay.addRow("手机号",tel)
        tel.setInputMask("+99 999-9999-9999")     # 只能输入0~9
        tel.setAlignment(Qt.AlignCenter)          # 居中
        
        '''
        密码第一次设置
        使用保密显示格式，QLineEdit.Password ; 只能输入字符和数字 ; 位置居中
        '''
        self.num1 = QLineEdit()
        lay.addRow("新密码", self.num1)
        self.num1.setPlaceholderText("请输入新密码")   # 设置浮现文字
        self.num1.setEchoMode(QLineEdit.Password)     # 密码显示保密模式
        r = QRegExp("[a-zA-Z0-9]+$")                  # 正则表达式
        reg = QRegExpValidator(self)                  # 创建校验对象
        reg.setRegExp(r)                              # 设置范围
        self.num1.setValidator(reg)                   # 设置文本
        self.num1.setMaxLength(16)                    # 最大输入字符
        self.num1.setAlignment(Qt.AlignCenter)        # 位置居中
        
        '''
        密码第二次设置
        使用保密显示格式，QLineEdit.Password ; 只能输入字符和数字 ; 位置居中
        '''
        self.num2 = QLineEdit()
        lay.addRow("确认密码", self.num2)
        self.num2.setPlaceholderText("请再次输入新密码")   # 设置浮现文字
        self.num2.setEchoMode(QLineEdit.Password)         # 密码显示保密模式
        r1 = QRegExp("[a-zA-Z0-9]+$")                     # 正则表达式
        reg1 = QRegExpValidator(self)                     # 创建校验对象
        reg1.setRegExp(r1)                                # 设置范围
        self.num2.setValidator(reg1)                      # 设置文本
        self.num2.setMaxLength(16)                        # 最大输入字符
        self.num2.setAlignment(Qt.AlignCenter)            # 位置居中
        self.num2.editingFinished.connect(self.enter)
        
        '''
        创建结果显示，只读模式
        如果创建成功，输出 创建成功；否则输出创建失败
        '''
        self.text = QLineEdit()
        lay.addRow("创建结果", self.text)
        self.text.setReadOnly(True)               # 只读模式
        self.text.setAlignment(Qt.AlignCenter)    # 居中
        
        '''
        返回表单布局
        '''
        return lay
    
    # 再次输入密码后处理函数，如果前后密码一致，在结果框显示 创建成功；否则输出 创建失败
    def enter(self):
        # 判断前后两次输入的密码是否相等
        if self.num1.text() == self.num2.text() :
            self.text.setText("创建成功")
            
        else :
            self.text.setText("前后密码不一致")
            # 清除原输入内容
            self.num1.clear()               
            self.num2.clear()
        
# 主函数
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    # 初始化一个窗口
    GUI = LineEdit()
    # 显示窗口标题
    GUI.setWindowTitle("04_文本框")
    # 创建表单布局,修改这里可以切换创建的表单
    lay = GUI.edit4()
    # 布局
    GUI.setLayout(lay)
    GUI.resize(350,50)
    # 显示
    GUI.show()
    sys.exit(app.exec_())