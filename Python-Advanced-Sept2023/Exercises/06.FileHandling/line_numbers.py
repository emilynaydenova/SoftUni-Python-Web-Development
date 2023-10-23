# text.txt must be in the same directory
from pathlib import Path
import string

BASE_DIR = Path(__file__).parent
in_file_path = BASE_DIR / 'text.txt'
out_file_path = BASE_DIR / 'output.txt'

output = []
try:
    with (open(in_file_path, 'r', encoding='utf8') as in_file,
          open(out_file_path, 'w', encoding='utf8') as out_file
          ):
        for idx, line in enumerate(in_file, 1):
            letters_count = len([ch for ch in line if ch.isalpha()])
            punctuation_count = sum([1 for ch in line if ch in string.punctuation])
            output.append(f'Line {idx}: {line[:-1]}({letters_count})({punctuation_count})')

        out_file.write('\n'.join(output))
except FileNotFoundError:
    print(f'File text.txt not found or output.txt not created.')
else:
    print(f'File output.txt is created.')
