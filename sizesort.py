#!/usr/bin/env python3
import os

def getSize(filename):
    st = os.stat(filename)
    return st.st_size

# pick a folder
#TODO: take pathname on command line
#folder = os.getcwd()
homedir = os.path.expanduser('~')
#folder = os.path.join(homedir,'4TB/Movies/unseeded')
folder = os.path.join(homedir,'4TB/Movies/H-WD500-MOVIES')

def getOneLevelSizes(folder):
  folder_list = os.listdir(path=folder)
  paths = [os.path.join(folder, name) for name in folder_list]
  #sizes = [(path, os.stat(path).st_size) for path in paths]
  sizes = []
  for path in paths:
    if os.path.isfile(path):
      if (('.mkv' in path) or ('.mp4' in path)) and not ('sample' in path.lower()):
        sizes.append((getSize(path), path))
    else: #recurse
      sizes += getOneLevelSizes(path)
  return sizes
sizes = getOneLevelSizes(folder)

def getKey(i):
   return i[0]
sizesSorted = sorted(sizes, key=getKey, reverse=True)

for size,path in sizesSorted:
#   print(size,'\t',path)
   print(str(size) + ',' + path)
