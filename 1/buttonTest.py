# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:20:27 2023

@author: BI6MHT
"""

import sys
from PyQt5.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

window = QPushButton("Push me")
window.show()

app.exec()