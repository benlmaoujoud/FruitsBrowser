import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui
#class Window
class Window(QMainWindow) :
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowIcon(QtGui.QIcon('Fruits.png'))

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        #en grand taille in 1st time
        self.showMaximized()

        #naving
        navbar = QToolBar()
        self.addToolBar(navbar)
        # back button
        back_button = QAction('GoBack',self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)
        #forward button
        forward_button = QAction('Forward',self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        #refresh button
        refresh_button = QAction('refresh', self)
        refresh_button.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_button)
        #activate navBar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigation)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)
    #function to active navbar search
    def navigation(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    #function to update url
    def update_url(self,arg):
        self.url_bar.setText(arg.toString())


# main app
appBrow = QApplication(sys.argv)
QApplication.setApplicationName('Fruits')
window = Window()
appBrow.exec()



