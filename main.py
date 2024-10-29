from MyWindow import MyWindow
from MainWindow import Ui_MainWindow
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    app.setStyleSheet(
        """
        QPushButton
        {
             font: 25 10pt '微软雅黑 Light';
             color: rgb(255,255,255);
             background-color: rgb(44, 99, 50);
             border:none;
             border-radius:9px;
             padding:2px 4px;
        }
        
        QPushButton:hover
        {
            background-color: rgb(95, 139, 77);
        }
        
        QPushButton:pressed
        {
            background-color: rgb(90, 111, 88);
        }
        
        QLabel
        {
            font: 25 10pt '微软雅黑 Light';
            color: rgb(255,255,0);
        }
        
        QMainWindow
        {
            background-color: rgb(45, 45, 45)
        }
        
        """
    )
    #app.setWindowIcon(QIcon(r'./pic/icon.jpg'))
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    My_Ui = MyWindow(ui)

    sys.exit(app.exec_())





