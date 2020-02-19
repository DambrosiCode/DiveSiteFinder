import sys
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, pyqtSlot    

FONT_SIZE = 15
FONT_FAM = "Ariel"     


#window size
win_h = 500
win_w = 500

#textbox size
tb_w = 40
tb_h = 40
        
#text box position
tb_x = 10
tb_y = 30
tb_sp = 5 #spacing between each box

#text box properties 
#text size and font
font = QFont()
font.setFamily(FONT_FAM)
font.setPointSize(FONT_SIZE)

class HelloWindow(QMainWindow):    
    def __init__(self):        
        QMainWindow.__init__(self)
        self.setStyleSheet("QLabel {font: "+str(FONT_FAM)+"pt "+FONT_STYLE+"}")

        self.setMinimumSize(QSize(win_h, win_w))    
        self.setWindowTitle("Dive Site Finder 0.0.2") 
        
        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   
 
        gridLayout = QGridLayout(self)     
        centralWidget.setLayout(gridLayout)  
         
        self.menu()
        self.titles()
        self.text_boxes()
        self.button()
        
    def menu(self):
        menu = self.menuBar().addMenu('Action for quit')
        leave = menu.addAction('Quit')
        leave.triggered.connect(QtWidgets.QApplication.quit)
    
    def titles(self):
        pass
    
    def text_boxes(self):
        #set text box inputs
        self.summ_temp = QLineEdit('1', self)
        self.spri_temp = QLineEdit('2', self)
        self.fall_temp = QLineEdit('3', self)
        self.wint_temp = QLineEdit('4', self)
        
        #each box is spaced from the first box at y+it's height (to prevent overlap)+space
        self.summ_temp.move(tb_x, (tb_y+tb_h*0+tb_sp*0))        
        self.summ_temp.resize(tb_w, tb_h)
        self.summ_temp.setFont(font)
        
        self.spri_temp.move(tb_x, (tb_y+tb_h*1+tb_sp*1))
        self.spri_temp.resize(tb_w, tb_h)
        self.spri_temp.setFont(font)
        
        self.fall_temp.move(tb_x, (tb_y+tb_h*2+tb_sp*2))
        self.fall_temp.resize(tb_w, tb_h)
        self.fall_temp.setFont(font)
        
        self.wint_temp.move(tb_x, (tb_y+tb_h*3+tb_sp*3))
        self.wint_temp.resize(tb_w, tb_h)
        self.wint_temp.setFont(font)
        
    def button(self):
        self.button = QPushButton('show text', self)
        self.button.move(tb_x, (tb_y+tb_h*4+tb_sp*4))
        self.button.setFont(font)
        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        textbox_value = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textbox_value)
        self.textbox.setText("")
        
        
        
        
if __name__ == "__main__":
    def run_app():
        app = QApplication([])
        app.setStyle('Fusion')
        mainWin = HelloWindow()
        mainWin.show()
        app.exec_()
    run_app()