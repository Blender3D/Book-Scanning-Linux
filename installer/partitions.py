#!/usr/bin/env python

import os, sys, subprocess, re
from math import floor

def cond_match(regexp, line, grp):
  match = re.search(regexp, line)
  
  if match:
    return match.group(grp)
  else:
    return ''

class Partition:
  def __init__(self, identifier = '', label = '', uuid = '', type = '', size = 0):
    self.identifier = identifier
    self.label = label
    self.uuid = uuid
    self.type = type
    self.size = size
  
  def __repr__(self):
    if self.label not in ['', None]:
      return str(self.label)
    else:
      return str(self.identifier)


def readable_size(bytes, sizes = ['B', 'KB', 'MB', 'GB', 'TB']):
  i = 0
  
  while bytes >= 1024:
    bytes /= 1024.0
    i += 1
  
  return str(round(bytes, 1)) + sizes[i]


def list_partitions():
  #if subprocess.Popen('whoami', stdout = subprocess.PIPE).communicate()[0].strip() != 'root':
  #  print('You must run this script as root.')
  #  sys.exit(1)

  blkid = subprocess.Popen('blkid', stdout = subprocess.PIPE).communicate()[0].split('\n')
  partitions = []

  for line in blkid[:-1]:
    line = line.strip()
    partition = Partition()
    
    partition.identifier = cond_match(r'^(/dev/[a-zA-Z0-9]+)', line, 0)
    partition.label = cond_match(r'LABEL="((?:[^"\\]|\\.)*)"', line, 1)
    partition.uuid = cond_match(r'UUID="((?:[^"\\]|\\.)*)"', line, 1)
    partition.type = cond_match(r'TYPE="((?:[^"\\]|\\.)*)"', line, 1)
    
    try:
      handle = open('/sys/block/{0}/{1}/size'.format(partition.identifier.replace('/dev/', '').rstrip('0123456789'), partition.identifier.replace('/dev/', '')), 'r')
      partition.size = int(handle.read()) * 512
      handle.close()
      
      partitions.append(partition)
    except:
      pass

  return partitions
