#!/usr/bin/env python

import sys, os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class QInstallProgress(QTreeWidget):
  def __init__(self, parent = None):
    super(QInstallProgress, self).__init__(parent)
