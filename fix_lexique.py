# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 09:41:20 2021.

@author: John
"""

FILEPATH = 'C:\\Users\\John\\Documents\\HoChunk\\Lexique Pro Data\\Hoocąk\\'
filename = 'Merged4LP.txt'
with open(FILEPATH+filename, 'rb') as f:
    lines = f.readlines()

# https://en.wikipedia.org/wiki/Caron
unicode_hacek = ['\u02c7', '\u01e6', '\u01e7', '\u0160', '\u0161', '\u017d', '\u017e']
corr_hacek = '\u030c'
# https://en.wikipedia.org/wiki/Ogonek
unicode_ogonek = ['\u02db', '\u0104', '\u0105', '\u012e', '\u012f', '\u0172', '\u0173']
corr_ogonek = '\u0328'

# Find egregious unicode characters
for k, line in enumerate(lines):
    for char in unicode_hacek:
        if char in line.decode('utf8'):
            print(k, line)
    for char in unicode_ogonek:
        if char in line.decode('utf8'):
            print(k, line)

# finds unicode chars
num = 0
for line in lines:
    try:
        # correct hacek, \u030c
        rline = line.replace(b'\xcc\x8c', b'')
        # correct ogonek, \u0328
        rline = rline.replace(b'\xcc\xa8', b'')
        # correct apostrophe, \u2019
        rline = rline.replace(b'\xe2\x80\x99', b'')
        # this character, '§', is in a bunch of lines
        rline = rline.replace(b'\xc2\xa7', b'')
        # accent mark in a number of entries, '\u0301'
        rline = rline.replace(b'\xcc\x81', b'')
        # other accent mark,
        rline = rline.replace(b'\xc3\xa0', b'')
        # weird question mark
        rline = rline.replace(b'\xef\xbf\xbd', b'')
        rline.decode('utf8').encode('ascii')
    except UnicodeEncodeError as e:
        print(e)
        print(line)
        num += 1
