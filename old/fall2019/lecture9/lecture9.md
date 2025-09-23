# Lecture 9

- Contents
  - NumPy - `Numerical Python` or `Numeric Python`
  - Pandas - 

## NumPy
### Description
- Ref: https://docs.scipy.org/doc/numpy/user/whatisnumpy.html
- Ref: https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf
- NumPy provides a multidimensional array object. 
- Each object comes with an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.
- Basically, you can use NumPy to create ndarray (N-dimensional array) and easily manipulate the array. It is super fast because it is written in C. 
### How is it different from Python arrays?
- Python lists can be modified -- you can add and remove elements. NumPy arrays have a fixed size at creation. 
- Python lists can contain different data types. NumPy arrays can only have one data type. 
- NumPy arrays come prepackaged with advanced mathematical operations. THe operations are super fast even on large numbers of data. 
### Why use NumPy
- Most data analysis programs use NumPy to manipulate data. They might take in data as standard Python lists, but they convert it to a NumPy array and manipulate the data using NumPy routines and output the transformed data as a NumPy array. 
- NumPy data array is the main data type used in most scientific and mathematical Python-based packages.
### Simple example

```python
# Square a list using Python
squared_values = []
for number in range(10):
    squared_values.append(number*numbers)

print(squared_values)

# Square a list using NumPy
import numpy as np

vector = np.array(range(10))
scalar = 5
print(vector * scalar)
print(vector * vector)

```


### Numpy Basics
- NumPy arrays can be a 1-D array, called a vector, or a 2-D array, called a matrix 

#### NumPy casting -- covert Python list to a NumPy array
```Python
my_list = [1, 2, 3]
print(my_list)

import numpy as np

my_vector = np.array(my_list)
print(my_vector)

my_matrix = np.array([my_list, my_list])
np.hstack([my_list, my_list])

my_nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_matrix = np.array(my_nested_list)
print(my_matrix)

my_list1 = [[1,2], [3,4]]
my_list2 = [[5,6], [7,8]]  
np.hstack([my_list1, my_list2])   
np.vstack([my_list1, my_list2])

```

#### NumPy creating arrays

```Python
my_list = range(10)

## Create array using arange
np.arange(10)
np.arange(0, 10)
np.arange(0, 10, 2)

## Create array of zeros
np.zeros(3)
np.zeros((3,3))

## Create array of ones
np.ones(3)
np.ones((3,3))
np.ones(3)*4

## Create evenly spaced vector
### Example use case: when you have Y values for a plot but need to generate X values
### *** Includes both start an end 
# np.arange(start, end(not included), step size)
# np.linspace(start, end(included), number_of_points)
np.linspace(0, 10, 5)
np.linspace(1900, 2000, 11)
```

## Create an identify matrix 
```Python
np.eye(3)
```

## Creating an empty array
```python
np.empty((2,3))
```

## Creating Random Numbers
- Ref: https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.random.html

```python
# Uniform distribution 
np.random.rand(3)
np.random.rand(3,3)
# Normal distribution
np.random.randn(3)
np.random.randn(3,3)
# Random integers
# np.random.randint(start, end(not_included), size)
np.random.randint(1,101)
np.random.randint(1,101,5)  
```

## Reshaping arrays

```python

vector = np.arange(1,10)
print(vector.reshape(3,3))

vector = np.arange(1,13)
print(vector.reshape(3,4))
```

## Basic array operations
```python
vector = np.random.randint(1,50,25)
# Min
vector.min()
# Max
vector.max()
# get location of min value
index = vector.argmin()
# get location of max value
index = vector.argmax()
# get shape
vector.shape

my_matrix = vector.reshape(5, 5)
my_matrix.shape
```

## Indexing a 1-D array -- vector
```python
vector = np.array(range(10))
# vector[index]
# vector [start:end]
# vector [:end]
# vector [start:]
# vector [start, end, step]

vector[3]
vector[3:8]
vector[:5]
vector[5:]
vector[3:9:2]
vector[-1]
```

