# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:03:20 2023

@author: BI6MHT
"""

from PyQt5.QtWidgets import QApplication, QWidget

import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()