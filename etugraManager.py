#!/usr/bin/python

import os
import getopt
import sys
from subprocess import call

try:
    opts, args = getopt.getopt(sys.argv[1:],"d")
except getopt.GetoptError:
    print("etugra.py -d <directory>             Directory where all the files are timestamped")
    sys.exit(2)

for opt, arg in opts:
    if opt == '-d':  
        dirlist = os.listdir(sys.argv[2])
        for infile in dirlist:
            print(infile)
            os.system('python etugra.py -g /log/' + infile)
        