## Setting multiple values at once -- Broadcasting
- There are two main features of NumPy arrays
  - Vectorization -- no need for explicit looping -- example, vector multiplication or squaring
  - Broadcasting -- set multiple values at once

```python
vector[3:6] = 12
```

## BE CAREFUL
- If you store a slice of an array in a new variable, changes in the new variable will be reflected in the original array. 

```python
vector = np.array(range(10))
my_slice = vector[3:7]
my_slice[:] = 20
print(vector)
```

- Copy the array if you need a copy
vector = np.array(range(10))
my_slice_copy = vector[3:7].copy()
print(vector)

## Indexing a 2-D array -- Matrix
- Remember -- Python is zero-indexed
```python
matrix = np.array(range(1,10)).reshape((3,3))
matrix[0,0]
matrix[0][0] 
matrix[2,2]  
matrix[2][2] 


matrix[:,2] # Grab the third column
matrix[1,:] # Grab the second row
matrix[:2] # grab the first two rows, all columns
matrix[:2,:] # grab the first two rows, all columns
matrix[:,1:] # grab all the rows, but columns starting from 1
```

## Conditional selection

```python
vector = np.arange(10)
gt2 = vector > 2 # create condition
lt8 = vector < 8 # create condition

selected_gt2 = vector[gt2] # apply condition to select
selected_lt8 = vector[lt8] # apply condition to select

vector[vector>2]
vector[vector<8]

cond = (vector>2) & (vector<7)
vector[cond]

cond = (vector>=2) & (vector<=7)
vector[cond]
```

## Array operations -- Basic

```python
vector = np.arange(10)

vector + vector
vector - vector
vector * vector
vector / vector # problem!!! return `nan` 
vector + 10
vector - 10
vector * 10
vector / 10
```

## Array operations -- Advanced
- Ref: https://docs.scipy.org/doc/numpy/reference/ufuncs.html#math-operations
```python
vector = np.arange(10)
np.max(vector)
np.min(vector)
np.sqrt(vector)
np.log(vector)

sum(vector<5)
import math
vector = np.arange(1,11) * math.pi 
np.sin(vector)
vector = np.arange(0,math.pi+math.pi/4,math.pi/4)
np.sin(vector)

matrix = np.random.rand(5,5)
np.floor(matrix*1000)/1000
np.round(matrix*1000)/1000
np.floor(matrix*1000)/1000

matrix = np.arange(1,10).reshape(3,3)
matrix.sum(axis=1) 
matrix.sum(axis=0) 
matrix.cumsum() 
matrix.cumprod() 

matrix.min(axis=1) 
matrix.min(axis=0) 

matrix.max(axis=1) 
matrix.max(axis=0) 

matrix = np.array([1,2,3]*3).reshape(3,3)
np.unique(matrix.reshape(3,3))
```




## Pandas
- Built-on top of NumPy -- meaning the underlying data structure used is ndarray
- Pandas provides series which are like NumPy arrays but with associated index labels -- meaning are like column  labels or row labels. Element data type can be different
- Pandas also provides dataframes which are like Excel sheets or database tables


### Basic examples

