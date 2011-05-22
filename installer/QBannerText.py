#!/usr/bin/env python

import sys, os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class QBannerText(QWidget):
  def __init__(self, parent = None):
    super(QBannerText, self).__init__(parent)
  
  def getText(self):
    return str(self.property('text').toString())
  
  def setText(self, string):
    return self.setProperty('text', string)
