# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:29:17 2023

@author: BI6MHT
"""

import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        
        # The super() function is used to give access to methods and properties of a parent or sibling class.
        # The super() function returns an object that represents the parent class.
        
        # Here, you’ve used super() to call the __init__() of the QMainWindow class, 
        # allowing you to use it in the MainWindow class without repeating code.
        super().__init__()
        
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        
        self.setCentralWidget(button)
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()