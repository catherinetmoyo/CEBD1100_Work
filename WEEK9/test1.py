import pandas as pd
import matplotlib.pyplot as mpl


# making values non scientific
pd.options.display.float_format = '{:.2f}'.format
# display fpr wide monitors
# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 20)
# pd.set_option('display.width', 1000)

# parse_dates = if you see a date make it a date not a string
# infer_datetime_format = JJ-MM-AA
df = pd.read_csv("50000 Sales Records.csv", nrows=50, parse_dates=True, infer_datetime_format=True)
print(df)

# print the list of the keys aka columns on the csv file
# print(df.keys())

# making headers workable
# strip ote les espaces inutiles
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

# print(df.columns)
print(df.total_revenue.describe())
# print()
# print(df.unit_price.max())
# print(df.unit_price.sum())
# print(df.unit_price.mean())
# print()
# print(df.region.value_counts())
# print()
# print(df.region.unique)
# print(df.region.values)


# print("##########")
# print(df.describe())
# print("##########")
# print(df.describe(include=object))

# print("########")
# print(df.groupby('region')['units_sold'].sum())
#
# # the sum for Europe
# print(df.groupby('region')['units_sold'].sum()['Europe'])


print(df.groupby('region')['units_sold'].sum())

a = df.groupby('region').sum()['units_sold']


# # histogram
# a.plot(kind='bar', x='region', y='units_sold')
# mpl.show()
#
# # pie chart
# a.plot(kind='pie', x='region', y='units_sold')
# mpl.show()

squares = [1, 4, 9, 16, 25, 500]

mpl.plot(squares, linewidth=5)
mpl.title("Square Numbers", fontsize=24)
mpl.xlabel("Value", fontsize=14)
mpl.ylabel("Square of Value", fontsize=14)
mpl.tick_params(axis='both', labelsize=14)
mpl.plot(squares)
mpl.show()








