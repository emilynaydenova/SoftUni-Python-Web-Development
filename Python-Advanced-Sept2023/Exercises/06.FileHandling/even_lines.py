# text.txt must be in the same directory
from pathlib import Path

BASE_DIR = Path(__file__).parent
file_path = BASE_DIR / 'text.txt'

try:
    with open(file_path) as f:
        for count, line in enumerate(f):
            if count % 2 == 0:
                new_line = ''.join(['@' if ch in "-,.!?" else ch for ch in line])
                words = new_line.split()[::-1]
                print(' '.join(words))
except FileNotFoundError:
    print('File not found')
