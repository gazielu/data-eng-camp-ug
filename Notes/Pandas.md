# Data Munging CheatSheet

## Definition
- **Series** is a one dim array
- **Dataframe** is a two dimension array

## Reading CSV
```py
df = pd.read_csv(address, index_col='Order Date', parse_dates=True)
```
## Filter and Select
### Arange
Create a random array
```python
np.arange(numberofelement), index=['row name']
```
### Create a random Dataframe

```python
DF_obj = DataFrame(np.random.rand(36).reshape((6,6)), 
                   index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6'],
                   columns=['column 1', 'column 2', 'column 3', 'column 4', 'column 5', 'column 6'])
```

### Indexer, retrieve specific rows, columns

```python
# object_name.ix[[row indexes], [column indexes]]
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# When you call the .ix[] special indexer, and pass in a set of row and colum indexes, this tells 
# Python to select and retrieve only those specific rows and columns.
DF_obj.ix[['row 2', 'row 5'], ['column 5', 'column 2']]
```

```py
cars_df = pd.DataFrame((cars.ix[:,(1,3,4,6)].values), columns = ['mpg', 'disp', 'hp', 'wt']) # create a new dataframe with manual data picking
    
cars_target = cars.ix[:,9].values
```

### Data slicing, receive all the records of row/column

```python
# ['starting label-index':'ending label-index'] 
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# Data slicing allows you to select and retrieve all records from the starting label-index, to the 
# ending label-index, and every record in between.
series_obj['row 3':'row 7']
```

### Compare with scalar

```python
# object_name < scalar value
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# You can use comparison operators (like greater than or less than) to return True / False values for 
# all records, to indicate how each element compares to a scalar value. 
DF_obj < .2
```

### Filter with scalar

```python
# object_name[object_name > scalar value] 
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# You can also use comparison operators and scalar values for indexing, to return only the records 
# that satisfy the comparison expression you write.
series_obj[series_obj > 6]
```

### Setting Values with Scalar

```python
# ['label-index', 'label-index', 'label-index'] = scalar value
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# Setting is where you select all records associated with the specified label-indexes and set those 
# values equal to a scalar.
series_obj['row 1', 'row 5', 'row 8'] = 8
```
## Treating Missing Values

### Is Null ?

```python
# object_name.isnull()
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# The .isnull() method returns a Boolean value that describes (True or False) whether an element in a 
# Pandas object is a null value.
series_obj.isnull()
```

### Filling in for missing values

1. Filling in nan with single values
    ```py
    # object_name.fillna(numeric value)
    # ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
    # The .fillna method() finds each missing value from within a Pandas object and fills it with the 
    # numeric value that you've passed in.
    filled_DF = DF_obj.fillna(0)
    ```

2. Filling in with a dictionary
    ```py
    # object_name.fillna(dict)
    # ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
    # You can pass a dictionary into the .fillna() method. The method will then fill in missing values 
    # from each column Series (as designated by the dictionary key) with its own unique value 
    # (as specified in the corresponding dictionary value).
    filled_DF = DF_obj.fillna({0: 0.1, 5: 1.25})
    ```

3. Filling in with last non-null element
    ```py
    # ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
    # You can also pass in the method='ffill' arguement, and the .fillna() method will fill-forward any 
    # missing values with values from the last non-null element in the column Series.
    fill_DF = DF_obj.fillna(method='ffill')
    ```
### Counting missing values

```py
# object_name.isnull().sum()
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# To generate a count of how many missing values a DataFrame has per column, just call the .isnull() 
# method off of the object, and then call the .sum() method off of the matrix of Boolean values it 
# returns.
DF_obj.isnull().sum()
```

### Filtering out missing values

```py
# object_name.dropna(how='all')
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# To identify and drop only the rows from a DataFrame that contain ALL missing values, simply 
# call the .dropna() method off of the DataFrame object, and pass in the how='all' argument.
DF_obj.dropna(how='all')
```

## Remove duplicates

### Is duplicated ?

```py
# object_name.duplicated()
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# The .duplicated() method searches each row in the DataFrame, and returns a True or False value to 
#indicate whether it is a duplicate of another row found earlier in the DataFrame.
DF_obj.duplicated()
```

### Drop duplicates

1. Drop whole dataset
    ```py
    # object_name.duplicated()
    # ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
    # The .duplicated() method searches each row in the DataFrame, and returns a True or False value to 
    #indicate whether it is a duplicate of another row found earlier in the DataFrame.
    DF_obj.duplicated()
    ```
2. Drop with columns
   
    ```py
    # object_name.drop_duplicates(['column_name'])
    # ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
    # To drop the rows that have duplicates in only one column Series, just call the drop_duplicates() 
    # method off of the DataFrame, and pass in the label-index of the column you want the de-duplication 
    # to be based on. This method will drops all rows that have duplicates in the column you specify.
    DF_obj.drop_duplicates(['column 3'])
    ```

