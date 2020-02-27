d1 = {'us': 'USA', 'ca': 'Canada'}  # curly bracket means it is a dictionary

print(d1.get('xx', 'NOT FOUND'))

# add a value into a dictionary
d1['yy'] = 'New country'
d1['yy'] = 'Hello'
d1['sen'] = 'Senegal'
d1.update({'yy': 'Germany'})
print(d1)

del d1['sen']
print(d1)

for key, value in d1.items():  # key for dictionary and index for lists
    print(key, value)

for x in d1.items():
    print(x)

for x in d1.keys():
    print(x)

for x in d1.values():
    print(x)

print(d1.keys())  # print the different keys into the dictionary

d2 = {999: "a", 888: "b"}
print(d2[888])

for x in d2.keys():
    print(x)
