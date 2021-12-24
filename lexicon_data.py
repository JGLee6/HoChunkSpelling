#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 13:01:11 2021

@author: John Greendeer Lee
"""

"""
Get Lexicon permutations
"""
filename = 'Merged4LP.txt'
with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()
num_lines = len(lines)
lexlist = []
verbadd3 = ['ire', 'iranį', 're', 'wire', 'nįre', 'winįre', 'kjene',
            'irekjene', 'nįkjene', 'iranįkjene', 'gįnį', 'šųnų', 'irešųnų',
            'aje', 'wiaje', 'nįaje', 'winįaje', 'že']
verbaddm = ['wi', 'nį', 'winį', 'nįkjene', 'nįkjanąwi', 'nįkje',
            'nįkjawi', 'wigįnį', 'že', 'wiže', 'nįže', 'ra', 'nįra',
            'wira']
verbaddnom = ['gįnį', 'šųnų']
verbaddv = ['kjene', 'kjanąwi', 'kje', 'kjawi']
for k in range(num_lines):
    line = lines[k]
    if not line.startswith('\lx'):
        continue
    root = line.split('\lx')[1].strip()
    if root != '' and root[0].isalpha():
        lexlist.append(root)
        k += 1
        ps = lines[k]
        while not ps.startswith('\ps'):
            k += 1
            ps = lines[k]
        ps = ps.split('\ps')[1].strip()
        if ps == 'n.':
            lexlist.append(root + 'ra')
            lexlist.append(root + 'ižą')
            lexlist.append(root + 'nąąkre')
        elif ps == 'v.act.' or ps == 'v.inact.':
            k += 1
            cf = lines[k]
            while not cf.startswith('\cf'):
                k += 1
                cf = lines[k]
            cf = cf.split('\cf')[1].split(', ')
            print(cf)
            metcheck, met = False, False
            if root[-1] in ('a', 'e', 'i', 'o', 'u', '̨'):
                vowel = ''
                if root[-1] == 'e':
                    metcheck = True
            else:
                vowel = 'i'
            if metcheck:
                k += 1
                mp = lines[k]
                while not mp.startswith('\mp'):
                    k += 1
                    mp = lines[k]
                if '+' in mp:
                    met = True
            lexlist.append(root + vowel + 'kje')
            lexlist.append(root + vowel + 'kjene')
            lexlist.append(root + 'ire')
            lexlist.append(root + 'irekjene')
            lexlist.append(root + 'iranį')
            lexlist.append(root + 'iranįkjene')
            lexlist.append(root + 're')
            lexlist.append(root + 'wire')
            lexlist.append(root + 'winįre')
            if len(cf) < 2:
                continue
            first = cf[0].strip()
            second = cf[1].strip()
            lexlist.append(first)
            lexlist.append(second)
            for addon in verbaddm:
                if met:
                    metlet = 'a'
                else:
                    metlet = first[-1]
                lexlist.append(first[:-1] + metlet + addon)
                lexlist.append(second[:-1] + metlet + addon)
            for addon in verbaddv:
                lexlist.append(first + vowel + addon)
                lexlist.append(second + vowel + addon)
