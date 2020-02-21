import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Font Display
FONT_SIZE = 15
FONT_FAM = "Ariel"     

#window size
win_h = 500
win_w = 500

#input textbox size
tb_w = 40
tb_h = 40

#input textbox position
tb_x = 10
tb_y = 30
tb_sp = 5 #spacing between each box

#output textbox size        
otb_w = 250
otb_h = 250

#output textbox positions
otb_x = win_h-otb_w-tb_sp
otb_y = 0

#text box properties 
#text size and font
font = QFont()
font.setFamily(FONT_FAM)
font.setPointSize(FONT_SIZE)

class HelloWindow(QMainWindow):    
    def __init__(self):        
        QMainWindow.__init__(self)
        self.setStyleSheet("QLabel {font: "+str(FONT_SIZE)+"pt "+FONT_FAM+"}")

        self.setMinimumSize(QSize(win_h, win_w))    
        self.setWindowTitle("Dive Site Finder 0.0.3") 
        
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
        #input values
        self.values = ['Winter', 'Spring', 'Summer', 'Fall']
        #set text box inputs
        self.box = []
    
        #each box is spaced from the first box at y+it's height (to prevent overlap)+space        
        for i in range(4):
            self.box.append(QLineEdit(self.values[i], self))
            self.box[i].move(tb_x, (tb_y+tb_h*i+tb_sp*i))
            self.box[i].setFont(font)
        
        
        
        #text box for Diving information    
        self.info_box = QLabel(self)
        self.info_box.setText('<b>Dive Location</b>\
                              <br>You Are Here\
                              <br>\
                              <br><b>Contact Information</b>\
                              <br>555.555.5555')
        
        self.info_box.move(otb_x, otb_y)
        self.info_box.resize(otb_w, otb_h)
        self.info_box.setAlignment(Qt.AlignCenter)
        self.info_box.setStyleSheet("QLabel {background-color: red;}")

    def button(self):
        self.button = QPushButton('show text', self)
        self.button.move(tb_x, (tb_y+tb_h*4+tb_sp*4))
        self.button.setFont(font)
        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        wint_val = self.box[0].text()
        
        #QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + wint_val)
        self.info_box.setText('<b>Dive Location</b>\
                              <br>'+str(self.values[0])+'\
                              <br>\
                              <br><b>Contact Information</b>\
                              <br>'+str(self.values[0]))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    def run_app():
        app = QApplication([])
        app.setStyle('Fusion')
        mainWin = HelloWindow()
        mainWin.show()
        app.exec_()
    run_app()