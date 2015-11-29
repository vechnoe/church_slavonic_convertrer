import sys
import textwrap

from utils import convert

if __name__ == '__main__':
    info = 'Usage: converter.py input.txt'
    try:
        source = sys.argv[1]
    except (TypeError, ValueError, IndexError):
        sys.exit(info)
    if len(sys.argv) < 2:
        sys.exit(info)

    with open(source) as file:
        out_line = ''.join(line for line in file)
        out_line = out_line.replace('-\n', '').replace('\n', ' ')

    with open('converted.txt', 'w') as out:
        source_str = convert(out_line)
        out.write(textwrap.fill(source_str, 60))
