a = 5  # Variable declaration/ initialization/ Assigning
b, c = 1, 2  # Variable declaration/ initialization/ Assigning
print("Value of a: ", a, ", b: ", b, ", c: ", c)  # Displays the output
d = input("Enter string value: ")  # Takes input(string) from user
e = int(input("Enter integral value: "))  # Takes input(integer) from user
print("Value of d: ", d, " and e: ", e)

# ARITHMETIC OPERATOR
# + ->Addition
# - ->Subtraction
# * ->Multiplication
# / ->Division
# % ->Modulus
# ** -> Exponent
# // ->Floor division

# RELATIONAL OPERATOR
# > ->Greater than
# >= ->Greater than or equal to
# < ->Less than
# <= ->Less than or equal to
# == ->Equal to
# != or <> ->Not equal to

# ASSIGNMENT OPERATOR
# += ->a += b ->a = a + b
# -= ->a -= b ->a = a - b
# *= ->a *= b ->a = a * b
# /= ->a /= b ->a = a / b
# %= ->a %= b ->a = a % b

# LOGICAL OPERATOR
# and ->returns True if all condition is true
# or ->returns True if any one condition is true
# not ->reverse the output (True <-> False)

# IDENTITY OPERATOR
# is ->checks the data type, ex:- if(type(x) is int): print("abc")
# is not ->checks the data type, ex:- if(type(x) is not int): print("abc")

# MEMBERSHIP OPERATOR
# in ->checks the availability of element, ex:- if(x in a): print("abc")
# not in ->checks the availability of element, ex:- if(x not in a): print("abc")

# BITWISE OPERATOR
# & ->bitwise AND operator
# | ->bitwise OR operator
# ^ ->bitwise XOR operator
# - ->bitwise NOR operator
# << ->bitwise LEFT shift operator
# >> ->bitwise RIGHT shift operator

# ***** CONTROL STATEMENT *****
# Selection Statement ->if, elif, else
# Example program to print maximum among three
f, g, h = 5, 2, 11
if f > g and f > h:
    print("maximum is f i.e. ", f)
elif g > f and g > h:
    print("maximum is g i.e. ", g)
else:
    print("maximum is h i.e. ", h)

# Looping statement ->while, for
# Example program of while to print from 1 to 10
i = 1
while i <= 10:
    print(i, end='  ')
    i = i + 1
print()

# Example program of for to print from 1 to 10
# for i in range(start_value, end+1_value, step_value)
for i in range(1, 11):
    print(i, end='  ')
print('\n')


# FUNCTIONS
# Example program of declaring and calling a function
def add():  # defining function
    a, b = 10, 20
    print("Sum of ", a, " and ", b, ": ", a + b)


add()  # function is called


# Passing arguments/parameters to function
def add2(x, y):
    print("Sum of ", x, " and ", y, ": ", x + y)


a, b = 15, 25
add2(a, b)
add2(5, 15)


# Passing arguments/parameters to function with return
def add3(x, y):
    z = x + y
    return z


a, b = 20, 30
print("Sum of ", a, " and ", b, ": ", add3(a, b))


# Default argument to a function
def add4(x, y=25, z=35):
    print("Sum of ", x, y, " and ", z, ": ", x + y + z)


add4(5)
add4(5, 15)
add4(5, 10, 15)
print()

# Break and Continue statement
for i in range(10):
    if i == 4:
        continue  # terminates the following statement
    if i == 8:
        break  # terminates the loop
    print(i, end=' ')
print('\n')

# STRING
a = 'Rituraj Raman'
b = 'is learning python'
print(a, b)
for i in a:
    print(i, end=' ')
print()

