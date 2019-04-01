# coding: utf-8

import sys
import os
import codecs
import emoji


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
    ''
}   





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
    with codecs.open(infpath, "r", "utf-8") as fp:
        for line in fp:
            for word,trueemoj in ascii_emoji.items():
                line = line.replace(word,trueemoj) 
            line = emoji.demojize(line)
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