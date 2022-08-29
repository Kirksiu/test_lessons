import numpy as np

a = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))

print(a)


new_arr = a.reshape(a.size)
new_arr = new_arr[::-1]
new_arr = new_arr.reshape(a.shape)

print(new_arr)
