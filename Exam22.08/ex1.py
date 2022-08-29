from string import punctuation

book = {'''Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
 when an unknown printer took a galley of type and scrambled it to make a type specimen book.
 It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
  It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
  and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''}
s = [word.strip(punctuation) for word in ' '.join([line.strip() for line in book]).split()]
s2 = [word.lower() for word in s]
set_ = set(s2)
dct = {i:s2.count(i) for i in set_}

# кто если не ты)
import sys
# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
for i in lst_in[::-1]:
    print(*i[::-1])