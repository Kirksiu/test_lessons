n = int(input())

for c in range(2, n):
    if n % c == 0:
        break
print(c)