print('Rituraj ' + 'Raman')  # concatenation operator
print('Rituraj ' * 3)  # replication operator
print('a' in 'Rituraj')  # membership operator
print('a' not in 'Rituraj')  # membership operator
# String slicing ->string[start_value : end+1_value : step_value)
print(a[:])
print(a[2:])
print(a[2:6])
print(a[:6])
print(a[-8:])
print(a[-8:-3])
print(a[::3])
print(len(a))
print('riTUraj'.capitalize())  # first letter to upper and all others to lower
print(a.find('raj'))  # returns the first index of substring
print('rituraj'.isalnum())  # checks if the string is alphanumeric or not
print('12345'.isdigit())  # checks the string is numeric or not
print(' '.isspace())  # checks the string is a space or not
print(a.replace(' ', '-'))  # replace the substring with new substring
print(a.upper())  # convert the string to uppercase
print(a.lower())  # convert the string to lowercase
print(a.split(' '), '\n')  # splits the string from the specified substring

# DATA STRUCTURES
# LIST ->Mutable
a = []  # blank list
a_ = list()  # blank list
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list with values
c = ['a', 1, 'abc', 1.5]
print(a, a_, '\n', b, '\n', c)
for i in b:  # traversing list
    print(i, end='  ')
print()
if 5 in b:  # membership operator
    print('yes 5 is available')
# List slicing ->list[start_value : end+1_value : step_value)
print(b[:])
print(b[2:])
print(b[2:6])
print(b[:6])
print(b[-8:])
print(b[-8:-3])
print(b[::3])
d = c.copy()  # list copying
print(d)
c[1] = 5  # list updating
print(c)
del c[1:3]  # list deletion
print(c)
del c[0]  # list deletion
print(c)
list1 = [30, 10, 70, 40, 10]
list2 = [90, 50, 20, 60, 80]
print(len(list1))  # returns size of list
print(max(list1))  # returns maximum among list
print(min(list1))  # returns minimum among list
print(list1.count(10))  # returns frequency of element
print(list1.index(10))  # returns index of element
print(list1 + list2)  # concatenates the lists
print(list1 * 2)  # replication of list
list1.append(5)  # add element at the list
print(list1)
list1.insert(2, 55)  # insert element at given index
print(list1)
list1.extend(list2)  # concatenates two lists
print(list1, '\n')
list1.remove(55)  # removes the specified element
print(list1)
list1.pop()  # deletes the last element of list
print(list1)
list1.reverse()  # reverse the list
print(list1)
list1.sort()  # sorting in ascending order
print(list1)
list1.sort(reverse=True)  # sorting in descending order
print(list1)

# TUPLES ->immutable and ordered
a = ()  # blank tuple
b = tuple()  # blank tuple
c = (1,)  # single valued tuple
d = (1, 'a', 'abc', 1.5)  # multi valued tuple
print(a, '\n', c, '\n', d)
for i in d:  # tuple traversing
    print(i, end='  ')
print()
if 1.5 in d:  # membership operator
    print('yes 1.5 is available')
# Tuple slicing ->tuple[start_value : end+1_value : step_value)
b = (1, 2, 3, 4, 5, 6, 7, 8, 9, 9)
print(b[:])
print(b[2:])
print(b[2:6])
print(b[:6])
print(b[-8:])
print(b[-8:-3])
print(b[::3])
print(len(b))  # returns size of tuple
print(max(b))  # returns maximum among tuple
print(min(b))  # returns minimum among tuple
print(b.count(9))  # returns frequency of element
print(b.index(9))  # returns index of element
print(c + d)  # concatenation of tuple
print(d * 2, '\n')  # replication of tuple

# DICTIONARY ->mutable and unordered
a = {}  # blank dictionary
a_ = dict()  # blank dictionary
b = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(a, '\n', a_, '\n', b)
c = {'a': [1, 2, 3, 4, 5],
     'b': [6, 7, 8, 9, 10],  # 2D dictionary
     'c': [11, 12, 13, 14, 15]}
print(c, '\n')
# Accessing dictionary
print(b[3])  # returns value at index "_3_"
print(b.get(4))  # returns value at index "_4_"
for i in b:  # keys
    print(i, end='  ')
print()
for i in b:  # values
    print(b[i], end='  ')
print()
for i in b.keys():  # keys
    print(i, end='  ')
print()
for i in b.values():  # values
    print(i, end='  ')
