import numpy as np

a = [3, 2, 5, 1, 4]  # Creating Numpy 1D array from list
b = np.array(a)
print(b)
print(np.array([5, 6, 7, 8, 9]))  # Creating Numpy 1D array without list
c = []  # Creating Numpy 1D array by taking input from user
z = int(input("Enter size of array: "))
for i in range(z):
    val = int(input("Enter number: "))
    c.append(val)
print(np.array(c), '\n')
print(np.random.random(5))  # returns any random values
print(np.random.rand(5))  # returns random values between '0' and '1'
print(np.random.randn(5))  # returns random values near to 0
print(np.random.randint(1, 10, 5))  # returns "_5_" random integral value starting from "_1_" to "_9_"
print(np.linspace(1, 2, 5))  # returns "_5_" values between "_1_" and "_2_" having equal gap difference
print(np.arange(1, 10))  # returns all integral values between "_1_" and "_9_"
print(np.tile([1, 2], 5))  # repeats the value no. of times provided
print(np.ndim(b))  # returns the dimension
print(np.shape(b))  # returns the shape
print(np.size(b))  # returns the size
print(np.zeros(5), '\n')  # return 1D array with value '0'
print(np.zeros((3, 2)), '\n')  # return 2D array with value '0'
print(np.ones(5), '\n')  # return 1D array with value '1'
print(np.ones((3, 2)), '\n')  # return 2D array with value '1'
print(np.eye(3), '\n')  # returns 2D array with diagonal elements as '1' and rest as '0'
print(np.eye(2, 3), '\n')  # returns 2D array with diagonal elements as '1' and rest as '0'
print(np.diag([1, 2, 3, 4]), '\n')  # returns 2D array with diagonal elements as given values and rest as '0'
print(np.min(b))  # returns minimum value
print(np.max(b))  # returns maximum value
print(np.argmin(b))  # returns index of minimum value
print(np.argmax(b))  # returns index of maximum value
print(np.sqrt(b))  # returns square root of numpy array
print(np.sin(b))  # returns sin value of array
print(np.cos(b))  # returns cos value of array
print(np.sort(b))  # sorting
print(np.sort(['z', 'c', 'k', 'f', 'x']))
print(np.where(b == 5))  # searching
print(np.where(b % 2 == 0), '\n')
d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Creating Numpy 2D array from a list
e = np.array(d)
print(e, '\n')
print(np.array([[4, 5, 6], [1, 2, 3], [7, 8, 9]]), '\n')  # Creating Numpy 2D array without list
print(np.ndim(e))  # returns the dimension
print(np.shape(e))  # returns the shape
print(np.size(e))  # returns the size
f = []  # Creating Numpy 2D array by taking input from user
y = int(input("Enter number of rows: "))
x = int(input("Enter number of columns: "))
for i in range(y):
    w = []
    for j in range(x):
        value = int(input("Enter Value: "))
        w.append(value)
    f.append(w)
print(np.array(f), '\n')
g = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
h = g.reshape(3, 3)  # reshaping from 1D to 2D
print(h, '\n')
print(h.reshape(9))  # reshaping from 2D to 1D
i = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(i.reshape(2, -1), '\n')  # reshaping with -1 concept
print(i.reshape(3, -1), '\n')
print(i.reshape(4, -1), '\n')
print(i.reshape(-1, 2), '\n')  # reshaping with -1 concept
print(i.reshape(-1, 3), '\n')
print(i.reshape(-1, 4), '\n')
# Indexing of 1D array
print(i[:])  # from index 0 to end
print(i[4:])  # from index "_4_" to end
print(i[4:9])  # from index "_4_" to "_8_"
print(i[:8])  # from index "_0_" to "_7_"
print(i[-5:])  # from index "_-5_" to end
print(i[-6:-2])  # from index "_-6_" to "_-3_"
print(i[-6:10], '\n')  # from index "_-6_" to "_9_"
# Indexing of 2D array
j = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(j[:], '\n')
print(j[1:, ], '\n')
print(j[1:, :], '\n')
print(j[:, 1:], '\n')
print(j[1:, 1:], '\n')
print(j[:3, :3], '\n')
print(j[1:3, 1:3], '\n')
# View VS Copy
k = np.array([1, 2, 3, 4, 5])
l = k[1:4]  # View
l[:] = 0
print(k)  # original array gets modified
m = np.array([1, 2, 3, 4, 5])
n = m[1:4].copy()  # Copy
n[:] = 0
print(m, '\n')  # no change in original array
# Conditional selection
print(m > 3)  # returns True or False based on condition
print(m[m > 3])  # returns True values
print(m % 2 == 0)  # returns True or False based on condition
print(m[m % 2 == 0])  # returns True values
# Operations on Numpy array
print(m / 2)
print(m * 2)
print(m + 2)
print(m - 2)
print(m ** 2)
o = np.array([1, 2, 3, 4, 5, 6])
p = np.array([7, 8, 9, 10, 11, 12])
print(p / o)
print(o * p)
print(o + p)
print(o - p, '\n')
q = o.reshape(2, 3)
r = p.reshape(2, 3)
print(r / q, '\n')
print(q * r, '\n')  # element multiplication
print(q + r, '\n')
print(q - r, '\n')
print(q.dot(p.reshape(3, 2)), '\n')  # matrix multiplication
# Broadcasting
m1 = np.array([[1, 2, 3], [4, 5, 6]])
n1 = np.array([[1], [2]])
o1 = np.array([1, 2, 3])
print(m1 + n1, '\n')
print(m1 + o1, '\n')
print(m1 * n1, '\n')
print(m1 * o1, '\n')
print(n1 * o1, '\n')
s = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [5, 6, 7, 8], [1, 2, 3, 4]])
print(np.min(s), '\t', np.max(s))  # returns minimum and maximum of 2D array
print(np.min(s, axis=1))  # returns minimum of 2D array row-wise
print(np.max(s, axis=0))  # returns maximum of 2D array column-wise
print(np.cumsum(s))  # returns cumulative sum of array
print(np.unique(s))  # returns unique elements from array
print(np.unique(s).size)  # returns number of unique elements
print(np.unique(s, return_index=True, return_counts=True),
      '\n')  # returns unique elements + index + number of occurrence of unique element
np.random.shuffle(s)  # shuffles the array
print(s, '\n')
t = np.array([2, 5, 8, 12, 27])
print(
    np.searchsorted(t, 7))  # return the index where "_7_" can be inserted maintaining the sorted order (left to right)
print(np.searchsorted(t, 7, side='right'))  # returns the index searching from right to left

# Prepared by RITURAJ RAMAN
# Note: Only Common built-in functions have been used in above program.
# Run the program for more clarity
