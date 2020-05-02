#!/usr/bin/env python3
import os

def getSize(filename):
    st = os.stat(filename)
    return st.st_size

# pick a folder
#TODO: take pathname on command line
#folder = os.getcwd()
homedir = os.path.expanduser('~')
folder = os.path.join(homedir,'4TB/Movies/unseeded')
#folder = os.path.join(homedir,'4TB/Movies/H-WD500-MOVIES')

#sizes = [(path, os.stat(path).st_size) for path in paths]

def getOneLevelSizes(folder):
  folder_list = os.listdir(path=folder)
  paths = [os.path.join(folder, name) for name in folder_list]
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
sizesSorted = sorted(sizes, key=getKey)

for size,path in sizesSorted:
   print(size,'\t',path)

#folder_size = 0
#for (path, dirs, files) in os.walk(folder):
#  for file in files:
#    filename = os.path.join(path, file)
#    folder_size += os.path.getsize(filename)

#print "Folder = %0.1f MB" % (folder_size/(1024*1024.0))
