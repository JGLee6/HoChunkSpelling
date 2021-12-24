# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 08:54:08 2018

@author: John
"""
import xml.etree.ElementTree as ET
import unicodecsv as csv
import glob

fileName = 'C:/Users/John/Documents/HoChunk/Hoocak.xml'
soundDir = u'C:\\Users\\John\\Documents\\HoChunk\\Lexique Pro Data\\'
soundDir += u'Hooca\u0328k\\sounds\\'
wavs = glob.glob(soundDir+'*.wav')
soundNames = []
for wav in wavs:
    soundNames.append(wav.split('\\')[-1])
hocak = ET.parse(fileName)
root = hocak.getroot()

output = {}

failed = []
# All word entries without question marks etc. (try to link a file)
with open('test2.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.writer(f)
    for atype in root.findall('entry'):
        key = atype[0][0][0].text
        if key == '?':
            break
        try:
            for btype in atype[1].findall('definition'):
                value = btype[0][0].text
                output[key] = value
                media = '[sound:'
                fileName = key.encode('ascii', 'ignore')
                fileName2 = key.replace(u'\u030c', 'h')
                fileName2 = fileName2.replace(u'\u2019', '\'')
                fileName3 = fileName2.replace(u'\u0328', 'n')
                if fileName+'.wav' in soundNames:
                    fileName += '.wav'
                elif fileName2+'.wav' in soundNames:
                    fileName = fileName2 + '.wav'
                elif fileName3+'.wav' in soundNames:
                    fileName = fileName3 + '.wav'
                else:
                    failed.append(key)
                media += fileName + ']'
                w.writerow([key+' '+media, value])
        except IndexError:
            output[key] = '__'
        except UnicodeEncodeError:
            print(key)

# Examples with audio files
with open('test3.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.writer(f)
    for atype in root.findall('entry'):
        key = atype[0][0][0].text
        if key == '?':
            break
        try:
            for btype in atype[1].findall('example'):
                exHC = btype[0][0].text
                wav = btype[1].get('href')
                exEN = btype[2][0][0].text
                media = '[sound:'
                media += wav
                media += ']'
                w.writerow([exHC+' '+media, exEN])
        except IndexError:
            print(key)
        except UnicodeEncodeError:
            print(key)

# All Examples
with open('test4.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.writer(f)
    for atype in root.findall('entry'):
        key = atype[0][0][0].text
        if key == '?':
            break
        try:
            for btype in atype[1].findall('example'):
                exHC = btype[0][0].text
                wav = btype[1].get('href')
                exEN = btype[2][0][0].text
                media = '[sound:'
                media += wav
                media += ']'
                w.writerow([exHC+' '+media, exEN])
        except IndexError:
            try:
                for btype in atype[1].findall('example'):
                    exHC = btype[0][0].text
                    #wav = btype[1].get('href')
                    exEN = btype[1][0][0].text
                    #media = '[sound:'
                    #media += wav
                    #media += ']'
                    w.writerow([exHC, exEN])
            except IndexError:
                print(key)
        except UnicodeEncodeError:
            print(key)


# import codecs
# import xmltodict
# import json
# with codecs.open(fileName, encoding='utf-8') as fd:
#     doc = xmltodict.parse(fd.read())
# json.dumps(doc)
