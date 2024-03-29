# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from SettingPage import Setting_MainWindow
sys.path.insert(0, 'Models')
import Internet,App,Basic,CMD,ComputerFunction


requestCMD = ['mở cài đặt','mở cài đặt âm thanh','mở cài đặt display''mở cài đặt autoplay','mở cài đặt usb','mở cài đặt pen and windows ink',
              'mở cài đặt touchpad','mở cài đặt mobile-devices','mở cài đặt mouse','mở cài đặt printers','mở cài đặt bluetooth','mở file explorer',
              'mở task manager','mở máy tính','mở control panel','mở quản lí ảnh','mở camera','mở lịch','mở quản lí đồng hồ','mở bản đồ','mở outlook']

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 597)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CameraFrame = QtWidgets.QFrame(self.centralwidget)
        self.CameraFrame.setGeometry(QtCore.QRect(0, 0, 571, 541))
        self.CameraFrame.setStyleSheet("background-color:#0085FF;\n"
"border-radius:10px;\n"
"border:0.5px solid;")
        self.CameraFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CameraFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CameraFrame.setObjectName("CameraFrame")
        self.SoundFrame = QtWidgets.QFrame(self.centralwidget)
        self.SoundFrame.setGeometry(QtCore.QRect(570, -1, 731, 541))
        self.SoundFrame.setStyleSheet("background-color:#FFF;")
        self.SoundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SoundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SoundFrame.setObjectName("SoundFrame")
        self.frame_3 = QtWidgets.QFrame(self.SoundFrame)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 521, 521))
        self.frame_3.setStyleSheet("background-color:lightgrey;\n"
"border-radius:10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.listView = QtWidgets.QListView(self.frame_3)
        self.listView.setGeometry(QtCore.QRect(10, 10, 501, 441))
        self.listView.setStyleSheet("background-color:#fff")
        self.listView.setObjectName("listView")
        self.SettingButton = QtWidgets.QPushButton(self.frame_3)
        self.SettingButton.setGeometry(QtCore.QRect(410, 460, 93, 51))
        self.SettingButton.setStyleSheet("background-color:lime")
        self.SettingButton.setObjectName("SettingButton")
        self.SettingButton.clicked.connect(self.open_setting_page)
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 460, 391, 51))
        self.textEdit.setStyleSheet("background-color:#fff;\n"
"font-size:30px;")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1116, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SettingButton.setText(_translate("MainWindow", "Cài đặt"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                "p, li { white-space: pre-wrap; }\n"
                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:30px; font-weight:400; font-style:normal;\">\n"
                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:30px;\">Xàm</span></p></body></html>"))
        
    def open_setting_page(self):
        # Instantiate the setting page
        self.setting_page = QtWidgets.QMainWindow()
        ui = Setting_MainWindow()
        ui.setupUi(self.setting_page)
        self.setting_page.show()
    def update_text(self,text):
        self.textEdit.setText(text)
    def doFunction(self,text):
        request = text
        if request is not None:
            request = request.lower()
        if 'mấy giờ' in request or 'ngày mấy' in request  :
            ComputerFunction.get_time(request)
        elif 'âm lượng' in request:
            vol = request.split('lượng',1)
            ComputerFunction.controlVolumn(int(vol[1]))
        elif 'độ sáng' in request:
            val = request.split('sáng',1)
            ComputerFunction.controlBrightness(int(val[1]))
        elif 'mở ứng dụng' in request:
            app = request.split('dụng',1)
            App.open_application_multi(app[1])
        elif 'mở web' in request:
            request = request.replace(" ","")
            web = request.split('web',1)
            Internet.open_website(web[1])
        elif 'mở youtube' in request:
            song = request.split('youtube',1)
            Internet.play_Video(song[1])
        elif 'mở zingmp3 tìm kiếm' in request:
            song = request.split('kiếm',1)
            Internet.play_song_mp3(song[1])
        elif 'tìm kiếm trên google' in request:
            search = request.split('google',1)
            Internet.googleSearch(search[1])
        elif 'chụp màn hình' in request:
            ComputerFunction.screenShot()
        elif 'gửi email' in request:
            title = input('Nhập tiêu đề :')
            content = input('Nhập nội dung :')
            email_receive = input('Nhập email nhận :')
            Internet.send_email(title,content,email_receive)
        for item in requestCMD:
            if item in request:
                CMD.OpenSetting(item)

        else :
            print('Error')