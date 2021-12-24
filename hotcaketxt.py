#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 10:47:20 2021

@author: John Greendeer Lee
"""
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import numpy as np

basepage = "http://hotcakencyclopedia.com/"
req = Request(basepage)
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)
textlinks = set([])
for link in links:
    if link and ('ho.HT' in link):
        textlinks.add(link)
textlinks = list(textlinks)
textlinks[120] = 'ho.HT.IceHole.html'
pd.read_html(basepage+textlinks[3])

tables = []
PATH = 'C:\\Users\\John\\Documents\\HoChunk\\'
for k in range(len(textlinks)):
    link = textlinks[k]
    print(k)
    tables.append(pd.read_html(basepage+link))


def save_texts():
    for k in range(len(textlinks)):
        outtable = pd.concat(tables[k])
        outtable = outtable.replace(np.nan, '')
        np.savetxt(PATH+textlinks[k].split('.')[-2]+'.txt', outtable.values,
                   fmt='%s', encoding='utf-8')


replace_dict = {'à': 'a', 'á': 'a', 'â': 'a', 'ä': 'a', 'å': 'a', 'ā́': 'a',
                'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e', 'ì': 'i', 'í': 'i',
                'î': 'i', 'ï': 'i', 'ñ': '̨', 'ò': 'o', 'ó': 'o', 'ö': 'o',
                'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u', 'ā': 'a', 'ą́': 'ą',
                'ą': 'ą', 'ą́': 'ą', 'ą̄': 'ą', 'č': 'c', 'ē': 'e', 'ĕ': 'e',
                'ę': 'e', 'ğ': 'ǧ', 'ī': 'i', 'ĭ': 'i', 'í': 'i', 'į': 'į',
                'į́': 'į', 'į̄': 'į', 'ō': 'o', 'ŏ': 'o', 'š': 'š', 'ū': 'u',
                'ŭ': 'u', 'ų́': 'ų', 'ų̄': 'ų', 'ų̄́': 'ų', 'ų': 'ų', 'ų́': 'ų',
                'ų̄': 'ų', 'ž': 'ž', 'ǧ': 'ǧ', 'ǫ': 'ą', 'ʌ': 'ʌ', 'ʼ': '’',
                'ᵉ': 'e', 'ᵋ': '', 'ḗ': 'e', 'ṓ': 'o', 'ṕ': 'p', 'ạ': 'ą',
                'ế': 'e', 'ị': 'į', '̄': '', '́': '', '̨̨': '̨', 'ǫ': 'ą'}


def clean_characters(text):
    for oddchar, repchar in replace_dict.items():
        text = text.replace(oddchar, repchar)
        text = text.replace(oddchar.upper(), repchar.upper())
    return text


def output_clean(textfile, start=1, skip=3):
    with open(textfile, encoding='utf-8') as f:
        text = f.read()
    textlines = text.split('\n')
    textl = '\n'.join(textlines[start::skip])
    cleantext = clean_characters(textl)
    outfile = textfile.split('.')[0]
    outfile += '_clean.txt'
    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(cleantext)
    return cleantext