print()
for i in b:  # keys + values
    print(i, ' ', b[i])
for i in b.items():  # keys + values (item = key + value)
    print(i, end='  ')
print()
for (i, j) in b.items():  # keys + values (item = key + value)
    print((i, j), end='  ')
print('\n')

# Changing and Adding values in a dictionary
b[1] = 'f'  # modifies if the key exists
print(b)
b[6] = 'g'  # add new key with value if key doesn't exists
print(b, '\n')

if 3 in b:  # checks the availability of keys
    print('Yes 3 is available')
else:
    print('not available')

if 'c' in b.values():  # checks the availability of values
    print('Yes C is available')
else:
    print('not available')
print()
# Inbuilt dictionary functions
print(len(b))  # returns the number of items in a dictionary (item = key + value)
a = b.copy()  # copies the dictionary
print(a)
b.pop(4)  # deletes the item at specified value (item = key + value)
print(b)
b.popitem()  # deletes the item at the end (item = key + value)
print(b)
a.clear()  # deletes the complete items of dictionary leaving the dictionary empty
print(a)
del b[3]  # deletes the item at specified value (item = key + value)
print(b)
b.update({3: 'c', 4: 'd'})  # insert items in the list (item = key + value)
print(b)
del b  # deletes entire dictionary
# print(b) -> will give an error because dictionary 'b' has been deleted
a = ('a', 'b', 'c')
b = (1)
c = dict.fromkeys(a, b)  # or c = c.fromkeys(a,b)
print(c, '\n')  # ^returns a new dictionary with specified keys and value

# SET ->unordered/unindexed, mutable and unique elements
a = set()  # empty set
b = {1, 2, 3, 4, 5}  # set with values
c = {5, 6, 7, 8, 9, 9, 9}  # (run the program to see uniqueness of a set)
print(a, '\n', b, '\n', c)
x = [1, 2, 3, 4, 5]
print(set(x))  # creating set from list
b.add(6)  # add single value to set
print(b)
b.update((7, 8, 9), {10, 11, 12}, [13, 14, 15])  # add multiple value to set
print(b)
b.discard(15)  # delete the specified value from the set
print(b)
b.remove(14)  # delete the specified value from the set
print(b)  # NOTE: .remove gives error, if the value to be deleted is not present
b.clear()  # delete all values of set leaving the set empty
print(b)
# Set operations
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a | b)  # or a.union(b)  Returns UNION
print(a & b)  # or a.intersection(b)  Returns INTERSECTION
print(a - b)
print(a ^ b, '\n\n')  # or a.symmetric_difference(b)  Returns SYMMETRIC DIFFERENCE

# Data type conversion
lst = [1, 2, 3, 4, 5]
tup = (6, 7, 8, 9, 10)
st = {11, 12, 13, 14, 15}
dct = {1: 'a', 2: 'b', 3: 'c'}
list1 = list(tup)  # from tuple to list
list2 = list(st)  # from set to list
list3 = list(dct)  # from dictionary-key to list
list4 = list(dct.values())  # from dictionary-values to list
tup1 = tuple(lst)  # from list to tuple
tup2 = tuple(st)  # from set to tuple
tup3 = tuple(dct)  # from dictionary-key to tuple
tup4 = tuple(dct.values())  # from dictionary-values to tuple
set1 = set(lst)  # from list to set
set2 = set(tup)  # from tuple to set
set3 = set(dct)  # from dictionary-key to set
set4 = set(dct.values())  # from dictionary-values to set
print(lst, type(lst))
print(tup, type(tup))
print(st, type(st))
print(list1, type(list1))
print(list2, type(list2))
print(list3, type(list3))
print(list4, type(list4))
print(tup1, type(tup1))
print(tup2, type(tup2))
print(tup3, type(tup3))
print(tup4, type(tup4))
print(set1, type(set1))
print(set2, type(set2))
print(set3, type(set3))
print(set4, type(set4))

# Prepared by RITURAJ RAMAN
# Note: Only Common built-in functions have been used in above program.
# Run the program for more clarity.
