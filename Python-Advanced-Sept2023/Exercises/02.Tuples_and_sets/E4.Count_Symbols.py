text = input()
letters = tuple(set(text))  # unique letters

for ch in sorted(letters):
    print(f'{ch}: {text.count(ch)} time/s')