```python
import numpy as np
import pandas as pd

header = ['chrom', 'pos', 'filter']
data = [4, 12345, 38.4]

vector = np.array(data)
data_dict = {'chrom': 4, 'pos': 12345, 'filter': 38.4}

s1 = pd.Series(data=data) # Notice the data type is float
s2 = pd.Series(data=data, index=header)

# can also do 
s1 = pd.Series(data)
s2 = pd.Series(data, header)

# can hold different data types

data = [1, '2s', 34] 
pd.Series(data)

# can use a dictionary to initialize a panda series
pd.Series(data_dict)

## Using index labels to fetch element
header = ['chrom', 'pos', 'filter']
data = [4, 12345, 38.4]
series = pd.Series(data=data, index=header)
series['chrom']
series['filter']

series = pd.Series(data)
series[0]


## Basic operations
header1 = ['chrom', 'pos', 'filter']
data1 = [4, 12345, 38.4]
header2 = ['chrom', 'pos', 'filter', 'qual']
data2 = [3, 4899, 234, 89.9]

s1 = pd.Series(data1, header1)
s2 = pd.Series(data2, header2)
s1+s2 

header1 = ['chrom', 'pos', 'filter']
data1 = [4, 12345, 38.4]
header2 = ['chrom', 'pos', 'filter', 'qual']
data2 = ['3', 4899, 234, 89.9]

s1 = pd.Series(data1, header1)
s2 = pd.Series(data2, header2)
s1+s2 

data1 = [4, 12345, 38.4]
data2 = [3, 4899, 234, 89.9]

s1 = pd.Series(data1)
s2 = pd.Series(data2)


## IMPORTANT - with index labels -- operations are based on label
header1 = ['pos', 'filter', 'chrom']
data1 = [12345, 38.4, 4]
header2 = ['chrom', 'pos', 'filter', 'qual']
data2 = [3, 4899, 234, 89.9]

s1 = pd.Series(data1, header1)
s2 = pd.Series(data2, header2)
s1+s2 


data1 = [12345, 38.4, 4]
data2 = [3, 4899, 234, 89.9]

s1 = pd.Series(data1)
s2 = pd.Series(data2)
```

## Dataframes -- 
- Dataframe is composed of series

```python
import numpy as np
import pandas as pd

header = ['exam1', 'exam2', 'exam3']
data = np.random.randint(65, 101, 12).reshape(4,3)
students = ['student1', 'student2', 'student3', 'student4']

df = pd.DataFrame(data=data, columns=header)

df = pd.DataFrame(data=data, index=students, columns=header)
df['exam1']
df.exam1 # not a good way to do this


df['average'] = (df['exam1'] + df['exam2'] + df['exam3'])/3 
df.drop('average') # does not work because default for drop is to work on row labels
df.drop('average', axis=1) # works on column labels 

## STILL NOT DROPPED from df
df
df.drop('average', axis=1, inplace=True)

## drop a student
df.drop('student3')

header = ['exam1', 'exam2', 'exam3']
data = np.random.randint(65, 101, 12).reshape(4,3)
students = ['student1', 'student2', 'student3', 'student3']
df = pd.DataFrame(data=data, index=students, columns=header)

df.drop('student3')
df.drop('student3', inplace=True)
## Row is referred to as axis=0
## Column is referred to as axis=1
## (R,C) == (axis=0, axis=1) df.shape
```

## Select Dataframe rows
```python
header = ['exam1', 'exam2', 'exam3']
data = np.random.randint(65, 101, 12).reshape(4,3)
students = ['student1', 'student2', 'student3', 'student4']
df = pd.DataFrame(data=data, index=students, columns=header)

df.loc['student1']
df.iloc[0] ## remember that column names do not count as rows
```

## Select subset of data
```python
header = ['exam1', 'exam2', 'exam3']
data = np.random.randint(65, 101, 12).reshape(4,3)
students = ['student1', 'student2', 'student3', 'student4']
df = pd.DataFrame(data=data, index=students, columns=header)

df.loc['student1', 'exam1']
df.loc[['student1', 'student3'], ['exam1', 'exam3']]
```

## Use conditions to select
```python
header = ['exam1', 'exam2', 'exam3']
data = np.random.randint(65, 101, 12).reshape(4,3)
students = ['student1', 'student2', 'student3', 'student4']
df = pd.DataFrame(data=data, index=students, columns=header)

df>=90
df[df>=90]
df['exam1']>=85 #   
df[df['exam1']>=85] # gives all columns where exam1 is greater than 85
df[df['exam1']>=85]['exam3'] 
df[df['exam1']>=85][['exam2', 'exam3']] 


df[(df['exam1']>=85) & (df['exam2']>=85)]
df[(df['exam1']>=85) & (df['exam2']>=85)]['exam3']

df[(df['exam1']>=85) | (df['exam2']>=85)]
df[(df['exam1']>=85) | (df['exam2']>=85)]['exam3']
```


