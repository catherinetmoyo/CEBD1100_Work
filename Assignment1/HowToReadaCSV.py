import csv

# create dictionaries and list
regions_units = {}
regions_rev = {}
regions = []

current_region = ""
current_units = 0
current_rev = 0


# read the input csv file
file = open("region_input.csv", 'rt')    # rt is the mode, need to install csv package
reader = csv.reader(file)

# This is the header we disregard it
next(reader)

for row in reader:
    print(row)   # temporary for debugging


    # Get the current row values
    current_region = row[0]
    current_units = row[1]
    current_rev = row[2]


    if not current_region in regions_units:
        regions_units[current_region] = current_units

    else:
        regions_units[current_region] = \
            int(regions_units[current_region]) + int(current_units)

# print(regions_units)

# change regions_units into a list
regions = list(regions_units.keys())

print(regions)

print("All the regions found are : ", end="")

for r in regions:
    print(r, end=",")
print()     # print a blank line

print("TOTAL PER REGION : ")

for r in regions:
    print(r)
    print("Total units per region :" + str(regions_units[r]))
    print()

