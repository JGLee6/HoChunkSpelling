#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 13:15:28 2021

@author: John Greendeer Lee
"""

syl_dict = {'a': ['a', 'aa', 'ą', 'ąą'],
            'l': ['b', 'p'],
            'ttA': ['c'],
            'e': ['e'],
            'K': ['g', 'k'],
            'x': ['ǧ', 'x'],
            'A': ['h'],
            'i': ['i', 'ii', 'į', 'įį'],
            'tt': ['j'],
            'KA': ['k'],
            'm': ['m'],
            'n': ['n'],
            'o': ['o', 'oo', 'u', 'uu', 'ų', 'ųų'],
            'lA': ['p'],
            'L': ['r'],
            'rA': ['s'],
            'dA': ['š'],
            't': ['t'],
            'w': ['w'],
            'xA': ['x'],
            'y': ['y'],
            'r': ['z', 's'],
            'd': ['ž', 'š']}

dlet = ['t', 'K', 'l', 'r', 'd', 'x']
vlist = ['a', 'e', 'i', 'o', 'u']
punclist = [':', '!', '?', ',', '.']
order = ['ttA', 'tt', 'KA', 'lA', 'rA', 'dA', 'xA', 'a', 'l', 'e', 'K', 'x',
         'A', 'i', 'm', 'n', 'o', 't', 'w', 'y', 'r', 'L', 'd']


def lookup_syl(char):
    prob = 1
    try:
        out = syl_dict[char]
        prob *= 1/len(out)
        return out[0], prob
    except KeyError:
        print('Key Error with character: ', char)
        return char, prob

def convert_syllabary(text):
    textline = text.strip()
    prob = 1
    for ch in order:
        out = syl_dict[ch]
        print(ch, out[0])
        textline = textline.replace(ch, out[0])
        prob *= 1/len(out)
    print(prob)
    k = 0
    while k < len(textline):
        ch = textline[k]
        if k == 0:
            k += 1
            continue
        chm1 = textline[k-1]
        if (ch == ' ') and (chm1 not in vlist and chm1 not in punclist):
            textline = textline[:k] + 'a' + textline[k:]
            k += 2
        elif (ch not in vlist) and (ch != '̌') and (chm1 not in vlist) and (chm1 != ' ') and chm1 not in punclist:
            textline = textline[:k] + 'a' + textline[k:]
            k += 2
        else:
            k += 1
    if textline[-1] not in vlist and textline[-1] not in punclist:
        textline += 'a'
    return textline
