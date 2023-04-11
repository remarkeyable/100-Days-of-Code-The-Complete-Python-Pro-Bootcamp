<h1>Today's Learning Points</h1>


<ul>
<li>Use .head(), .tail(), .shape and .columns to explore your DataFrame and find out the number of rows and columns as well as the column names.</li>

<li>Look for NaN (not a number) values with .findna() and consider using .dropna() to clean up your DataFrame.</li>

<li>You can access entire columns of a DataFrame using the square bracket notation: df['column name'] or df[['column name 1', 'column name 2', 'column name 3']]</li>

<li>You can access individual cells in a DataFrame by chaining square brackets df['column name'][index] or using df['column name'].loc[index]</li>

<li>The largest and smallest values, as well as their positions, can be found with methods like .max(), .min(), .idxmax() and .idxmin()</li>

<li>You can sort the DataFrame with .sort_values() and add new columns with .insert()</li>

<li>To create an Excel Style Pivot Table by grouping entries that belong to a particular category use the .groupby() method </ul></li>