## Concatenate and transforming

Appending by columns
```py
# pd.concat([left_object, right_object], axis=1)
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# The concat() method joins data from seperate sources into one combined data table. If you want to 
# join objects based on their row index values, just call the pd.concat() method on the objects you 
# want joined, and then pass in the axis=1 argument. The axis=1 argument tells Python to concatenate 
# the DataFrames by adding columns (in other words, joining on the row index values).
pd.concat([DF_obj, DF_obj_2], axis =1)
```
Appending by rows, missing data treated as `NaN`

`pd.concat([DF_obj, DF_obj_2])`

### Drop data

Drop a row
```py
# object_name.drop([row indexes])
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# You can easily drop rows from a DataFrame by calling the .drop() method and passing in the index 
# values for the rows you want dropped.
DF_obj.drop([0,2])
```

Drop a column

```py
DF_obj.drop([0,2], axis=1)
```

### Adding a data
1. Join()
    ```py
    # DataFrame.join(left_object, right_object)
    # ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
    # You can use .join() method two join two data sources into one. The .join() method works by joining 
    # the two sources on their row index values.
    variable_added = DataFrame.join(DF_obj, series_obj)
    variable_added
    ```

2. Append()
    ```py
    added_datatable = variable_added.append(variable_added, ignore_index=True)
    ```
### Sorting data

```py
# object_name.sort_values(by=[index value], ascending=[False])
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# To sort rows in a DataFrame, either in ascending or descending order, call the .sort_values() 
# method off of the DataFrame, and pass in the by argument to specify the column index upon which 
# the DataFrame should be sorted.
DF_sorted = DF_obj.sort_values(by=[5], ascending=[False])
```

## Group and Aggregate 

```py
# object_name.groupby('Series_name')
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# To group a  DataFrame by its values in a particular column, call the .groupby() method off of the DataFrame, and then pass
# in the column Series you want the DataFrame to be grouped by.
cars_groups = cars.groupby(cars['cyl'])
cars_groups.mean()
```

## Data visualization

Imports
```py
import matplotlib.pyplot as plt
from matplotlib import rcParams
```

Settings
```py
%matplotlib inline
rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')
```

### Plotting a line chart in matplotlib

1. Simple line chart
    ```py
    x = range(1,10)
    y = [1,2,3,4,0,4,3,2,1]

    plt.plot(x, y)
    ```
2. Dataframe plotting (multiline)
    ```py
    df = cars[['cyl', 'wt', 'mpg']]
    df.plot()  
    ```
### Bar chart

```py
plt.bar(x, y)
```
From Pandas Object

```py
mpg.plot(kind='bar')
```

Horizontal 
```py
mpg.plot(kind='barh')
```

### Pie Chart

```py
x = [1,2,3,4,0.5]
plt.pie(x)
plt.show()
```

### Save a chart (export)

```py
plt.savefig('pie_chart.jpeg')
plt.show()
```

### Define axes, ticks, and grids

```py
x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]

fig = plt.figure()

ax = fig.add_axes([.1, .1, 1, 1]) # defin axes

ax.set_xlim([1,9]) # define axes limits
ax.set_ylim([0,5])

ax.set_xticks([0,1,2,4,5,6,8,9,10]) # manual axes ticking
ax.set_yticks([0,1,2,3,4,5])

ax.grid() # Add Grid

ax.plot(x,y)
```

### Multiple plots

[Ref: Figure()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figure.html)

```py
fig = plt.figure() # create a new figure
fig, (ax1, ax2) = plt.subplots(1,2)

ax1.plot(x)
ax2.plot(x,y)
```

### Bar Width

```py
wide = [0.5, 0.5, 0.5, 0.9, 0.9, 0.9, 0.5, 0.5, 0.5]
plt.bar(x, y, width=wide, align='center')
```

### Plot colors

    ```py
    wide = [0.5, 0.5, 0.5, 0.9, 0.9, 0.9, 0.5, 0.5, 0.5]
    color = ['salmon']
    plt.bar(x, y, width=wide, color=color, align='center')
    ```

Multiple coloring

    ```py
    color_theme = ['darkgray', 'lightsalmon', 'powderblue']
    df.plot(color=color_theme)
    ```

Pie chart coloring

    ```py
    color_theme = ['#A9A9A9', '#FFA07A', '#B0E0E6', '#FFE4C4', '#BDB76B']
    plt.pie(z, colors = color_theme)
    plt.show()
    ```

### Line Styles

