import pandas as pd
import numpy as np

# *** SERIES ***
a = pd.Series(dtype=object)  # creating pandas empty series
z = [1, 2, 3, 4, 5]
b = pd.Series(z)  # creating pandas series using existing list
c = pd.Series([6, 7, 8, 9, 10])  # creating pandas series from new list
d = pd.Series("Hello")
print(a, '\n\n', b, '\n\n', c, '\n\n', d, '\n')
y = np.array([1, 2, 3, 4, 5])
e = pd.Series(y)  # creating pandas series from numpy array
f = pd.Series(np.array([5, 6, 7, 8, 9, 10]))
g = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})  # creating pandas series from dictionary
h = pd.Series([1, 2, 3, 4, 5], index=[5, 10, 15, 20, 25])  # specifying index values
i = pd.Series(1000, index=[5, 10, 15, 20])  # will assign all index with same value
print(e, '\n\n', f, '\n\n', g, '\n\n', h, '\n\n', i, '\n')

a = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10})
# Some Pandas inbuilt functions
print(a.index)  # returns the index values
print(a.values)  # returns the data/values
print(a.dtype)  # returns the datatype of object
print(a.shape)  # returns the shape
print(a.ndim)  # returns the dimension
print(a.size)  # return the size
print(a.nbytes)  # return the total bytes captured
print(type(a))  # returns the type of object
print(a.empty)  # checks whether the object is empty or not
print(a.head())  # returns 5(default) values from top
print(a.head(3))  # returns "_3_" values from top
print(a.tail())  # returns 5(default) values from bottom
print(a.tail(3), '\n')  # returns "_3_" values from Bottom
print(a[2], '\n', a[4], '\n', a[7], '\n')  # accessing elements from series

# Slicing in series ->object[start_value : end+1_value : step_value)
print(a[:])
print(a[2:])  # or a['c':]
print(a[2:6])  # or a['c':'g']
print(a[:6])  # or a[:'g']
print(a[-8:])
print(a[-8:-3])
print(a[::3], '\n')

# Adding/Modifying Series object's value

a['k'] = 15  # adding series object's value
print(a)
a[0] = 7  # modifying series object's value
print(a)
a['a':'c'] = 9  # modifying series object's value
print(a)
a[0:3] = 11  # modifying series object's value
print(a, '\n')

# Renaming/modifying index
a = a.rename({'a': 's', 'b': 't'})  # renaming specific index
print(a, '\n')
a.index = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p']  # renaming every index
print(a, '\n')

