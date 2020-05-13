# Easy pandas
Sugary stuff for the pandas Python library

```python
import easy_pandas as pd
````

```
from sklearn import datasets
iris = datasets.load_boston()
```



## Value counts with both count and share of each proportion
```python
pd.value_counts(normalize="both")
```
|      |   N_obs |     Share |
|-----:|--------:|----------:|
|  0   |     372 | 0.735178  |
| 20   |      21 | 0.041502  |
| 80   |      15 | 0.0296443 |
| 12.5 |      10 | 0.0197628 |
| 22   |      10 | 0.0197628 |


## Human readable size

```
df.size(human_readable=True)
>>> 2.3 Gb
```

### Simple pivot

```
df = pd.DataFrame({"Age": np.random.choice(list(range(50,100)), size = 100), "Happy": np.random.choice([True, False], size = 100)})

pd.crosstab(df.Age, df.Happy, normalize = True)

```

|      |Happy|    |
|-----:|--------:|----------:|
|   Age|   True  |     False |
|  55  |     50  |      20   |
| 56   |      10 |30         |
| 57   |      28 | 52        |



### Explicit Na

```python
>>> pd.Series([1,1,2,np.nan, 2]).value_counts()
2.0    2
1.0    2

pd.options.explicit_Na = True

>>> pd.Series([1,1,2,np.nan, 2]).value_counts()
2.0    2
1.0    2
NaN    1
dtype: int64



```

### Merge info
```
>>> pd.merge(df_1,df_2, on = "zipcode")
(4,7)(7,8)(5,9)


>>> pd.merge(df_1,df_2, on = "zipcode", merge_report = "Full")
df_1.shape == (4,7) Lmerge with df_2.shape == (7,8) resulted in a merge of shape
(a,b)
```


# Dytypes
Dtypes in pandas can be tricky

### Astype protection
Check if the new type assigned with `astype` is compatible with current values of the array.


- Current behaviour
```
>>> df_12 = pd.DataFrame({"A":list(range(10))+[10**6]})
>>> print(df_12.A.values)
array([    0,     1,     2,     3,     4, 10000])
>>> df_12.A.astype("int8")
0     0
1     1
2     2
3     3
4     4
5    16
Name: A, dtype: int8
```
- Implemented Behaviour
```
>>> df_12.A.astype("int8")
AssertionError "int8" is a too small dtype

>>> df_12.A.astype("int8", error = "")


```

#### assert merges if not the same dtypes
Already implemented

```
>>> df_1 = pd.DataFrame({"zipcode": [31859,32568,47852]})
>>> df_2 = pd.DataFrame({"zipcode": ["31859","32568","47852"]})
>>> pd.merge(df_1,df_2, on = "zipcode")
```

ValueError: You are trying to merge on int64 and object columns. If you wish to proceed you should use pd.concat







### Immutable dtype per column

Create a dictionnary that associate a unique dtype to each column.

To change type of a column use
`df.A.coltype("str")` deleate the `astype` method execpt if the option is `pd.easy_pandas.dtypes.astrype_compatibility = [True, coltype, none]` .

```python
>>> df_12 = pd.DataFrame({"A":range(10)})
assert(df_12.applymap(type).A.nunique()==1)

>>>df_12.iloc[3] = "coucou"

AssertionError: Operation that would induce a mixed Dtype. Please change Dtype of the column to "mixed", "list", "dict", or "string".

```