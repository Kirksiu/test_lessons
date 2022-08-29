n = int(input())
s = 1000
i = 0
while i < n:
    s *= 1.05
    i += 1
print(round(s, 2))

