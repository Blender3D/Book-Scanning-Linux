#!/usr/bin/env python

import sys, os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class QInstallProgressItem(QTreeWidgetItem):
  def __init__(self, parent = None):
    super(QInstallProgressItem, self).__init__(parent)
    
    pixmap = QPixmap(24, 24)
    pixmap.fill()
    
    self.blankIcon = QIcon(pixmap)
    
    self.setState(False)
      
  def setState(self, state = 0):
    if state == 0:
      if self.childCount() > 0:
        self.setExpanded(False)
      
      self.setIcon(0, self.blankIcon)
    elif state == 1:
      if self.childCount() > 0:
        self.setExpanded(True)
      
      self.setIcon(0, QIcon.fromTheme('reload'))
    elif state == 2:
      self.setIcon(0, QIcon.fromTheme('dialog-apply'))
