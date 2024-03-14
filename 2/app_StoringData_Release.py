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
        
        self.button = QPushButton('Press Me!')
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)
    
        self.setCentralWidget(self.button)
        
    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
