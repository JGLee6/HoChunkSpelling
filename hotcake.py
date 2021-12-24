# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 17:44:29 2020

@author: John
"""
import numpy as np
import urllib.request as urlr
import io
import unidecode as undc
import pickle as pkl
import re
import datetime as dt

page = 'http://hotcakencyclopedia.com/ho.HocakLexicon.html'

bibStr = 'Bibliography'
startStr = 'Hočąk— English'

hcchar = ['a', 'e', 'i', 'o', 'u', 'ą', 'į', 'ų', 'b', 'c', 'g', 'ǧ', 'h',
          'j', 'k', 'm', 'n', 'p', 'r', 's', 'š', 't', 'w', 'x', 'y', 'z',
          'ž', "'"]
mxchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
          'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
oddchar = ['č', 'à', 'á', 'ā́', 'ą́', 'ē', 'è', 'é', 'ī', 'ì', 'í', 'í', 'į̄',
           'į́', 'ō', 'ō', 'ò', 'ó', 'ṓ', 'ǫ', 'ŭ', 'ū', 'ù', 'ú', 'ų̄', 'ų̄́',
           'ų́']
repchar = ['c', 'a', 'a', 'a', 'ą', 'e', 'e', 'e', 'i', 'i', 'i', 'i', 'į',
           'į', 'o', 'o', 'o', 'o', 'o', 'o', 'u', 'u', 'u', 'u', 'ų', 'ų',
           'ų']
hcset = set(['a', 'e', 'i', 'o', 'u', 'ą', 'į', 'ų', 'b', 'c', 'g', 'ǧ', 'h',
             'j', 'k', 'm', 'n', 'p', 'r', 's', 'š', 't', 'w', 'x', 'y', 'z',
             'ž', '’'])
oddset = set(['č', 'à', 'á', 'ā́', 'ą́', 'ē', 'è', 'é', 'ī', 'ì', 'í', 'í', 'į̄',
              'į́', 'ō', 'ō', 'ò', 'ó', 'ṓ', 'ǫ', 'ŭ', 'ū', 'ù', 'ú', 'ų̄', 'ų̄́',
              'ų́'])
oddset2 = ['à', 'á', 'â', 'ä', 'å', 'ā́', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï',
           'ñ', 'ò', 'ó', 'ö', 'ù', 'ú', 'û', 'ü', 'ā', 'ą́', 'ą', 'ą́', 'ą́', 'ą̄', 'č', 'ē', 'ĕ',
           'ę', 'ğ', 'ī', 'ĭ', 'í', 'į', 'į́', 'į̄', 'ō', 'ŏ', 'š', 'ū', 'ŭ', 'ų́', 'ų̄', 'ų̄́', 'ų', 'ų́', 'ų̄', 'ž', 'ǧ',
           'ǫ', 'ʌ', 'ʼ', 'ᵉ', 'ᵋ', 'ḗ', 'ṓ', 'ṕ', 'ạ', 'ế', 'ị',
           b'\xcc\x84'.decode('utf8'), b'\xcc\x81'.decode('utf8'), b'\xcc\xa8\xcc\xa8'.decode('utf8'), b'o\xcc\xa8'.decode('utf8')]
repset2 = ['a', 'a', 'a', 'a', 'a', 'a', 'e', 'e', 'e', 'e', 'i', 'i', 'i', 'i',
           b'\xcc\xa8'.decode('utf8'), 'o', 'o', 'o', 'u', 'u', 'u', 'u', 'a', 'ą', 'ą', 'ą', 'ą', 'ą', 'c', 'e', 'e',
           'e', 'ǧ', 'i', 'i', 'i', 'į', 'į', 'į', 'o', 'o', 'š', 'u', 'u', 'ų', 'ų', 'ų', 'ų', 'ų', 'ų', 'ž', 'ǧ',
           'ą', 'ʌ', '’', 'e', '', 'e', 'o', 'p', 'ą', 'e', 'į',
           '', '', b'\xcc\xa8'.decode('utf8'), 'ą']

splitchar = '—'

wordlist = set()
Ilist = {}
youList = {}
theyList = {}
futureList = {}
lexicon = {}
negList = {}
thatList = {}
gajaList = {}
giziList = {}
ejaList = {}
zheList = {}
nameList = {}


def get_hotcakes(page):
    """
    Opens the webpage (page) and copies everything from line ~585 to 83660.
    """
    datum = urlr.urlopen(page)
    read = datum.read().decode('utf-8')
    read = read.split('\n')
    startStr = 'English</strong>'
    endDat = len(read)-4
    record = False
    # Copy all of the word-list to a file for later
    with io.open('hotcake_lexicon.txt', 'w', encoding='utf8') as f:
        for k, line in enumerate(read):
            if startStr in line:
                startId = k+1
                print(startId)
                record = True
            elif record:
                continue
            else:
                startId = endDat
            if k > startId and k < endDat:
                print('start index', k)
                f.write(line)
                f.write('\n')
    return read


read = get_hotcakes(page)
content = read[585: len(read)-4]
for k, line in enumerate(content):
    # Format used has splitchar to separate word from definition
    spltln = line.split(splitchar)
    # Check that each line actually had a splitchar in it (contains a def)
    if len(spltln) > 1:
        worac, description = spltln[:2]
        # clean up some whitespace
        worac = worac.strip()
        description += ' (' + worac + ')'
        # Make lowercase
        worac = worac.lower()
        # We will also remove babebibo part for now
        worac = worac.split('(')[0]
        worac = worac.strip()
        # We need to clean up some strange characters used
        repl = False
        for l, ch in enumerate(oddset2):
            if ch in worac.lower():
                worac = worac.lower().replace(ch, repset2[l])
                repl = repl or True
            else:
                repl = repl or False
        #if repl:
        #    print(worac, worac in wordlist)
        # Check if there are still funny letters and add them to our list
        for wch in worac:
            if wch.lower() not in hcset and wch.isalpha():
                oddset.add(wch.lower())
        # Clean some simple grammar/spelling errors
        if 'na' in worac and 'ną' not in worac:
            worac = worac.replace('na', 'ną')
        if 'ni' in worac and 'nį' not in worac:
            worac = worac.replace('ni', 'nį')
        if 'nu' in worac and 'nų' not in worac:
            worac = worac.replace('nu', 'nų')
        if 'ank' in worac:
            worac = worac.replace('ank', 'ąk')
        if 'ąnk' in worac:
            worac = worac.replace('ąnk', 'ąk')
        if 'anc' in worac:
            worac = worac.replace('anc', 'ąc')
        if 'ąnc' in worac:
            worac = worac.replace('ąnc', 'ąc')
        if 'ink' in worac:
            worac = worac.replace('ink', 'įk')
        if 'įnk' in worac:
            worac = worac.replace('įnk', 'įk')
        if 'inc' in worac:
            worac = worac.replace('inc', 'įc')
        if 'įnc' in worac:
            worac = worac.replace('įnc', 'įc')
        if 'unc' in worac:
            worac = worac.replace('unc', 'ųc')
        if 'eske' in worac:
            worac = worac.replace('eske', 'esge')
        if 'aske' in worac:
            worac = worac.replace('aske', 'asge')
        if 'šku' in worac:
            worac = worac.replace('šku', 'šgu')
        if 'sku' in worac:
            worac = worac.replace('sku', 'sgu')
        if 'xcį' in worac:
            worac = worac.replace('xcį', 'xjį')
        if 'jgr' in worac:
            worac = worac.replace('jgr', 'cr')
        if 'jgn' in worac:
            worac = worac.replace('jgn', 'cn')
        if 'jg' in worac:
            worac = worac.replace('jg', 'cg')
        if 'gg' in worac:
            worac = worac.replace('gg', 'k')
        if worac.startswith('c’'):
            worac = worac.replace('c’', 'c')
        if 'ma' in worac and 'mą' not in worac:
            worac = worac.replace('ma', 'mą')
        if 'mi' in worac and 'mį' not in worac:
            worac = worac.replace('mi', 'mį')
        if 'mu' in worac and 'mų' not in worac:
            worac = worac.replace('mu', 'mų')
        if worac.startswith('ca') and ' how' in description:
            worac = worac.replace('ca', 'ja')
        if worac.startswith('ca') and ' what' in description:
            worac = worac.replace('ca', 'ja')
            worac = worac.replace('k', 'g')
        if worac.startswith('ca') and ' why' in description:
            worac = worac.replace('ca', 'ja')
            worac = worac.replace('k', 'g')
        if worac.endswith('’'):
            worac = worac[:-1]
        # Remove linebreak html <br> from description
        description = description.replace('<br>', '')
        # If the word is already in our wordlist we'll add the definition to
        # the previous. Otherwise, create a new dictionary entry
        # add the word to the wordlist set if not there already
        if ' I ' in description and 'ya' in worac:
            Ilist[worac] = description
        elif ' I ' in description and 'ha' in worac:
            Ilist[worac] = description
        elif ' I ' in description:
            Ilist[worac] = description
        elif 'we ' in description and 'ha' in worac and 'wi' in worac:
            Ilist[worac] = description
        elif 'we ' in description and 'ya' in worac and 'wi' in worac:
            Ilist[worac] = description
        elif 'you' in description and 'ra' in worac:
            youList[worac] = description
        elif 'you' in description and 'nį' in worac:
            youList[worac] = description
        elif description.startswith(' you '):
            youList[worac] = description
        elif 'they' in description and ('ire' in worac or 'įre' in worac):
            theyList[worac] = description
        elif 'they' in description and ('ine' in worac or 'įne' in worac):
            theyList[worac] = description
        elif description.startswith(' they') and 'ira' in worac:
            theyList[worac] = description
        elif 'kjane' in worac or 'kjana' in worac or 'kcane' in worac or 'kjąne' in worac or 'kjen' in worac or 'kjon' in worac:
            futureList[worac] = description
        elif 'not ' in description and 'nį' in worac:
            negList[worac] = description
        elif worac in wordlist:
            #print(worac)
            lexicon[worac] += '; ' + description
            wordlist.add(worac)
        elif worac.endswith('ra') and worac[:-2] in wordlist:
            lexicon[worac[:-2]] += '; ' + 'stripped('+worac+', JGL) '+ description
            wordlist.add(worac[:-2])
        elif worac.endswith('era') and worac[:-3] in wordlist:
            lexicon[worac[:-3]] += '; ' + 'stripped('+worac+', JGL) '+ description
            wordlist.add(worac[:-3])
        elif worac.endswith('ną') and worac[:-3] in wordlist and description.startswith(' the '):
            print(worac)
            lexicon[worac[:-3]] += '; ' + 'stripped('+worac+', JGL) '+ description
            wordlist.add(worac[:-3])
        elif worac.endswith('iža') and worac[:-4] in wordlist:
            lexicon[worac[:-4]] += '; ' + 'stripped('+worac+', JGL) '+ description
            wordlist.add(worac[:-4])
        elif worac.endswith('ižą') and worac[:-5] in wordlist:
            lexicon[worac[:-5]] += '; ' + 'stripped('+worac+', JGL) '+ description
            wordlist.add(worac[:-5])
        elif worac.endswith('jega') or worac.endswith('nąga') or worac.endswith('nąka'):
            thatList[worac] = description
        elif worac.endswith('gaja') or worac.endswith('gają'):
            gajaList[worac] = description
        elif worac.endswith('giži') or worac.endswith('regi'):
            giziList[worac] = description
        elif worac.endswith('eja') or worac.endswith('aija') or worac.endswith('ąija') or worac.endswith('oija') or worac.endswith('uija'):
            ejaList[worac] = description
        elif worac.endswith('gi') and 'when' in description:
            giziList[worac] = description
        elif worac.endswith('že') or worac.endswith('še'):
            zheList[worac] = description
        elif 'personal name' in description:
            nameList[worac] = description
        else:
            lexicon[worac] = description
            wordlist.add(worac)
    else:
        print(k, line)

# Pickle the output
#f = open("hotcakelexicon.pkl", "wb")
#pkl.dump(lexicon, f)
#f.close()
#lexicon = pkl.load(open('hotcakelexicon.pkl', 'rb'))
#
#fileName = 'C:/Users/John/Documents/HoChunk/Hoocak.xml'
#soundDir = u'C:\\Users\\John\\Documents\\HoChunk\\Lexique Pro Data\\'
#soundDir += u'Hooca\u0328k\\sounds\\'
#wavs = glob.glob(soundDir+'*.wav')
#soundNames = []
#for wav in wavs:
#    soundNames.append(wav.split('\\')[-1])
#hocak = ET.parse(fileName)
#root = hocak.getroot()
#for atype in root.findall('entry'):
#    key = atype[0][0][0].text
#    if key == '?':
#        break
#    try:
#        for btype in atype[1].findall('definition'):
#            value = btype[0][0].text
#            output[key] = value
#    except IndexError:
#        output[key] = '__'
#    except UnicodeEncodeError:
#        print(key)
#        
#output
#for k, line in enumerate(set(lexicon) - set(output)):
#    print(line, lexicon[line].split('<br>')[0])
#with open('hotcake.tsv', 'w', encoding='utf-8', newline='\n') as csvfile:
#    spamwriter = csv.writer(csvfile, delimiter='\t')
#    for i, (k, v) in enumerate(lexicon.items()):
#        if k not in outset:
#            print(k, v)
#            spamwriter.writerow([k, v])
