from string import punctuation

with open('bulgakov.txt', encoding='utf-8') as book:
    s = [word.strip(punctuation) for word in ' '.join([line.strip() for line in book.readlines()]).split()]
    s2 = [word.lower() for word in s if len(word) > 3]
    set_ = set(s2)
    dct = {i:s2.count(i) for i in set_}


dct = {}
for i in s2:
    if i not in dct:
        dct[i] = 1
    else:
        dct[i] += 1

keys = sorted(dct, key=dct.get, reverse=True)
[print(f'{ind}. {word} - {dct[word]}') for ind, word in enumerate(keys, 1) if ind <= 10]
