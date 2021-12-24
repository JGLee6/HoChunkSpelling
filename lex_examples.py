#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 10:59:46 2021

@author: John Greendeer Lee
"""
import xml.etree.ElementTree as ET

# This part is to open the lexicon xml data
fileName = '/Users/johnglee/Documents/HoChunk/Hoocak.xml'

hocak = ET.parse(fileName)
root = hocak.getroot()

failed = []

examples = {}
for atype in root.findall('entry'):
    key = atype[0][0][0].text
    if key == '?':
        break
    for btype in atype[1].findall('example'):
        exHC = btype[0][0].text
        if exHC:
            try:
                exEN = btype[2][0][0].text
                examples[exHC] = exEN
            except IndexError:
                try:
                    exEN = btype[1][0][0].text
                    examples[exHC] = exEN
                except IndexError:
                    examples[exHC] = ' '
                    print(exHC)
            except UnicodeEncodeError:
                print(key)
        else:
            exHC = btype[0][0][0].text
            try:
                examples[exHC] = btype[0][2][0][0].text
            except IndexError:
                try:
                    examples[exHC] = btype[0][1][0][0].text
                except IndexError:
                    examples[exHC] = ' '
                    print(exHC)
            except UnicodeEncodeError:
                print(key)

outputtxt = ''
for key, val in examples.items():
    outputtxt += key + '\n'

with open('lexExamples.txt', 'w', encoding='utf-8') as f:
    f.write(outputtxt)
