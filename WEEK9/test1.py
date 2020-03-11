import pandas as pd

# parse_dates = if you see a date make it a date not a string
# infer_datetime_format = JJ-MM-AA
df = pd.read_csv("50000 Sales Records.csv", nrows=5000, parse_dates=True, infer_datetime_format=True)
print(df)

# print the list of the keys aka columns on the csv file
# print(df.keys())

# making headers workable
# strip ote les espaces inutiles
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

print(df.columns)
print(df.unit_price.describe())
print()
print(df.unit_price.max())
print(df.unit_price.sum())
print(df.unit_price.mean())
print()
print(df.region.value_counts())
print()
print(df.region.unique)
print(df.region.values)











