phone_book = {}
count = 0

while True:
    text = input()
    if text.isdigit():
        count = int(text)
        break
    (name, number) = text.split('-')
    phone_book[name] = number

for _ in range(count):
    name = input()
    if name in phone_book:
        print(f'{name} -> {phone_book[name]}')
    else:
        print(f'Contact {name} does not exist.')
