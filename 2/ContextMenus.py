# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:47:23 2023

@author: BI6MHT
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QApplication, QLabel, QMainWindow, QMenu


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()


    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            # handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            # handle the middle-button press in here.
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            # handle the right-button press in here.
            self.label.setText("mousePressEvent RIGHT")

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1",self))
        context.addAction(QAction("test 2",self))
        context.addAction(QAction("test 3",self))
        context.exec(e.globalPos())
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
