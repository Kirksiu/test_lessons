import sys
l = []
mat = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [5, 4, 3]]
for i in mat[::-1]:
    print(*i[::-1])


mat2 = mat[0][::-1]
mat3 = mat[1][::-1]
mat4 = mat[2][::-1]
mat5 = mat[3][::-1]
l.append(mat5)
l.append(mat4)
l.append(mat3)
l.append(mat2)

print(*l)

