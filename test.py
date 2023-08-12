import numpy as np

a = np.array([[1, 2], [3, 4]])

np.tile(a, 2)
# array([[1, 2, 1, 2],
#        [3, 4, 3, 4]])

np.tile(a, (2, 1))
# array([[1, 2],
#        [3, 4],
#        [1, 2],
#        [3, 4]])
print(np.tile(a, (2, 2)))