```py
plt.plot(x, y, ls = 'steps', lw=5)
plt.plot(x1,y1, ls='--', lw=10)
```

### Marker

```py
plt.plot(x, y, marker = '1', mew=20)
plt.plot(x1,y1, marker = '+', mew=15)
```

### Labeling 

Bar chart

    ```py
    x = range(1,10)
    y = [1,2,3,4,0.5,4,3,2,1]
    plt.bar(x,y)

    plt.xlabel('your x-axis label')
    plt.ylabel('your y-axis label')
    ```

Pie chart

    ```py
    z = [1 , 2, 3, 4, 0.5]
    veh_type = ['bicycle', 'motorbike','car', 'van', 'stroller']
    plt.pie(z, labels= veh_type)
    plt.show()
    ```

### Set title

```py
ax.set_title('Miles per Gallon of Cars in mtcars')

```

### Labeling compilation

```py
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = cars.mpg

fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1])

mpg.plot()

ax.set_xticks(range(32))

ax.set_xticklabels(cars.car_names, rotation=60, fontsize='medium')
ax.set_title('Miles per Gallon of Cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')

```

### Annotate chart

```py
fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
mpg.plot()
ax.set_title('Miles per Gallon of Cars in mtcars')
ax.set_ylabel('miles/gal')

ax.set_ylim([0,45])

ax.annotate('Toyota Corolla', xy=(19,33.9), xytext = (21,35),
           arrowprops=dict(facecolor='black', shrink=0.05))
```

### Time Series Plot

```py
address = 'C:/Users/Lillian Pierson/Desktop/Exercise Files/Ch02/02_05/Superstore-Sales.csv'
df = pd.read_csv(address, index_col='Order Date', parse_dates=True)
```

Downsizing the sample

    ```py
    df2 = df.sample(n=100, random_state=25, axis=0)

    plt.xlabel('Order Date')
    plt.ylabel('Order Quantity')
    plt.title('Superstore Sales')

    df2['Order Quantity'].plot()
    ```

### Histograms, box plots, scatter plots

imports

```py
from pandas.tools.plotting import scatter_matrix

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb
```

1. Eyeballing dataset distribution with histogram

    ```py
    cars = pd.read_csv(address)
    cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
    cars.index = cars.car_names
    mpg = cars['mpg']

    mpg.plot(kind='hist')
    ```

    ```py
    sb.distplot(mpg)
    ```

2. Seeing scatter plot in action

    ```py
    cars.plot(kind='scatter', x='hp', y='mpg', c=['darkgray'], s=150)
    ```

    Regional plot

        ```py
        sb.regplot(x='hp', y='mpg', data=cars, scatter=True)
        ```

3. Generating a scatter plot matrix

    ```py
    sb.pairplot(cars)
    ```

    ```py
    cars_df = pd.DataFrame((cars.ix[:,(1,3,4,6)].values), columns = ['mpg', 'disp', 'hp', 'wt']) # create a new dataframe with manual data picking

    cars_target = cars.ix[:,9].values
    target_names = [0, 1]

    cars_df['group'] = pd.Series(cars_target, dtype="category")
    sb.pairplot(cars_df, hue='group', palette='hls')
    ```

