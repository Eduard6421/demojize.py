# coding: utf-8

import sys
import os
import codecs
import emoji
import re
from unidecode import unidecode
from functools import partial

ascii_emoji = {
     'o/'     : '👋',
    '</3'     : '💔',
    '<3'      : '💗',
    '8-D'     : '😁',
    '8D'      : '😁',
    ':-D'     : '😁',
    '=-3'     : '😁',
    '=-D'     : '😁',
    '=3'      : '😁',
    '=D'      : '😁',
    'B^D'     : '😁',
    'X-D'     : '😁',
    'XD'      : '😁',
    'x-D'     : '😁',
    'xD'      : '😁',
    ':\')'    : '😂',
    ':\'-)'   : '😂',
    ':-))'    : '😃',
    '8)'      : '😄',
    ':)'      : '😄',
    ':-)'     : '😄',
    ':3'      : '😄',
    ':D'      : '😄',
    ':]'      : '😄',
    ':^)'     : '😄',
    ':c)'     : '😄',
    ':o)'     : '😄',
    ':}'      : '😄',
    ':っ)'     : '😄',
    '=)'      : '😄',
    '=]'      : '😄',
    '0:)'     : '😇',
    '0:-)'    : '😇',
    '0:-3'    : '😇',
    '0:3'     : '😇',
    '0;^)'    : '😇',
    'O:-)'    : '😇',
    '3:)'     : '😈',
    '3:-)'    : '😈',
    '}:)'     : '😈',
    '}:-)'    : '😈',
    '*)'      : '😉',
    '*-)'     : '😉',
    ':-,'     : '😉',
    ';)'      : '😉',
    ';-)'     : '😉',
    ';-]'     : '😉',
    ';D'      : '😉',
    ';]'      : '😉',
    ';^)'     : '😉',
    ':-|'     : '😐',
    ':|'      : '😐',
    ':('      : '😒',
    ':-('     : '😒',
    ':-<'     : '😒',
    ':-['     : '😒',
    ':-c'     : '😒',
    ':<'      : '😒',
    ':['      : '😒',
    ':c'      : '😒',
    ':{'      : '😒',
    ':っC'     : '😒',
    '%)'      : '😖',
    '%-)'     : '😖',
    ':-P'     : '😜',
    ':-b'     : '😜',
    ':-p'     : '😜',
    ':-Þ'     : '😜',
    ':-þ'     : '😜',
    ':P'      : '😜',
    ':b'      : '😜',
    ':p'      : '😜',
    ':Þ'      : '😜',
    ':þ'      : '😜',
    ';('      : '😜',
    '=p'      : '😜',
    'X-P'     : '😜',
    'XP'      : '😜',
    'd:'      : '😜',
    'x-p'     : '😜',
    'xp'      : '😜',
    ':-||'    : '😠',
    ':@'      : '😠',
    ':-.'     : '😡',
    ':-/'     : '😡',
    ':/'      : '😡',
    ':L'      : '😡',
    ':S'      : '😡',
    ':\\'     : '😡',
    '=/'      : '😡',
    '=L'      : '😡',
    '=\\'     : '😡',
    ':\'('    : '😢',
    ':\'-('   : '😢',
    ':-c'	  : '😢',
    '^5'      : '😤',
    '^<_<'    : '😤',
    'o/\\o'   : '😤',
    '|-O'     : '😫',
    '|;-)'    : '😫',
    ':###..'  : '😰',
    ':-###..' : '😰',
    'D-\':'   : '😱',
    'D8'      : '😱',
    'D:'      : '😱',
    'D:<'     : '😱',
    'D;'      : '😱',
    'D='      : '😱',
    'DX'      : '😱',
    'v.v'     : '😱',
    '8-0'     : '😲',
    ':-O'     : '😲',
    ':-o'     : '😲',
    ':O'      : '😲',
    ':o'      : '😲',
    'O-O'     : '😲',
    'O_O'     : '😲',
    'O_o'     : '😲',
    'o-o'     : '😲',
    'o_O'     : '😲',
    'o_o'     : '😲',
    ':$'      : '😳',
    '#-)'     : '😵',
    ':#'      : '😶',
    ':&'      : '😶',
    ':-#'     : '😶',
    ':-&'     : '😶',
    ':-X'     : '😶',
    ':X'      : '😶',
    ':-J'     : '😼',
    ':*'      : '😽',
    ':^*'     : '😽',
    'ಠ_ಠ'    : '🙅',
    '*\\0/*'  : '🙆',
    '\\o/'    : '🙆',
    ':>'      : '😄',
    '>.<'     : '😡',
    '>:('     : '😠',
    '>:)'     : '😈',
    '>:-)'    : '😈',
    '>:/'     : '😡',
    '>:O'     : '😲',
    '>:P'     : '😜',
    '>:['     : '😒',
    '>:\\'    : '😡',
    '>;)'     : '😈',
    '>_>^'    : '😤',
    '(・ω・)'   : '😁'
}   


