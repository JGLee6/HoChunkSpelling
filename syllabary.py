#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 13:15:28 2021

@author: John Greendeer Lee
"""
import re

syl_dict = {'a': ['a', 'aa'],
            'l': ['b', 'p'],
            'ttA': ['c'],
            'e': ['e'],
            'K': ['g', 'k'],
            'H': ['ǧ', 'x'],
            'A': ['h'],
            'i': ['i', 'ii'],
            'tt': ['j'],
            'KA': ['k'],
            'm': ['m'],
            'n': ['n'],
            'o': ['o', 'oo'],
            'oo': ['u', 'uu'],
            'lA': ['p'],
            'L': ['r'],
            'rA': ['s'],
            'dA': ['š'],
            't': ['t'],
            'w': ['w'],
            'HA': ['x'],
            'j': ['y'],
            'r': ['z', 's'],
            'd': ['ž', 'š'],
            'in': ['į', 'įį'],
            'oon': ['ų', 'ųų'],
            'ai': ['ai'],
            'an': ['ą', 'ąą']}

dlet = ['t', 'K', 'l', 'r', 'd', 'x']
vlist = ['a', 'e', 'i', 'o', 'u']
punclist = [':', '!', '?', ',', '.']
order = ['ttA', 'j', 'tt', 'KA', 'lA', 'rA', 'dA', 'HA',
         'oon', 'ai', 'an', 'in', 'oo', 'a', 'l', 'e', 'K', 'H',
         'A', 'i', 'm', 'n', 'o', 't', 'w', 'r', 'L', 'd']

ipa_dict = {'ǧ': 'H', 'š': 'dA', 'ž': 'd', 'b': 'l', 'c': 'ttA',
            'j': 'tt', 'k': 'K', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'lA',
            'r': 'L', 's': 'rA', 't': 't', 'u': 'oo', 'w': 'w', 'x': 'HA',
            'y': 'j', 'z': 'r', 'e': 'e', 'g': 'K', 'i': 'i', 'h': 'A',
            '̨': 'n'}


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


def babebibo_to_ipa2(text):
    word = ''
    textout = ['']
    rep_char = syl_dict.get(word, [''])[0]
    for char in text+' ':
        new_rep = syl_dict.get(word+char, [''])[0]
        if new_rep == '':
            if len(textout)>1 and textout[-2]=='a' and textout[-1]=='n' and rep_char not in vlist and rep_char!=' ':
                textout[-2] = 'ą'
                textout.pop()
            elif textout[-1] not in vlist and rep_char not in vlist and textout[-1]!='' and textout[-1]!=' ' and rep_char!=' ':
                textout.append('a')
            textout.append(rep_char)
            word = char
            rep_char = syl_dict.get(char, [char])[0]
        else:
            word += char
            rep_char = new_rep
    output = ''.join(textout)
    # add an "a" after any single letters
    output = re.sub(r'(\s\w)\s', r'\1a ', output)
    # unvoice ending letters
    wordlist = split_words(output)
    for m, word in enumerate(wordlist):
        wordlist[m] = unvoice_foot(word)
    output = ''.join(wordlist)
    # if text ends in "n" it should probably end in "ną" instead.
    return output


un_voice_dict = {'ǧ': 'x', 'g': 'k', 'j': 'c', 'b': 'p', 'z': 's', 'ž': 'š'}


def unvoice_foot(word):
    if word == '':
        return word
    last_char = word[-1]
    if last_char == '̌':
        last_char = word[-2:]
    lchar = len(last_char)
    rep_char = un_voice_dict.get(last_char, last_char)
    word = word[:-lchar] + rep_char
    return word


def split_words(text):
    return re.split(r'([^a-zA-Z0-9_’̨̌])', text)


def case_of(text):
    """Return the case-function appropriate for text: upper, lower, title, or str."""
    return (str.upper if text.isupper() else
            str.lower if text.islower() else
            str.capitalize if text.istitle() else
            str)


def ipa_to_babebibo(word):
    """
    Convert IPA to Babebibo syllabary.

    This uses a look-up table of letter correspondances and replaces them
    directly. This doesn’t guarantee agreement with accepted spellings in the
    Kingswan lexicon.

    Parameters
    ----------
    word : string
        IPA Hoocąk text.

    Returns
    -------
    word : string
        Babebibo Ao ttA K text.
    """
    # replace nasal with empty
    #word = word.replace('̨', '')
    # replace double vowels
    word = re.sub(r'([aeiou])\1*', r'\1', word)
    # replace double nasal vowels
    word = re.sub(r'([aeiou]̨)\1*', r'\1', word)
    # lower word
    word = word.lower()
    # "ai" is treated as "y" in babebibo
    for key, val in ipa_dict.items():
        word = word.replace(key, val)
    # {'a': ' ', 'ai': 'ai'} handled separately
    for k in range(len(word)-1):
        if (word[k] == 'a') and (word[k+1] != 'i'):
            word = word[:k] + ' ' + word[k+1:]
    word = word.replace('nn', 'n')
    return word
