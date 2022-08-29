n = 1
i = 0
while n != 0:
    i += n
    n = int(input())
    if n % 2 != 0:
        continue
    print(n - 1)
