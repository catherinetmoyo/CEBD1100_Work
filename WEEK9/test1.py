import pandas as pd

# making values non scientific
pd.options.display.float_format = '{:.2f}'.format
# display fpr wide monitors
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

# parse_dates = if you see a date make it a date not a string
# infer_datetime_format = JJ-MM-AA
df = pd.read_csv("50000 Sales Records.csv", parse_dates=True, infer_datetime_format=True)
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

print("########")
print(df.groupby('region')['units_sold'].sum())

# the sum for Europe
print(df.groupby('region')['units_sold'].sum()['Europe'])









