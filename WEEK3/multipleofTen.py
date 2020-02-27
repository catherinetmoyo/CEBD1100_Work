# 1
'''while True:
    value = input("enter a number:")

    if value.upper() == "Q":
        break

    if int(value) % 10 == 0:
        print("multiple of ten")
    else:
        print("not a multiple of ten")'''

# 2
value = ""
i = ""
mylist = []

while True:

    value = input("enter a number >")

    if value.upper() == "Q":
        break

    mylist.append(int(value))

sum = 0
for a in mylist:
    sum += a
print(sum)
print(sum/len(mylist))
print(mylist)



