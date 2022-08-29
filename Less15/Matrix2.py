import random
lst1 = [i ** 3 if i < 50 else i ** 2 for i in range(100) if i%3 == 0] # список
lst = (i ** 3 if i < 50 else i ** 2 for i in range(100) if i%3 == 0) # генератор

print(*lst)
#print(lst1)
