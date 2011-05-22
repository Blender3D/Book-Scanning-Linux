#!/usr/bin/env python

import sys, os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import functions

from gui import *

class StartQT4(functions.StartQT4, QMainWindow):
  def __init__(self, parent = None):
    QWidget.__init__(self, parent)
    
    self.firstStage = True
    self.partition = None
    self.swap = None
    
    self.headers = {0: 'Induction Linux Setup',
                    1: 'Induction Linux Setup',
                    2: 'Select an install destination',
                    3: 'Select a swap partition',
                    4: 'Disk Summary',
                    5: 'Web browsers'}
    
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    
    self.connect(self.ui.forwardButton, SIGNAL('clicked()'), self.forward)
    self.connect(self.ui.backButton, SIGNAL('clicked()'), self.back)
    self.connect(self.ui.cancelButton, SIGNAL('clicked()'), self.cancel)
    
    self.connect(self.ui.partitionList, SIGNAL('itemSelectionChanged()'), self.partition_selected)
    self.connect(self.ui.swapList, SIGNAL('itemSelectionChanged()'), self.swap_selected)
#    self.connect(self.ui.actionChooseRight, SIGNAL('triggered()'), self.chooseRight)
  
if __name__ == '__main__':
  app = QApplication(sys.argv)
  myapp = StartQT4()
  myapp.show()
  sys.exit(app.exec_())
