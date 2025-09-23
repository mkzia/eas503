# Week 12 Pandas continued and Plotting

## Agenda
- Pandas
- Matplotlib
- Seaborn
- Plotly



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

## Example5 in pandas

## More examples
```
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv")