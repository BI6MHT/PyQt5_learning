# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:47:23 2023

@author: BI6MHT
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.button_is_checked = True
        
        self.setWindowTitle("My App")
        
        button = QPushButton('Press Me!')
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)
    
        self.setCentralWidget(button)
        
    def the_button_was_toggled(self,checked):
        self.button_is_checked = checked

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
