mylist = [1, -2, 3, 4, 5, 5, 7, 72, 9, 0]

# get the lowest value
min = mylist[0]
max = mylist [0]

for x in mylist:
    if x < min:
       min = x

print(min)

# get the highest value
for x in mylist:
    if x > max:
       max = x

print(max)
mylist[1] = 10000
print(mylist)

# print list of duplicate values