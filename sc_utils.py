#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 08:39:58 2021

@author: John Greendeer Lee
"""
replace_dict = {'à': 'a', 'á': 'a', 'â': 'a', 'ä': 'a', 'å': 'a', 'ā́': 'a',
                'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e', 'ì': 'i', 'í': 'i',
                'î': 'i', 'ï': 'i', 'ñ': '̨r', 'ò': 'o', 'ó': 'o', 'ö': 'o',
                'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u', 'ā': 'a', 'ą́': 'ą',
                'ą': 'ą', 'ą́': 'ą', 'ą̄': 'ą', 'č': 'c', 'ē': 'e', 'ĕ': 'e',
                'ę': 'e', 'ğ': 'ǧ', 'ī': 'i', 'ĭ': 'i', 'í': 'i', 'į': 'į',
                'į́': 'į', 'į̄': 'į', 'ō': 'o', 'ŏ': 'o', 'š': 'š', 'ū': 'u',
                'ŭ': 'u', 'ų́': 'ų', 'ų̄': 'ų', 'ų̄́': 'ų', 'ų': 'ų', 'ų́': 'ų',
                'ų̄': 'ų', 'ž': 'ž', 'ǧ': 'ǧ', 'ǫ': 'ą', 'ʌ': 'ʌ', 'ʼ': '’',
                'ᵉ': 'e', 'ᵋ': '', 'ḗ': 'e', 'ṓ': 'o', 'ṕ': 'p', 'ạ': 'ą',
                'ế': 'e', 'ị': 'į', '̄': '', '́': '', '̨̨': '̨', 'ǫ': 'ą'}


def clean_characters(text):
    """
    Clean up common odd characters.

    Parameters
    ----------
    text : string
        String containing text to clean.

    Returns
    -------
    text : string
        Cleaned text with odd characters replaced by IPA.

    """
    for oddchar, repchar in replace_dict.items():
        text = text.replace(oddchar, repchar)
        text = text.replace(oddchar.upper(), repchar.upper())
    return text


nasaldict = {'na': 'ną', 'ni': 'nį', 'nu': 'nų', 'ma': 'mą',
             'mi': 'mį', 'mu': 'mų'}
checkdict = {'inj': 'įj', 'unj': 'ųj', 'jhi': 'cii', 'sh': 'š', 'zh': 'ž',
             'phi': 'pi', 'še-': 'že’', 'ing': 'įg',
             'ank': 'ąk', 'unk': 'ųk', 'ink': 'įk', 'ung': 'ųk',
             'ang': 'ąk', 'arn': 'ąn', 'ąnk': 'ąk', 'ųnk': 'ųk',
             'įnk': 'įk', 'ąrn': 'an', 'ąng': 'ąk', 'ųng': 'ųk',
             'ing': 'įg', 'įng': 'įg', 'orn': 'on',
             'amp': 'ąp', 'onk': 'ąk', 'amb': 'ąp', 'de-': 'te’', 'd': 't',
             'šaną': 'šąną', 'anje': 'ąje', 'anjawi': 'ąjawi',
             'anj': 'ąc', 'kanąg': 'kąnąk', 'kaną': 'kąną',
             'šinį': 'šįnį', 'pinį': 'pįnį', 'kjane': 'kjene',
             'kjanįhawi': 'kjanąhawi', "unš": "ųš", 'jagu': 'jaagu',
             'jeg': 'ceek', 'hinųg': 'hinųk', 'jowe': 'coowe',
             'jonį': 'coonį', 'jasge': 'jaasge', 'horuxuj': 'horoǧoc',
             'wąkšig': 'wąąkšik', 'šesge': 'žeesge', 'uine': 'ųire',
             'aine': 'ąire', 'xji': 'xjį'}
worderrs = {'šige': 'žige', 'waša': 'wažą', 'wašara': 'wažąra',
            'wašanįša': 'wažąraižą', 'hiša': 'hižą',
            'hąnąj': 'hanąąc', 'egi': 'eegi',
            'eja': 'eeja', 'Mąura': 'Mąą’ųra', 'u': 'ųų',
            'nąb': 'nąąp', 'wąk': 'wąąk', 'hinįgra': 'hinįkra',
            'e': 'ee', 'hąp': 'hąąp', 'mą': 'mąą', 'įke': 'hįke',
            'esge': 'eesge', 'roha': 'roohą', 'hakišu': 'hakižu',
            'wakišu': 'waakižu', 'janąga': 'jaanąga', "eyi": "eegi",
            "ne": "nee", "wąkregi": "wąąkregi",
            "peše": "peežega", "weną": "weeną", "hųk": "hųųk",
            "hoera": "ho’era", "hageja": "haakeja", "raš": "raaš",
            "hajįja": "hacįįja"
            }


def clean_spell(text):
    """
    Clean several partial and whole-word spelling errors in gospel text.

    Parameters
    ----------
    text : string
        Whole text string of four-gospel text.

    Returns
    -------
    text : string
        Whole text string of four-gospel text with spelling errors corrected.
    """
    texto = text
    lines = text.split('\n')
    for k, line in enumerate(lines):
        words = line.split(' ')
        for m, word in enumerate(words):
            if word.lower().startswith("egi") and word.lower() != "egi":
                word = word[:3]+" "+word[3:]
            for err, corr in nasaldict.items():
                if err in word and corr not in word:
                    word = word.replace(err, corr)
                erru = err[0].upper() + err[1:]
                corru = corr[0].upper() + corr[1:]
                if erru in word and corru not in word:
                    word = word.replace(erru, corru)
            for err, corr in checkdict.items():
                if err in word and corr not in word:
                    word = word.replace(err, corr)
                erru = err[0].upper() + err[1:]
                corru = corr[0].upper() + corr[1:]
                if erru in word and corru not in word:
                    word = word.replace(erru, corru)
            for werr, wcorr in worderrs.items():
                if word == werr:
                    word = word.replace(werr, wcorr)
                werru = werr[0].upper() + werr[1:]
                wcorru = wcorr[0].upper() + wcorr[1:]
                if word == werru:
                    word = word.replace(werru, wcorru)
            words[m] = word
        lines[k] = ' '.join(words)
    text = '\n'.join(lines)
    if texto != text:
        print('Found errors')
    return text


def remove_nhat(text):
    """
    Remove use of 'ň' in lexicon examples.

    I prefer the use of r and inferring nasality spread, which makes the
    grammar more easily interpretable.

    Parameters
    ----------
    text : string
        Input text using 'ň'.

    Returns
    -------
    text : string
        output text without 'ň'.
    """
    text = text.replace('ňą', 'ra')
    text = text.replace('ňų', 'ru')
    text = text.replace('įįň', 'įir')
    text = text.replace('ąįň', 'ąir')
    text = text.replace('ųįň', 'ųir')
    text = text.replace('ň', 'r')
    return text


def replace_kjane(text):
    """
    Remove use of 'kjane' future marker in lexicon examples.

    Parameters
    ----------
    text : string
        Input text using 'kjane'.

    Returns
    -------
    text : string
        Output text with 'kjane' replaced by 'kjene'.
    """
    text = text.replace('kjane', 'kjene')
    text = text.replace('kjanaw', 'kjanąw')
    return text
