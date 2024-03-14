# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:47:23 2023

@author: BI6MHT
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
    
    
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
        # print(e)
        
    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")
    
    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")
        
    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickeEvent")
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
