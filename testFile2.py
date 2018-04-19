import os,sys
from sys import *
from os import *

root='.\TestSet'
badName='(copy)'

for path, subdirs, files in os.walk(root):
    for name in files:
        fullPath=os.path.join(path, name)
        if badName in fullPath:
            newPath=fullPath[:-11]+".jpg"
            rename(fullPath,newPath)
            fullPath=newPath
        print(fullPath)
        system("python classyfy2.py "+fullPath)
