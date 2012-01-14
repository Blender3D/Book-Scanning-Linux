#!/usr/bin/env python

import sys, os

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from partitions import *

class StartQT4(QMainWindow):
  def cancel(self):
    dialog = QMessageBox.warning(self, 'Induction Linux Installer', 'Are you sure you want to exit the installation?', QMessageBox.No, QMessageBox.Yes)
    
    if dialog == QMessageBox.Yes:
      self.close()
  
  def forward(self):
    self.ui.progressList.topLevelItem(self.ui.contentWidget.currentIndex()).setState(2)
    self.ui.progressList.topLevelItem(self.ui.contentWidget.currentIndex() + 1).setState(1)
    
    if self.firstStage:
      self.ui.forwardButton.setText('&Forward')
      self.ui.backButton.setEnabled(True)
      self.ui.contentWidget.setCurrentIndex(1)
      
      self.firstStage = False
    else:
      self.ui.label.setText(self.headers[self.ui.contentWidget.currentIndex() + 1])
      self.ui.progressList.setCurrentItem(self.ui.progressList.topLevelItem(self.ui.contentWidget.currentIndex() + 1))
      
      if self.ui.contentWidget.currentIndex() + 1 == 2:
        self.select_partition()
        self.ui.contentWidget.setCurrentIndex(self.ui.contentWidget.currentIndex() + 1)
      elif self.ui.contentWidget.currentIndex() + 1 == 3:
        self.select_swap()
        self.ui.contentWidget.setCurrentIndex(self.ui.contentWidget.currentIndex() + 1)
        
        if self.swap == False:
          self.ui.swapList.setEnabled(False)
          QMessageBox.information(self, 'Induction Linux Installer', 'You do not have any Swap partitions.\nThey are not required, but they speed up your system when you are low on RAM.\nIt is recommended that you make at least a 1GB Swap partition.', QMessageBox.Ok)
      elif self.ui.contentWidget.currentIndex() + 1 == 4:
        self.ui.diskSpaceWarning.setText(str(self.ui.diskSpaceWarning.text()).replace('{{disk_space}}', readable_size(self.partition.size)))
        self.ui.diskSpaceWarning.setText(str(self.ui.diskSpaceWarning.text()).replace('{{useable_space}}', readable_size(self.partition.size - 2.5 * 10**9)))
        self.ui.contentWidget.setCurrentIndex(self.ui.contentWidget.currentIndex() + 1)
      else:
        self.ui.contentWidget.setCurrentIndex(self.ui.contentWidget.currentIndex() + 1)
  
  def back(self):
    self.ui.progressList.topLevelItem(self.ui.contentWidget.currentIndex()).setState(0)
    self.ui.progressList.topLevelItem(self.ui.contentWidget.currentIndex() - 1).setState(1)
    
    if self.ui.contentWidget.currentIndex() == 1:
      self.ui.contentWidget.setCurrentIndex(0)
      self.ui.backButton.setEnabled(False)
      self.ui.forwardButton.setText('&Start')
      
      self.firstStage = True
    else:
      if self.ui.contentWidget.currentIndex() == 2:
        self.ui.forwardButton.setEnabled(True)
      elif self.ui.contentWidget.currentIndex() == 4:
        self.ui.diskSpaceWarning.setText('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;">\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Induction Linux needs at least <span style=" font-weight:600;">2.5GB</span> of disk space to function properly.</p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">The partition that you have selected currently has a size of <span style=" font-weight:600;">{{disk_space}}</span>, which leaves you with a total of <span style=" font-weight:600;">{{useable_space}}</span> for personal files and additional software.</p>\n<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"></p>\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Are you sure that you want to continue with the installation? If you\'d like to change the install partition, press the &quot;<span style=" font-weight:600;">Back</span>&quot; button until you reach the installation destination step.</p></body></html>')
      
      self.ui.label.setText(self.headers[self.ui.contentWidget.currentIndex() - 1])
      self.ui.contentWidget.setCurrentIndex(self.ui.contentWidget.currentIndex() - 1)
  
  def select_partition(self):
    self.ui.forwardButton.setEnabled(False)
    self.ui.partitionList.clear()
    
    for partition in list_partitions():
      item = QTreeWidgetItem([partition.label, readable_size(partition.size), partition.type, partition.identifier, partition.uuid])
      
      if partition.type not in ['ext2', 'ext3', 'ext4']:
        item.setDisabled(True)
      
      self.ui.partitionList.addTopLevelItem(item)
  
  def partition_selected(self):
    row = self.ui.partitionList.selectedItems()[0]
    self.ui.forwardButton.setEnabled(True)
    
    for part in list_partitions():
      if part.uuid == row.text(4):
        self.partition = part
        break
  
  def select_swap(self):
    exists = False
    self.ui.swapList.clear()
    
    for partition in list_partitions():
      item = QTreeWidgetItem([partition.label, readable_size(partition.size), partition.type, partition.identifier, partition.uuid])
      
      if partition.type == 'swap':
        exists = True
        self.ui.swapList.addTopLevelItem(item)
    
    if not exists:
      self.swap = False
    
    
  def swap_selected(self):
    row = self.ui.swapList.selectedItems()[0]
    
    for part in list_partitions():
      if part.uuid == row.text(4):
        self.swap = part
        break
    
