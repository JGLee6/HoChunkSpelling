# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 07:17:36 2021

@author: John
"""
import re
from collections import Counter
import sc_utils as scu

"""
Spell-checker stuff
https://norvig.com/spell-correct.html
"""


def clean_punctuation(text):
    """Ignore punctuation of text."""
    return re.sub('[,.@:;?!"]', ' ', text)


def deletes1(word):
    """Generate all single letter deletes of word."""
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    return set(deletes)


def deletes2(word):
    """Return all strings that are two deletes away from this word."""
    return {e2 for e1 in deletes1(word) for e2 in deletes1(e1)}


WORDS = Counter(clean_punctuation(open('podcasts.txt',
                                       encoding='utf-8').read()).lower().split())
WORD2 = Counter(clean_punctuation(open('weather_reports.txt',
                                       encoding='utf-8').read()).lower().split())
with open('lexExamples.txt', encoding='utf-8') as f:
    textlex = f.read()
WORD4 = Counter(clean_punctuation(scu.clean_characters(textlex)).lower().split())
WORDS.update(WORD2)
WORDS.update(WORD4)

# dictionary of all 1-delete words
deldict = {}
for key in WORDS.keys():
    deletes = deletes1(key)
    for delword in deletes:
        deldict[delword] = deldict.get(delword, []) + [key]

# dictionary of all 2-delete words
deldict2 = {}
for key in WORDS.keys():
    deletes = deletes2(key)
    for delword in deletes:
        deldict2[delword] = deldict2.get(delword, []) + [key]


def P(word, N=sum(WORDS.values())):
    """Probability of `word`."""
    return WORDS[word] / N


def correct(word):
    "Find the best spelling correction for this word."
    # Prefer edit distance 0, then 1, then 2; otherwise default to word itself.
    candidates = (known(edits0(word)) or
                  known(edits1(word)) or
                  known(edits2(word)) or
                  [word])
    return max(candidates, key=WORDS.get)


def candidates(word):
    """Generate possible spelling corrections for word."""
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def edits1(word):
    """All edits that are one edit away from `word`."""
    letters = 'aąbcegǧhiįjkmnoprsštuųwxyzž’'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def known(words):
    """Return the subset of words that are actually in the dictionary."""
    return {w for w in words if w in WORDS}


def edits0(word):
    """Return all strings that are 0 edits away from word (the word itself)."""
    return {word}


def edits2(word):
    """Return all strings that are 2 edits away from this word."""
    return {e2 for e1 in edits1(word) for e2 in edits1(e1)}


def correct_text(text):
    """Correct all the words within a text, returning the corrected text."""
    letters = 'aąbcegǧhiįjkmnoprsštuųwxyzž’'
    return re.sub('['+letters+letters.upper()+']+', correct_match, text)


def correct_match(match):
    """Spell-correct word in match, and preserve proper upper/lower/title case."""
    word = match.group()
    return case_of(word)(correct(word.lower()))


def case_of(text):
    """Return the case-function appropriate for text: upper, lower, title, or str."""
    return (str.upper if text.isupper() else
            str.lower if text.islower() else
            str.title if text.istitle() else
            str)


def delknown(words):
    """Return all strings that correspond to any string in wordswith one deletion."""
    return set([dw for word in words for dw in deldict.get(word, [])])


def delknown2(words):
    """Return all strings that correspond to any string in wordswith two deletions."""
    return set([dw for word in words for dw in deldict2.get(word, [])])


def correct2(word):
    """Find the best spelling correction for this word using 1-del symspell."""
    # Prefer edit distance 0, then 1; otherwise default to word itself.
    candidates = (known(edits0(word)) or
                  known(deletes1(word)) | delknown([word]) |
                  delknown(deletes1(word))
                  or [word])
    return max(candidates, key=WORDS.get)


def correct3(word):
    """Find the best spelling correction for this word."""
    # Prefer edit distance 0, then 1, then 2; otherwise default to word itself.
    candidates = (known(edits0(word)) or
                  known(deletes1(word)) | delknown([word]) |
                  delknown(deletes1(word)) or
                  known(deletes2(word)) | delknown2([word]) |
                  delknown2(deletes1(word)) | delknown2(deletes2(word)) |
                  delknown(deletes2(word)) or
                  [word])
    return max(candidates, key=WORDS.get)
