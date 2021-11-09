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
|      |   N_obs |     Share |  Cumulate |
|-----:|--------:|----------:|----------:|
|  0   |     372 | 0.735178  |  0.735178 |
| 20   |      21 | 0.041502  |  0.776xxx |
| 80   |      15 | 0.0296443 |  0.79     |
| 12.5 |      10 | 0.0197628 |  0.81     |
| 22   |      10 | 0.0197628 |  0.83     |


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
### Add a na line after the Count line in df.describe()


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


check if works also with mixed dtypes ( [context here](If not implemented check https://towardsdatascience.com/data-cleaning-with-pandas-avoid-this-mistake-7af559657c2c) )



#### Info option for drop_duplicates
>>> df.drop_duplicates(subset=["date", "id"], info=True)
loggging INFO: 106 duplicates dropped, representing 1% of the rows.

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

### Logger for pipe function
display the input ou output shape (or informations) of a df in a `pipe` function. 

>>> df = df.pipe(dropna).pipe(remove_outliers).pipe(drop_duplicated_columns)
dropna: removed 40 rows. (123459,12) --> (12319, 12)
remove_outliers: removed 12 rows. (12319, 12) --> (12317, 12)
drop_duplicated_columns: removed 2 columns. (12317, 12) --> (12317, 10)

### Check pipe function
Xamine the shape of a df in and out and assert if not good. 


>>> df = df.pipex(dropna, max_row_loss=.1, n_cols=12)
dropna: removed 40 rows. (123459,12) --> (12319, 12)


remove_outliers: removed 12 rows. (12319, 12) --> (12317, 12)
drop_duplicated_columns: removed 2 columns. (12317, 12) --> (12317, 10)



shape = (123_000, 133)  shape to match exactly in output
max_row_loss            max percentage of rows lost in the process (option with relative or absolute to deal ( e.g if a tupple is provided for max_row_loss


#### Include index in the query namespace
index_to_keep = df[filter].index
df.query("index in @index_to_keep")

#### Feather automatic reset_index

```def to_feather_auto(df, path): 
     df.reset_index().to_feather(path) ### write additional func if the index column already exists (e.g. index_save_feather)
   return df
pd.to_feather = to_feather_auto  ## or modify such that the to_feather is modified everywhere
```

```def read_feather(df, path): 
     return pd.read_feather().set_index('index')     
```
#### Selection of the options
We could have a dictionary that set all features. 
e.g.
```
{explicit_na : True,
sugar_value_counts : True,
human_readable_size : True
}
```
It might be interesting to have a distinction between options that do not change pandas behavior (e.g. df.size(human_readable=True) does not change behavior if not used).

#### Allows .map({dict}) to keep values in Series that are not in the dictionary (as keys)
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html

https://stackoverflow.com/questions/44159495/missing-data-using-pandas-map

We can use replace instead.


#### Other related project:

pyjanitor : https://pyjanitor-devs.github.io/pyjanitor/
datatest : https://github.com/shawnbrown/datatest/
great_expectations : https://greatexpectations.io/