## Adding student index
```python
header = ['exam1', 'exam2', 'exam3']
data = np.random.randint(65, 101, 12).reshape(4,3)
students = ['student1', 'student2', 'student3', 'student4']
df = pd.DataFrame(data=data, columns=header)
df['name'] = students

df.set_index('name', inplace=True)
df.loc['student1']
df.reset_index(inplace=True)
```

## Multi-index data
```python
students = 'student1 student1 student1 student2 student2 student2 student3 student3 student3'
exams = 'exam1 exam2 exam3'.split()*3
classes = 'class1 class2'
index = list(zip(students.split(), exams))
index = pd.MultiIndex.from_tuples(index)
df = pd.DataFrame(np.random.randint(65, 101, 3*3*2).reshape(9,2) , index, classes.split())
df.loc['student1'].loc['exam1']['class1'] 
df.index.names
df.index.names = ['Students', 'Exams']

## cross-section
df.xs('student1')
df.xs('exam1', level='Exams')
```


## Dealing with missing data
```python
my_dict = {'student1': [90, 84, np.nan], 'student2': [77, np.nan, np.nan], 'student3': [88, 65, 93]}
df = pd.DataFrame(my_dict)
df.dropna()
df.dropna(axis=0)
df.dropna(axis=1)

df.dropna(thresh=2)
df.fillna(value=55)

df.drop(axis=0, labels=[1,2]) 
df.drop(axis=1, columns=['student1']) 
```


## Groupby
```python
my_dict = {
    'Exams': 'exam1 exam1 exam1'.split() + 'exam2 exam2 exam2'.split() + 'exam3 exam3 exam3'.split(),
    'Students': 'student1 student2 student3'.split()*3,   
    'Scores': np.random.randint(65,101,9)
}
df = pd.DataFrame(my_dict)
df.groupby('Students').mean()
df.groupby('Students').mean().loc['student1']
df.groupby('Exams').max()['Scores']
df.groupby('Exams').describe() 
df.groupby('Students').describe().transpose() 
```

## Merging  -- SQL JOIN
```python
departments = { 
    'DepartmentId': [1, 2, 3, 4],
    'DepartmentName': ['IT', 'Physics', 'Arts', 'Math'] 
}

df1 = pd.DataFrame(departments)

students = {
    'StudentId': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'StudentName': ['Michael', 'John', 'Jack', 'Sara', 'Sally', 'Jena', 'Nancy', 'Adam', 'Stevens', 'George'],
    'DepartmentId': [1, 1, 1, 2, 2, np.nan, 2, 3, 3, np.nan]
}

df2 = pd.DataFrame(students)

marks = {
    'MarkId': [1, 2, 3, 4, 5, 6, 7, 8],
    'StudentId': [1, 2, 3, 4, 5, 6, 7, 8], 
    'Mark': [18, 20, 16, 19, 14, 20, 20, 20]
}

df3 = pd.DataFrame(marks)

pd.merge(df2, df1, how='inner', on='DepartmentId')
pd.merge(df1, df2, how='inner', on='DepartmentId')
pd.merge(df1, df2, how='outer', on='DepartmentId')
pd.merge(df2, df1, how='right', on='DepartmentId') 

pd.merge(df3, pd.merge(df2, df1, how='inner', on='DepartmentId'), how='inner', on='StudentId')
data = pd.merge(df3, pd.merge(df2, df1, how='inner', on='DepartmentId'), how='inner', on='StudentId')

data[['StudentName', 'Mark', 'DepartmentName']] 

```
- ref: https://stackoverflow.com/a/48411543