abbreviations = {
	'gf' : 'girlfriend',
	'm' : 'am',
	'u' : 'you',
	'r' : 'are',
	'ur' : 'your',
	'k' : 'ok',
	'fu' :'fuck you',
	'fn' : 'fucking',
	'im' : 'i am',
	'i\'m' : 'i am',
	'i\'ll' : 'i will',
	'ill' : 'i will',
	'i\'ve' : 'i have',
	'ive' : 'i have',
	'don\'t' : 'do not',
	'dont' : 'do not',
	'doesn\'t' : 'does not',
	'doesnt' : 'does not',
	'didin\'t' : 'did not',
	'didint' : 'did not',
	'that\'s' : 'that is',
	'thats' : 'that is',
	'it\'s' :'it is',
	'its' : 'it is', # In the dataset it seems that people use frequently this word incorrectly so it makes sense to change it so
	'can\'t' : 'can not',
	'cant' : 'can not',
	'c\'mon' : 'come on',
	'wtf' : 'what the fuck',
	'ftw' : 'for the win',
	'gtfo' : 'get the fuck out',
	'lol' : 'lots of laughs',
	'rofl' : 'rolling on the floor laughing',
	'hw' : 'how',
	'how\'s' : 'how is',
	'hows' :' how is',
	'i ve' : 'i have',
	'aren\'t' : 'are not',
	'nvm' : 'nevermind',
	'g2g' : 'got to go',
	'wt' : 'what',
	'kno' : 'know',
	'nd' : 'second',
	'fst' : 'first',
	'2nite' : 'tonight',
    'how\'s' : 'how is',
    'what\'s' : 'what is',

}


def replace(match):
    return abbreviations[match.group(0)]

def is_exist(fpath):
    if os.path.isfile(fpath):
        return True
    print("Here is the path")
    print (fpath)
    print ("Error: File {} does not exist. Skipped.".format(fpath))
    return False


def run(infpath, outfpath):
    print ("demojizing... {}".format(infpath))
    # read
    data = []

    regex_emoji_sequence = re.compile(r"(:[A-Za-z_-]+:):")
    regex_emoji_after_word = re.compile(r"([A-Za-z-.])(:[A-Za-z_-]+:)")
    regex_abreviations = re.compile(r"\b[a-zA-Z]+\b")
    regex_tab = re.compile(r"\t")

    with codecs.open(infpath, "r", "utf-8") as fp:
        for line in fp:

            line = line.lower()
            line = re.sub('|'.join(r'\b%s\b' % re.escape(s) for s in abbreviations), replace, line) 

            
            for word,trueemoj in ascii_emoji.items():
            	line = line.replace(word,trueemoj) 
            
            line = emoji.demojize(line)
            line = unidecode(line)
            # Regex replace must take in account the older replaces. As such we cannot use only one call to replace.

            while True:
                newline = regex_emoji_sequence.sub('\\1 :',line,count=1)
                if newline == line:
                    break
                else:
                    line = newline

            while True:
                newline = regex_emoji_after_word.sub('\\1 \\2',line,count=1)
                if newline == line:
                    break
                else:
                    line = newline


            while True:
                newline = regex_tab.sub(' <end> ',line,count=1)
                if newline == line:
                    break
                else:
                    line = newline


            data.append(line)
        # save
    with codecs.open(outfpath, "w", "utf-8") as fp:
        for line in data:
            fp.write(line)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print ("Usage: python demojize.py <path_to_file>")
        print ("Usage: python demojize.py <path_to_dir> <file_name>...")
        sys.exit()

    if len(args) == 2:
        infpath = args[1]
        if is_exist(infpath):
            indir, fname = os.path.split(infpath)
            outfpath = os.path.join(indir, "demojized_{}".format(fname))
            run(infpath, outfpath)
    else:
        indir = args[1]
        for fname in args[2:]:
            fname = os.path.split(fname)[1]
            if "demojized_" in fname:
                continue
            infpath = os.path.join(indir, fname)
            if not is_exist(infpath):
                continue
            outfpath = os.path.join(indir, "demojized_{}".format(fname))
            run(infpath, outfpath)
    print('Task has finished successfully')