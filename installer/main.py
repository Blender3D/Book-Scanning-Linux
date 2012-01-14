#!/usr/bin/env python

import sys, os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import functions

from gui import *
from QInstallProgressItem import *

class StartQT4(functions.StartQT4, QMainWindow):
  def __init__(self, parent = None):
    QWidget.__init__(self, parent)
    
    self.firstStage = True
    self.partition = None
    self.swap = None
    
    self.headers = [
      'Induction Linux Setup',
      'Induction Linux Setup',
      'Select an install destination',
      'Select a swap partition',
      'Disk Summary',
      'Web Browsers'
    ]

    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    
    progress_labels = []
    
    for i in range(self.ui.progressList.topLevelItemCount()):
      item = self.ui.progressList.topLevelItem(i)
      
      newItem = QInstallProgressItem()
      newItem.setText(0, item.text(0))
      
      if item.childCount() > 0:
        for j in range(item.childCount()):
           child = item.child(j)
           
           newChild = QInstallProgressItem()
           newChild.setText(0, child.text(0))
           
           newItem.addChild(newChild)
      
      progress_labels.append(newItem)
      
    self.ui.progressList.clear()
    self.ui.progressList.addTopLevelItems(progress_labels)
    
    
    '''
    for label in list(set(self.progress)):
      item = QInstallProgressItem()
      item.setText(0, label)
      
      self.ui.progressList.addTopLevelItem(item)
    '''
    self.ui.progressList.topLevelItem(0).setState(1)
    
    self.ui.forwardButton.setIcon(QIcon.fromTheme('next'))
    self.ui.backButton.setIcon(QIcon.fromTheme('back'))
    self.ui.cancelButton.setIcon(QIcon.fromTheme('gtk-cancel'))
    
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
