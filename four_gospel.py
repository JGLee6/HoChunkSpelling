# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 13:54:31 2021

@author: John Greendeer Lee
"""
import pdfminer.high_level
from collections import Counter


#PATH = 'C:\\Users\\John\\Documents\\HoChunk\\'
PATH = '/Users/johnglee/Documents/HoChunk/'
title = 'Four_Gospels_Acts_Genesis_and_Exodus_Cha.pdf'


def reload_text():
    """
    Re-scrapes text from Four-Gospel Ho-Chunk pdf.

    (Reverses page order)

    Returns
    -------
    text : string
        String of entire pdf from Four-Gospels in Ho-Chunk.
    """
    text1 = ''
    # pdf is scanned in reverse so have to change ordering
    for k in range(517, 0, -1):
        print(k)
        text1 += pdfminer.high_level.extract_text(PATH + title,
                                                  page_numbers=[k])
    with open(PATH + 'four_gospeld.txt', mode="w", encoding='utf-8') as f:
        f.write(text1)

    return text1


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
                'ế': 'e', 'ị': 'į', '̄': '', '́': '', '̨̨': '̨', 'ǫ': 'ą',
                'ş': 's'}

def clean_characters(text):
    for oddchar, repchar in replace_dict.items():
        text = text.replace(oddchar, repchar)
        text = text.replace(oddchar.upper(), repchar.upper())
    return text


def separate_punctuation(text):
    punc_char = ['.', ',', '?', '!', ':', ';', '(', ')']
    for char in punc_char:
        text = text.replace(char, ' '+char+' ')
    return text


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
nasaldict = {'na': 'ną', 'ni': 'nį', 'nu': 'nų', 'ma': 'mą', 'mi': 'mį',
             'mu': 'mų', 'giu': 'gi’ų', 'hiu': 'hi’ų',
             'nąši': 'nąąžį', 'saja': 'saacą', 'janti': 'cąąt’į',
             'šegu': 'žeegų', 'xji': 'xjį'}
checkdict = {'inj': 'įj', 'unj': 'ųj', 'jhi': 'cii', 'sh': 'š', 'zh': 'ž',
             'phi': 'pi', 'še-': 'že’', 'ing': 'įg',
             'ank': 'ąk', 'unk': 'ųk', 'ink': 'įk', 'ung': 'ųk',
             'ang': 'ąk', 'arn': 'an', 'ąnk': 'ąk', 'ųnk': 'ųk',
             'įnk': 'įk', 'ąrn': 'ąn', 'ąng': 'ąk', 'ųng': 'ųk',
             'ing': 'įg', 'įng': 'įg', 'orn': 'on', 'anc': 'ąc',
             'amp': 'ąp', 'onk': 'ąk', 'amb': 'ąp', 'de-': 'te’', 'd': 't',
             'šaną': 'šąną', 'anje': 'ąje', 'anjawi': 'ąjawi',
             'anj': 'ąc', 'kanąg': 'kąnąk', 'kaną': 'kąną',
             'šinį': 'šįnį', 'pinį': 'pįnį', 'kjane': 'kjene',
             'kjanįhawi': 'kjanąhawi', "unš": "ųš", "uine": "ųire",
             "iųi": "i’ųi", "iun": "i’ųn", "iųk": "i’ųk", "umb": "ųp",
             "gr": "kr", "uxuj": "oǧoc", "g-": "k-", "j-": "c-", "b-": "p-",
             "gš": "kš", "jš": "cš", "bš": "pš", "jw": "cw", "bw": "pw",
             "gw": "kw", "sb": "š", "bg": "pg", "jg": "cg", "wauk": "wąąk",
             "waų": "wa’ų", "imp": "įp", "imb": "įp", "-hire": "ire",
             "gn": "kn", "bn": "pn", "jn": "cn", "hišaki": "hižąki",
             "gigus": "gigųs", "khan": "kąn", "gk": "kk", "jk": "ck",
             "bk": "pk", "bij": "hij", "gj": "kj", "jr": "cr", "bj": "pj",
             "nąxir": "nąąǧir", "hiąc": "hi’ąc", "ghir": "kir", "'": "’",
             'v': 'n', 'jagu': 'jaagu', 'hinųg': 'hinųk', 'jowe': 'coowe',
             'jonį': 'coonį', 'jasge': 'jaasge', 'wąkšig': 'wąąkšik',
             'šesge': 'žeesge', 'aine': 'ąire', 'kb': 'kh',
             'khinųb': 'kiinųp', 'hiunį': 'hi’ųnį', '-hiran': 'iran',
             'nąb': 'nąp', '-khine': 'kįire', 'khine': 'kįire',
             'ant': 'ąt', 'hi’ųki': 'hiyųge', 'unų': 'ųnų',
             'kišu': 'kižu', 'šeši': 'žeeži',
             'paną': 'pąną', 'biąc': 'hi’ąc',
             'bini': 'hini', '-nįk': 'nįk', "šejan": "žejąn",
             'sinš': 'sįc', 'bs': 'ps', 'gs': 'ks', 'js': 'cs',
             '-hašąną': 'hašąną', 'pb': 'ph', 'ye': 'ge', 'yo': 'go',
             'yi': 'gi', 'gh': 'kh', 'bh': 'ph', 'jh': 'ch', 'jb': 'jh',
             'gi-u': 'gi’u', 'bir': 'hir', 'iie': 'ie', 'iio': 'io',
             'khuha': 'kųųhą', 'tanį-': 'tanį', 'khenį': 'keenį',
             '-wi': 'wi', 'šaua': 'šąną', 'ik-i': 'ik’i', 'nųb': 'nųp',
             'sete': 'xete', 'ną-i': 'ną’i', 'chųi': 'cųi', 'papa': 'pąną',
             'inp': 'įp', 'biša': 'hižą', 'aiša': 'aižą', 'eiša': 'eižą',
             'iui': 'ini', 'i-šur': 'išur', 'šurog': 'šorog',
             'gi-š': 'giš', 'res-ja': 'resikja', 'res-nį': 'resnį',
             'chasga': 'caasga', 'awa-a': 'awa’a', 'šura': 'žura',
             'ogišu': 'ogižu', '-ba': '-ha', 'šesga': 'žesga',
             'nąxi': 'nąǧi', 'ay': 'ag', 'šiy': 'šik', 'sok': 'zok',
             '̨y': '̨g', 'ey': 'eg', 'yk': 'nk', 'eua': 'ena',
             'nąxgun': 'nąxgųn', 'hauąj': 'ha’ųaj', 'wauąj': 'wa’ųaj',
             'siwi': 'sįwį', '-ranįk': 'ranįk', 'geja': 'keja'}
worderrs = {'šige': 'žige', 'waša': 'wažą', 'wašara': 'wažąra',
            'wašanįša': 'wažąraižą', 'hiša': 'hižą', 'iša': 'hižą',
            'šesge': 'žeesge', 'hanąj': 'hanąąc', 'egi': 'eegi',
            'eja': 'eeja', 'esge': 'eesge', 'mąura': 'mą’ųra', 'u': 'ųų',
            'nąb': 'nąąp', 'wąk': 'wąąk', 'wąkšig': 'wąąkšik',
            'wąkšigra': 'wąąkšikra', 'hinįgra': 'hinįkra', 'e': 'ee',
            'hąp': 'hąąp', 'mą': 'mąą', 'įke': 'hįke', 'jeg': 'ceek',
            'jonį': 'coonį', 'jagu': 'jaagu', 'jasge': 'jaasge',
            'esge': 'eesge', 'roha': 'roohą', 'hakišu': 'hakižu',
            'wakišu': 'waakižu', 'janąga': 'jaanąga', "eyi": "eegi",
            "ne": "nee", "wąkregi": "wąąkregi", "horuxujre": "horoǧocre",
            "peše": "peežega", "weną": "weeną", "hųk": "hųųk",
            "hoera": "ho’era", "hageja": "haakeja", "raš": "raaš",
            "hajįja": "hacįįja", '-eja': 'eeja', "ne": "nee",
            "t’e": "t’ee", 'jegeja': 'ceekeja', 'jhanąx': 'caanąx',
            'hąnąj': 'hanąąc', 'wakižu': 'waakižu', 'jhasga': 'caasga',
            'jega': 'jeega', 'jane': 'jaane', 'pi': 'pįį', 'mąra': 'mąąra',
            'nąc': 'nąąc', 'higu': 'higų', 'reną': 'reeną',
            'hireną': 'hiireną', 'wanįnera': 'waanįirera', 'mąu': 'mą’ų',
            'hųkra': 'hųųkra', 'hogusra': 'hogųsra', 'rokąną': 'rookąną',
            'hinųkjega': 'hinųkjeega', 'mąx': 'mąąx', 'hąpra' : 'hąąpra',
            'jajiga': 'jaajiga', 'mąšja': 'mąąšją', 'ho': 'hoo',
            'hijanera': 'hijąnera', 'hanįnera': 'hanįirera',
            'rašra': 'raašra', 'epa': 'eepa', 'wore': 'woore', 'su': 'suu',
            'hiwusųš': 'hiwusųc', 'jaaguiša': 'jaaguižą', 'mąnegi': 'mąąregi',
            'jaagu-u': 'jaagu’ų', 'wa-i': 'wa’i', 'šun': 'š’ųų', 'š’un': 'š’ųų'
            }
space_dict = {"-hianj": " hianj", "hianj-": "hianj ", "-hinig": " hinig",
              "hinig-": "hinig ", "-anaga": " anaga", "anaga-": "anaga ",
              "wianaga": "wi anaga", "nianaga": "ni anaga",
              "iranaga": "ire anaga", "uanaga": "u anaga",
              "ianaga": "i anaga", "-jega": " jega", "-nagre": " nagre",
              "-nanka": " nanka", "-jane": " jane", "-agre": " agre",
              "-gigi": " gigi", "-wagigi": " wagigi", "-nigi": " nigi",
              "-hingi": " hingi", "-ningi": " ningi", "-isha": " isha",
              "-hisha": " hisha", "hinug-": "hinug ", "ne-": "ne ",
              'kerepana-': 'kerepana ', "d'eh": "d'e h", "wang-": "wang ",
              "-wang": " wang", 'hamb-': 'hamb ', '-hamb': ' hamb',
              '-wah': ' wah', '-hahi': ' hahi', '-haji': ' haji',
              '-nai': ' nai', '-harni': ' harni', 'woehi-': 'wo’e hii ',
              'sto-': 'stoo ', 'nab-': 'nab ', 'naj-': 'naj ', 'jhi-': 'jhi ',
              'nige-': 'nige ', 'harni-': 'harni ', 'howa-hu': 'howahu ',
              'ruj-': 'ruj ', 'hija-': 'hija ', '-hiru': ' hiru',
              '-jhi': ' jhi', '-hojhi': ' hojhi', '-kiri': ' kiri',
              'howe-': 'howe ', 'phi-': 'phi ', '-xete': ' xete',
              'shishig-': 'shishig ', '-shishig': ' shishig',
              '-wara': ' wara', '-nihe': ' nihe', 'xete-': 'xete ',
              'hogihi-': 'hogihi ', '-wirac': ' wirac', '-wiru': ' wiru',
              '-raje': ' raje', '-haj': ' haj', '-hara': ' hara',
              'niamb-': 'ni’amb ', 'waj-': 'waj ', '-wagi': ' wagi',
              '-ingig': ' hingig', 'najge-': 'najge ', '-karagi': ' karagi',
              '-hu': ' hu', 'jeg-': 'jeg ', 'roha-': 'roha ', '-rehi': ' rehi',
              '-nunige': ' nunige', 'res-hik': 'res hik', 'kara-u': 'kara u',
              'shu-u': 'shu u', '-egi': ' egi', 'egi-': 'egi ', 'max-': 'max ',
              'mas-': 'mas ', '-hashi': ' hashi', '-washi': ' washi',
              '-warni': ' warni', 'shura-': 'shura ', 'howare-': 'howare ',
              '-nup': ' nup', 'inanaga': 'ine anaga', 'naxi-': 'naxi ',
              'janti-': 'janti ', 'nagu-': 'nagu '
              }

shelist = ["hiše", "šguuše", "ranįše", "wašoše", "šuuše", "xguxguiše",
           "waše", "šaraše", "hiwaše", "waišoše", "wanįšoše", "giše", "haiše",
           "raiše", "nąąše", "nąraše"]


def case_of(text):
    """Return the case-function appropriate for text: upper, lower, title, or str."""
    return (str.upper if text.isupper() else
            str.lower if text.islower() else
            str.capitalize if text.istitle() else
            str)


def clean_egi(text):
    """Egi often attached to front of word, so we split."""
    texto = text
    lines = text.split('\n')
    for k, line in enumerate(lines):
        words = line.split()
        for m, word in enumerate(words):
            case = case_of(word)
            word = word.lower()
            if word.startswith("egi") and word != "egi":
                word = word[:3]+" "+word[3:]
            elif word.startswith("eyi") and word != "eyi":
                word = word[:3]+" "+word[3:]
            elif word.startswith("eshi") and word != "eshi":
                word = word[:4]+" "+word[4:]
            elif word.startswith("esge") and word != "esge":
                word = word[:4]+" "+word[4:]
            elif word.startswith("kheni") and word != "kheni":
                word = word[:5]+" "+word[5:]
            elif word.startswith("ni-") and word != "ni-":
                word = word[:2]+" "+word[3:]
            elif word.startswith("ma-") and word != "ma-":
                word = word[:2]+" "+word[3:]
            elif word.startswith("peshe") and word != "peshe":
                word = word[:5]+" "+word[5:]
            elif word.startswith("e-") and word != "e-":
                word = "ee "+word[2:]
            elif word.endswith("nunige") and word != "nunige":
                word = word[:-6] + ' nunige'
            #elif word.startswith("šesge") and word != "šesge":
            #    word = word[:4]+" "+word[4:]
            if word.endswith("-eja") and word != "-eja":
                word = word[:-4]+" "+"-eja"
            elif word.startswith("inke") and word != "inke":
                word = word[:4] + " " + word[4:]
            for comp_word, s_word in space_dict.items():
                if comp_word in word:
                    word = word.replace(comp_word, s_word)
            words[m] = case(word)
        lines[k] = ' '.join(words)
    text = '\n'.join(lines)
    if texto != text:
        print('Found egi')
    return text


def clean_spell(text):
    """
    Load the four-gospel text and cleans several whole-word spelling errors.

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
        words = line.split()
        for m, word in enumerate(words):
            case = case_of(word)
            word = word.lower()
            for err, corr in nasaldict.items():
                if err in word and corr not in word:
                    word = word.replace(err, corr)
            for werr, wcorr in worderrs.items():
                if word == werr:
                    word = word.replace(werr, wcorr)
            for err, corr in checkdict.items():
                if err in word:
                    word = word.replace(err, corr)
            if word.endswith('g'):
                word = word[:-1]+'k'
            elif word.endswith('j'):
                word = word[:-1]+'c'
            elif word.endswith('b'):
                word = word[:-1]+'p'
            if ("-kj") in word and not word.startswith("-"):
                sword = word.split("-kj")
                if sword[0][-1] in ("a", "e", "i", "o", "u", "̨", "n"):
                    word = sword[0]+"kj"+sword[-1]
                else:
                    word = sword[0]+"ikj"+sword[-1]
            if (word.endswith("kaja")) or (word.endswith("gaja")):
                word = word[:-4]+"gają"
            if (word.startswith("-")) or (word.startswith("’")):
                word = word[1:]
            if word.endswith("-šąną"):
                word = word[:-8] + word[-7:]
            elif word.endswith("saną"):
                word = word[:-5] + 'šąną'
            elif word.endswith("giši"):
                word = word[:-5] + "giži"
            elif word.endswith("-"):
                word = word[:-1]
            elif word.endswith("-un"):
                word = word[:-3] + "’ų"
            elif word.endswith("aun"):
                word = word[:-2] + "’ų"
            elif word.endswith("še") and word not in shelist:
                word = word[:-3] + "že"
            if ('ss' in word) and ('sš' not in word):
                word = word.replace('ss', 's')
            words[m] = case(word)
        lines[k] = ' '.join(words)
    text = '\n'.join(lines)
    if texto != text:
        print('Found errors')
    return text


with open(PATH + 'four_gospeld.txt', encoding='utf-8') as f:
    text1 = f.read()

text1_c = clean_characters(text1)
text1c = separate_punctuation(text1_c)
# Make this function to split "egi" separate since changes word count
text1c = clean_egi(text1c)
text1cc = clean_spell(text1c)
text1cc = clean_spell(text1cc)
text1cc = clean_spell(text1cc)


def test_cleaning(text1cc, text1c, WORDS):
    """Test the number of intersections with WORDS before/after cleaning."""
    WORDc = Counter([word for word in text1c.lower().split() if not word.isnumeric()])
    n_wordc = len(WORDc)
    WORDcc = Counter([word for word in text1cc.lower().split() if not word.isnumeric()])
    n_wordcc = len(WORDcc)
    WORDSc = WORDS.copy()
    WORDScc = WORDS.copy()
    print("# unique words:", len(WORDc), len(WORDcc))
    WORDc.update(WORDSc)
    WORDcc.update(WORDScc)
    print("Intersection with WORDS: ")
    print(len(WORDS)-(len(WORDc)-n_wordc), len(WORDS)-(len(WORDcc)-n_wordcc))
