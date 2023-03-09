import sys
from mapping import CHARA_MAP

def process_line(line):
    if line[0] in '<[':
        return f'#TODO: {line}'
    if ': ' in line[:20]:
        chara, text = line.split(': ', 1)
        chara = chara.lower()
        chara = CHARA_MAP.get(chara, chara)
        return f'{chara} {repr(text)}'
    return f'n {repr(line)}'

for line in open(sys.argv[1], 'r'):
    print('    ' + process_line(line))
