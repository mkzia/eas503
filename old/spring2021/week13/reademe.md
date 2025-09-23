# Week 13 Pandas and Machine Learning

## Topics
- Pandas
- Machine Learning with Python 


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
    'C0': ['C0R0', 'C0R1', 'C0R2'],
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

## Lambdas with Pandas
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

## Example5 in pandas

## More examples

```
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv")
```

Ref: https://www.kaggle.com/syedmubarak/pandas-75-exercises-with-solutions


## General Machine Learning Concept
- Simplified: in machine learning, a computer is trained to classify new data. Think of it as an input-output device that takes in a number of inputs, and based on the pattern of these inputs, determine the most likely class associated with that data. There two main types of learning strategies. 1) Supervised learning where you train the machine using data for which the correct class is known. 2) Unsupervised learning where the classifier itself tries to find patterns within the input data itself. (Biosignal and Medical Image Processing John Semmlow) 
- Classification vs Regression (prediction) 

## General Outline of Machine Learning

1. Loading Data
  - Load toy data included in sklearn
  - Download published/annotated data from online
  - Generate data with specific statistics to learn how algorithms work
2. Preprocessing Data
  - Make data zero mean
  - Make data unit variance
  - Fix range of values
  - Deal with missing values
  - Map text labels to integer labels (if applicable)
3. Dimensionality Reduction of data
  - If you use too many features and do not have enough samples, you could over fit.
  - So you have to choose the most discriminating few features
4. Applying algorithms
  - Labeled Data - Supervised 
  - Non-labeled Data - Unsupervised 
5. Evaluation 
  - Receiver Operator Curve
    - Sensitivity
    - Specificity
  - Imbalanced Data
    - Example: 95 % one class, 5% another class

- REF: Scikit-learn Essentials: Mastering the scikit-learn Machine Learning Library for Python by Dhiraj Kumar

## Various Python Libraries: When to use what
  - ref:https://www.quora.com/What-is-the-relationship-among-NumPy-SciPy-Pandas-and-Scikit-learn-and-when-should-I-use-each-one-of-them
  - Numpy -- provides efficient array computation via vectorization and broadcasting
      - Vectorization -- no need for explicit looping -- example, vector multiplication or squaring
      - Broadcasting -- manipulate multiple values at once
  - Pandas - Uses Numpy arrays as the underlying structure. Good for analyzing tabular data
  - Scipy (scientific python)- provides libraries for scientific computing, including: integration, interpolation, signal processing, linear algebra, statistics. Also uses Numpy infrastructure
  - Scikit-learn - provides a collection of machine-learning algorithms that use Numy and Scipy 
    - Most used Python library for machine-learning
      - regression
      - classification
      - clustering

## Topics Covered
  - Introduction to Scikit-learn
  - Loading Dataset using Scikit-learn
  - Preprocessing data using scikit-learn
  - Train Test split using scikit-learn
  - Linear regression using scikit-learn
  - Naive Bays using Scikit learn
  - SVM using Scikit learn
  - k-Nearest neighbor using Scikit-learn

## Introduction to Scikit-learn 
  - Choose the right estimator -- the right algorithm for doing ML
    - https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html
  - Consistent -- all object share a common interface
  - Inspection -- all parameter values are exposed as public attributes
  - Limited object Hierarchy -- algorithms are represented as Python classes, datasets mainly as numpy array and parameters as standard python strings 
  - Composition -- ML as a sequences of fundamental algorithms
  - Defaults -- provides good default values

### High Level Steps
  - Choose the class of model to be coded
  - Choose the hyper parameters of the model
  - Arrange data into target and features
  - Write model fitment code using fit() method. 

### General Steps
  - Load Data
    - Three ways load data
      - Dataset loaders (toy datasets that come with skikit-learn)
        - Good for illustrating how the various algorithms work
      - Dataset fetchers (real world datasets)
        - Built-in functions to load large datasets
        - Pull from openml.org
      - Dataset generation functions
        - Artificial datasets -- can create labeled datasets
        - 
  - Pre-process Data
    - Remove mean **
    - Scale Variance **
    - Non-linear transformation
    - Normalization
    - Encoding categorical features
    - Discretization
    - Imputation of missing values 
    - Maybe remove outliers if it can be justified. Always document this in research paper

### Loading data

### Preprocessing
#### Mean and Variance
- algorithms require that all the features have variance of similar magnitude. If the magnitude differ by orders of magnitude larger than others, it might dominate the objective function.
  - Whatever mean or std you subtract from the training set, you have to use the same on the testing set. 
- Algorithms assume that the input data is Gaussian distribution with zero mean and unit variance. 
- Power transformers aim to map data from any distribution to as close to a Gaussian distribution 

#### Encoding
- Map text values to integer codes. Instead of using text for city names, use integers. Or Male = 0, Female = 1. 

#### Discretization 
- Turn continuous values in to discrete values. You bin the continuous into bins. *** Linear models can become non-linear due to discretization 


#### Imputation 
- Many real world datasets contain missing values; 
  - Discard entire rows
  - Or fill data -- usually by guessing from available data


### Splitting Data
- It is common to split data into training and testing samples. 
- Usually you do 90/10 or 80/20. 
- The splitting has to be random
- K-Cross-fold validation -- split data K times

### Linear Regression
- LR models the relationship between a dependent variable and one or more independent variable. When one increase or decrease, the other increases or decreases. 

### Naive Bayes
- Simple supervised machine learning classifier
- Assumes the features are independent 
  - Example -- apple is red, round and 4 cm in diameter 


### Support Vector Machine (SVM)
- Another supervised machine learning classifier
  - use for both classification and regression 
- Can do non-linear classification
- Hyper plane -- maximize the margin between two classes
- Support Vectors -- data points that define the hyper plane 
- Margin width -- define an optimal hyper plane we need to maximize the width
of the margin 

