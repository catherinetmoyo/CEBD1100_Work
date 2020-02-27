# x = 'abcd'
# for i in x:
#     print(i)
#     x = x.upper()
print()
values = [value % 2 for value in range(1, 6)]
print(values)

print()
my_list = list("hello")
print(my_list)

# x = (i in i in range(3))
# for i in x:
#     print(i)

print()
print(0.1 + 0.2 == 0.3)

print()
for i in range(5):
    if i == 5:
        break
    else:
        print(i)
else:
    print("here")

print()
for i in range(10):
    if i == 5:
        break
    else:
        print(i)
else:
    print("here")

print()
A = not (10 < 20) and not (10 > 30)
print(A)

print()
x = 'abcd'
for i in range(len(x)):
    print(x)
    x = 'a'

print()
countries = {'us': 'USA', 'fr': 'France', 'ca': 'Canada'}
for a, b in countries.items():
    print(b)
    break

print()
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

print()