# Vector operation on series object
print(a + 2)
print(a - 2)
print(a * 2)
print(a ** 2)
print(a / 2)
print(a // 2)
print(a % 2, '\n')

# Arithmetic operation on series object
a = pd.Series([1, 2, 3, 4])
b = pd.Series([5, 6, 7, 8])
c = pd.Series([9, 10])
print(a + b)
print(a + c)
print(a - b)
print(a - c)
print(a * b)
print(a * c)

# Filtering values in series
a = pd.Series([5, 7, 10, 15, 22, 27, 30])
print(a > 15)  # checks the condition and returns True/False
print(a[a > 10])  # checks the condition and returns values
print(a % 2 == 0)  # checks the condition and returns True/False
print(a[a % 2 == 0], '\n')  # checks the condition and returns values

# Sorting in series
a = pd.Series([22, 10, 5, 30, 15, 7, 27], index=[3, 6, 9, 7, 4, 1, 5])
print(a.sort_values())  # values in ascending order
print(a.sort_values(ascending=False))  # values in descending order
print(a.sort_index())  # index in ascending order
print(a.sort_index(ascending=False), '\n\n\n')  # index in descending order

# *** DATAFRAMES ***
print('*****DATAFRAME*****')
a = pd.DataFrame(dtype=object)  # empty dataframe
print(a, '\n')
b = {'a': [10, 20, 30, 40], 'b': [50, 60, 70, 80], 'c': [20, 40, 60, 80]}
df = pd.DataFrame(b)  # creating dataframe object using 2D dictionary having list as values.
print(df, '\n')

df = pd.DataFrame(b, index=['p', 'q', 'r', 's'])  # user defined index
print(df, '\n')

df = pd.DataFrame({'a': {'p': 10, 'q': 20, 'r': 30, 's': 40},
                   'b': {'p': 50, 'q': 60, 'r': 70, 's': 80},
                   'c': {'p': 20, 'q': 40, 'r': 60,
                         's': 80}})  # creating dataframe object using 2D dictionary having dictionary as values.
print(df, '\n')

a = {'p': 10, 'q': 20, 'r': 30, 's': 40}
b = {'p': 50, 'q': 60, 'r': 70, 's': 80}
c = {'p': 20, 'q': 40, 'r': 60, 's': 80}
lst = [a, b, c]
df = pd.DataFrame(lst)  # creating dataframe object using list of dictionary
print(df, '\n')

a = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
df = pd.DataFrame(a, index=['x', 'y', 'z'], columns=['a', 'b', 'c'])  # creating dataframe object using 2D list
print(df, '\n')

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
df = pd.DataFrame(arr)  # creating dataframe object using ndarray (Numpy Array)
print(df, '\n')

arr = np.array([[10, 20, 30, 40], [50, 60, 70], [80, 90]], dtype=object)
df = pd.DataFrame(arr, columns=['a'])  # creating dataframe object using ndarray having different shapes
print(df, '\n')

a = pd.Series(['p', 'q', 'r'])
b = pd.Series([1, 2, 3])
c = pd.Series([1.5, 2.5, 3.5])
dct = {'x': a, 'y': b, 'z': c}
df1 = pd.DataFrame(dct)  # creating dataframe object using series object
print(df1, '\n')

df2 = pd.DataFrame(df1)  # creating dataframe object using dataframe object
print(df1, '\n\n')

# DataFrame attributes
a = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
df = pd.DataFrame(a, index=['x', 'y', 'z'], columns=['a', 'b', 'c'])
print(len(df))  # returns length of dataframe
print(df.index)  # returns the index values
print(df.columns)  # returns the column values
print(df.axes)  # returns index and column values
print(df.empty)  # checks if dataframe object is empty or not
print(df.size)  # returns the size of dataframe object
print(df.shape)  # returns the shape of dataframe object
print(df.ndim)  # returns the dimension of dataframe object
print(df['b'].dtypes, '\n')  # returns datatype of specific dataframe object
print(df.dtypes, '\n')  # returns datatype of all dataframe object
print(df.head())  # returns 5(default) values from top
print(df.head(3))  # returns "_3_" values from top
print(df.tail())  # returns 5(default) values from bottom
print(df.tail(3), '\n')  # returns "_3_" values from Bottom
print(df.count(), '\n')  # returns number of values present in index
# or df.count(0)             #  returns number of values present in index
# or df.count(axis='index')  #  returns number of values present in index
print(df.count(1), '\n')  # returns number of values present in columns
# or df.count(axis='columns') #  returns number of values present in columns
print(df.T, '\n')  # transpose the dataframe object
print(df.values, '\n\n')  # returns dataframe values in the form of ndarray (Numpy Array)
print('*********************************')
# Selecting/Accessing/Slicing dataframe object
print(df.a, '\n')  # returns values present in "_a_" column
print(df['a'], '\n')  # returns values present in "_a_" column
print(df[['a', 'c']], '\n')  # returns values present in multiple column
print(df.loc['x'], '\n')  # returns values present in "_x_" index
print(df.loc['x', :], '\n')  # returns values present in "_x_" index
print(df.iloc[0, :], '\n')  # returns values present in "_x_" index
print(df.loc[:], '\n')  # returns all values of the dataframe
print(df.iloc[:], '\n')  # returns all values of the dataframe
print(df.loc[:, :], '\n')  # returns all values of the dataframe
print(df.iloc[:, :], '\n')  # returns all values of the dataframe
print(df.loc[:, 'a':'b'], '\n')  # returns values in colums "_a_" to "_b_" of all rows
print(df.iloc[:, 0:2], '\n')  # returns values in colums numbered "_0_" to "_1_" of all rows
print(df.loc['x':'y', 'a':'b'], '\n')  # returns values in colums "_a_" to "_b_" of "_x_" to "_y_" rows
print(df.iloc[0:2, 0:2], '\n')  # returns values in colums "_0_" to "_1_" of "_0_" to "_1_" rows
# Note: .loc works on index values and .iloc works on index number

# Accessing/Modifying individual elements
print(df.a['y'])  # returns the value present at column "_a_" and row "_y_"
print(df.at['y', 'a'])  # returns the value present at column "_a_" and row "_y_"
print(df.iat[1, 0])  # returns the value present at column "_a_" and row "_y_"
print(df.loc['y'].at['a'])  # returns the value present at column "_a_" and row "_y_"
print(df.iloc[1].at['a'], '\n')  # returns the value present at column "_a_" and row "_y_"
df.a['x'] = 'R'  # modifying the value present at column "_a_" and row "_x_"
df.at['y', 'a'] = 'r'  # modifying the value present at column "_a_" and row "_y_"
df.iat[2, 0] = 'Rr'  # modifying the value present at column "_a_" and row "_z_"
print(df, '\n\n')

# Adding/Modifying a column
df['d'] = 10  # adding column with same value
df['e'] = [1, 2, 3]  # adding column
df.loc[:, 'f'] = [4, 5, 6]  # adding column
print(df, '\n')
df.insert(loc=3, column='cd', value=[1, 2, 3])  # adding column at specific position
print(df, '\n')
df.d = [1, 5, 9]  # modifying column
df['e'] = 15  # modifying column
df.loc[:, 'f'] = [1, 2, 3]  # modifying column using loc attribute
print(df, '\n')
df.iloc[:, 5] = [12, 14, 16]  # modifying column using iloc attribute
print(df, '\n\n')

# Deleting column
del df['f']  # deletes "_f_" column permanently
print(df, '\n')
print(df.drop(['cd', 'e'], axis=1), '\n\n')  # deletes "_cd_", "_e_" column temporary
df = df.drop(['cd', 'd'], axis=1)  # deletes "_cd_", "_d_" column permanently
del df['e']  # deletes "_e_" column permanently

# Adding/Modifying a row
df.loc['v'] = [1, 2, 3]  # adding row
print(df, '\n')
df.at['w', :] = [8, 5, 2]  # adding row
print(df, '\n')
df.iloc[1] = [1, 2, 3]  # modifying row at index "_1_"
print(df, '\n')
df.at['w', :] = [2, 4, 6]  # modifying row
print(df, '\n\n')

# Deleting row
print(df.drop(['w'], axis=0), '\n\n')  # deletes "_w_" row temporary
df = df.drop(['v'], axis=0)  # deletes "_v_" row permanently
print(df, '\n\n')

# Renaming rows/columns

print(df.set_axis(['k', 'l', 'm', 'n'], axis=0), '\n')  # renaming rows temporary
print(df.set_axis(['p', 'q', 'r'], axis=1), '\n')  # renaming columns temporary
df.set_axis(['k', 'l', 'm', 'n'], axis=0, inplace=True)  # renaming rows permanently
df.set_axis(['p', 'q', 'r'], axis=1, inplace=True)  # renaming columns permanently
print(df, '\n')
df.index = ['w', 'x', 'y', 'z']  # renaming rows permanently
df.columns = ['a', 'b', 'c']  # renaming columns permanently
print(df, '\n')
df = df.rename({'a': 'm', 'c': 'n'}, axis='columns')  # renaming columns permanently
df = df.rename({'x': 'p', 'y': 'q'})  # renaming rows permanently
print(df, '\n')

# Iteration on DataFrame
a = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
df = pd.DataFrame(a, index=['x', 'y', 'z'], columns=['a', 'b', 'c'])
for (i, j) in df.iterrows():  # iterating row wise
    print("Row: ", i, "\nvalues: \n", j)
print()
for (i, j) in df.iterrows():  # iterating row wise
    print("\nRow: ", i, "\nvalues: ")
    for h in j:
        print(h)
print()
for (i, j) in df.iterrows():  # iterating row wise in a specific column
    print("Value of b in ", i, ": ", j['b'])
print('\n')

for (i, j) in df.iteritems():  # iterating column wise
    print("Column: ", i, "\nvalues: \n", j)
print()
for (i, j) in df.iteritems():  # iterating column wise
    print("\nColumn: ", i, "\nvalues: ")
    for h in j:
        print(h)
print()
for (i, j) in df.iteritems():  # iterating column wise in a specific row
    print("Value of y in ", i, ": ", j['y'])
print('\n')

# Binary operation on dataframe
a = pd.DataFrame([[10, 20], [30, 40]])
b = pd.DataFrame([[80, 70], [60, 50]])
c = pd.DataFrame([[5, 15, 25], [35, 45, 55]])
print("Sum:\n", a + b)  # a + b
print("Sum:\n", a + c)  # a + b
print("Sum:\n", a.add(b))  # a + b
print("Sum:\n", a.radd(b), '\n')  # b + a
print("Difference:\n", a - b)  # a - b
print("Difference:\n", a - c)  # a - b
print("Difference:\n", a.sub(b))  # a - b
print("Difference:\n", a.rsub(b), '\n')  # b - a
print("Multiplication:\n", a * b)  # a * b
print("Multiplication:\n", a * c)  # a * b
print("Multiplication:\n", a.mul(b))  # a * b
print("Multiplication:\n", a.rmul(b), '\n')  # b * a
print("Division:\n", a / b)  # a / b
print("Division:\n", a / c)  # a / b
print("Division:\n", a.div(b))  # a / b
print("Division:\n", a.rdiv(b))  # b / a

# Prepared by RITURAJ RAMAN
# Note: Only Common built-in functions have been used in above program.
# Run the program for more clarity