4. [Building Box plot](http://www.physics.csbsju.edu/stats/box2.html)

    ```py
    cars.boxplot(column='mpg', by='am')
    cars.boxplot(column='wt', by='am')
    ```

    Adding pallete

        ```py
        sb.boxplot(x='am', y='mpg', data=cars, palette='hls')
        ```


# Working with Numpy and Scipy

```py
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats
```

# pandas and csv get schema
```py
df = pd.read_csv('file',nrows=50)
print(pd.io.sql.get_schema(df, name='yellow_texi_data')
pd.to_datetime(df.timestap)
```

settimg new 
df.xxx = pd.to_datetime(df.xxx)


## Math and Statistics

```python
cars.sum() # summarize each column

cars.sum(axis=1) #sumarize each row

cars.median() # get the mid value

cars.mean() # get the average

cars.max() 

mpg = cars.mpg
mpg.idxmax()

cars.std() # standard deviation

cars.var() # Variance

gear = cars.gear

gear.value_counts()

cars.describe()

# Describe with grouping
gears_group = cars_cat.groupby('gear')
gears_group.describe()
```

### Transforming variables to categorical data type

```py
# pd.Series(x_variable, dtype)
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# To create a Series of categorical data type, call the pd.Series() function on the array or Series that holds the data you
# want the new Series object to contain. When you pass in the dtype="category" argument, this tells Python to assign the new
# Series a data type of "category". Here we create a new categorical Series from the gear variable, and then assign it to a
# new column in the cars DataFrame, called 'group'.
cars['group'] = pd.Series(cars.gear, dtype="category")
cars['group'].dtypes
cars['group'].value_counts()
```

### Describing categorical data with crosstabs

```py
# pd.crosstab(y_variable, x_variable)
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# To create a cross-tab, just call the pd.crosstab() function on the variables you want included in 
# the output table.
pd.crosstab(cars['am'], cars['gear'])
```

## Correlation between variables

import

```py
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats.stats import pearsonr

```

### Parametric methods in Pandas and Scipy

#### The pearson correlation

> **Pearson Correlation Coefficient**
> - R = 1 -> Strong positive Relationship
> - R = 0 -> not linearly correlated
> - R = -1 -> Strong negative relationship

> **Assumptions**
> - Data is normally distributed
> - continuous, numeric variables
> - Variables are linearly related

> **Usage**
> - Uncover (linear) rela
> - Not to rule out possible (non-linear) relationships between variables

```py
sb.pairplot(cars)

X = cars[['mpg', 'hp', 'qsec','wt']]
sb.pairplot(X)
```
#### Using scipy to calculate the Pearson correlation coefficient

```py
mpg = cars['mpg']
hp = cars['hp']
qsec = cars['qsec']
wt = cars['wt']

pearsonr_coefficient, p_value = pearsonr(mpg, hp)
print 'PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient)

pearsonr_coefficient, p_value = pearsonr(mpg, qsec)
print 'PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient)


pearsonr_coefficient, p_value = pearsonr(mpg, wt)
print 'PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient)
```

#### Using pandas to calcuate Pearson correlation coefficient

```py
corr = X.corr()
corr
```

#### Using Seaborn to visualize the Pearson correlation coefficient

```py
sb.heatmap(corr,xticklabels=corr.columns.values, yticklabels=corr.columns.values)
```

## Non-parametric Methods for Correlation

> - **Spearman's rank correlation**: Finds the R correlation between variable-pairs of ordinal data types. Variable-pair are then able to be ranked according to the strength of the correlation between them.
> -**Chi-square table**s (pronounce 'kai')
 
### Spearman's rank correlation

> - R = 1 -> Strong positive Relationship
> - R = 0 -> not linearly correlated
> - R = -1 -> Strong negative relationship

> **Assumption**
> - Variables are ordinal (numeric,but able to be ranked like a categorical var)
> - related non-linearly
> - non-normally distributed

#### Implementation with scipy

**Imports**

```py
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats import spearmanr
```

```py
cyl = cars['cyl']
vs = cars['vs']
am = cars['am']
gear = cars['gear']
spearmanr_coefficient, p_value = spearmanr(cyl, vs)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)


spearmanr_coefficient, p_value = spearmanr(cyl, am)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)


spearmanr_coefficient, p_value = spearmanr(cyl, gear)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)
```

### Chi-square table

> - p < 0.05 -> Reject null hypothesis and conclude that the var are correlated
> - p > 0.05 -> Accept null hypothesis and conclude that the var are independent
> - R = -1 -> Strong negative relationship

**When to use**
> Categorical or numeric
> You have binned the numeric vars

#### Implementation 

**Imports**

```py
table = pd.crosstab(cyl, am)

from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(table.values)
print 'Chi-square Statistic %0.3f p_value %0.3f' % (chi2, p)
```

```py
table = pd.crosstab(cars['cyl'], cars['vs'])
chi2, a, dof, expected = chi2_contingency(table.values)
print 'Chi-square Statistic %0.3f p_value %0.3f' % (chi2, p)
```

```py
table = pd.crosstab(cars['cyl'], cars['gear'])
chi2, p, dof, expected = chi2_contingency(table.values)
print 'Chi-square Statistic %0.3f p_value %0.3f' % (chi2, p)
```

## Data Scaling

**Why?**
- Prevent differing magnitube among variables from producing erroneous/misleading statistics
- Prepare data for machine learning

**Two way to scale data**
- Normalization: put observation on a relative scale between values of 0 and 1
- Standardization: Rescaling data so it has a zero mean and unit variance

**Scikit-learn preprocessing**
- Scale data
- Center data
- Normalize data
- Bin data
- Impute data

**Imports**

```py
import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale
```

 **Implementations**

```py 
# Normalization
mpg_matrix = mpg.reshape(-1,1)
scaled = preprocessing.MinMaxScaler()
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)

mpg_matrix = mpg.reshape(-1,1)
scaled = preprocessing.MinMaxScaler(feature_range=(0,10)) # custom range
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)

# Standardization
standardized_mpg = scale(mpg, axis=0, with_mean=False, with_std=False) # this will result in the  same original values
plt.plot(standardized_mpg)

# Scale
standardized_mpg = scale(mpg)
plt.plot(standardized_mpg)
```

