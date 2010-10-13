#!python2.6
#-*- encoding: utf-8 -*-

# these are English printable characters...
from string import printable

import glob,codecs,os
import re,sys

sys.stdout = open('needs-translation.txt','w')
os.chdir('0000')

printable = set(printable)

okay = set()

# I manually verified that these contain no Japanese characters.
for name in ('0001.txt','0002.txt','0006.txt','0007.txt','0012.txt',
             '0018.txt','0020.txt','0022.txt','0026.txt'):
    with codecs.open(name,encoding='utf-8') as input:
        okay.update(set(input.read()) - printable)

for name in glob.glob('*.txt'):
    with codecs.open(name,encoding='utf-8') as input:
        if set(input.read()).difference(okay):
            print name