## Concatenation
```python
d1 = {
    'C0': ['COR0', 'COR1', 'COR2'],
    'C1': ['C1R0', 'C1R1', 'C2R2'],
    'C2': ['C2R0', 'C2R1', 'C2R2'],
}

df1 = pd.DataFrame(d1)

d2 = {
    'C0': ['C0R3', 'C0R4', 'C0R5'],
    'C1': ['C1R3', 'C1R4', 'C1R5'],
    'C2': ['C2R3', 'C2R4', 'C2R5'],
}

df2 = pd.DataFrame(d2)

d3 = {
    'C0': ['C0R6', 'C0R7', 'C0R8'],
    'C1': ['C1R6', 'C1R7', 'C1R8'],
    'C2': ['C2R6', 'C2R7', 'C2R8'],
}

df3 = pd.DataFrame(d3)

pd.concat([df1, df2, df3])

## Concatenation -- Fix index

d1 = {
    'C0': ['COR0', 'COR1', 'COR2'],
    'C1': ['C1R0', 'C1R1', 'C2R2'],
    'C2': ['C2R0', 'C2R1', 'C2R2'],
}

df1 = pd.DataFrame(d1, index=[1, 2, 3])

d2 = {
    'C0': ['C0R3', 'C0R4', 'C0R5'],
    'C1': ['C1R3', 'C1R4', 'C1R5'],
    'C2': ['C2R3', 'C2R4', 'C2R5'],
}

df2 = pd.DataFrame(d2, index=[4, 5, 6])

d3 = {
    'C0': ['C0R6', 'C0R7', 'C0R8'],
    'C1': ['C1R6', 'C1R7', 'C1R8'],
    'C2': ['C2R6', 'C2R7', 'C2R8'],
}

df3 = pd.DataFrame(d3, index=[7, 8, 9])

pd.concat([df1, df2, df3])
```


## More Pandas Operations
```python
data['DepartmentName'].unique() 
data['DepartmentName'].nunique() 
data['DepartmentName'].value_counts()
data[data['Mark']>17]  
```

## Lambda with Pandas
- Scale marks by 5 
```python

def times5(val):
    return val * 5

data['Mark'].apply(times5)

data['Mark'].apply(lambda val: val*5)

```
- Upper all department names

```python
def upper(string):
    return string.upper()

data['DepartmentName'].apply(upper)

data['DepartmentName'].apply(lambda string: string.upper())
```
```python

mapping = {18: 'B', 14: 'C', 19: 'A-', 20: 'A+'}
df3['Mark'].map(mapping)     


```


## Dropping columns
```Python
data.columns
data.drop(['StudentId', 'MarkId' , 'DepartmentId'], axis=1)
```

## Sorting 
```Python
data.sort_values('Mark')
data.sort_values('Mark', ascending=False)
```


## Importing CSV, TSV
```python

data = pd.read_csv('students.tsv', sep='\t', names=['lastname', 'firstname', 'username', 'exam1', 'exam2', 'exam3']) 

data.sort_values('exam1', ascending=False) 

data[['exam1', 'exam2', 'exam3']].mean() 
data['average']= np.mean(data[['exam1', 'exam2', 'exam3']], axis=1) 
data.sort_values('average', ascending=False) 

data.to_csv('output.tsv', sep='\t', index=False, header=False)
```

## Other methods
```python
data.head()
data.head(2)

data.tail
data.tail(3)

data.shape
data.iloc[3] 
data.columns 
data.dtypes 
data.info()  
data.get_dtype_counts() 
data.describe()  
```

## More data manipulation
```python
data[data['exam1'].between(75, 85)] 
data[data['exam1'].in([75, 85, 95])
data[data['exam1'].isin([75, 85, 95])]  
data['exam1'].unique() 
data['exam1'].nunique()
np.sort(data['exam1'].unique())
```

## More examples
```
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv")
```