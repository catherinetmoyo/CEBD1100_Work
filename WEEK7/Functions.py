# define a function 1
def print_name(first, last):
    print("Hello " + first + " " + last)
    return "oh djadja"


# function 2
def add_numbers(numb1, numb2):
    result = numb1 + numb2
    return result  # or return numb1 + numb2


# function 3
def my_max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n3:
        return n2
    else:
        return n3


# function 4
def my_max2(n1, n2, n3):
    my_list = [n1, n2, n3]
    return max(my_list)


# function 5
def my_max3(n1, n2, n3):
    my_list = []
    input1 = my_list.append(n1)
    input2 = my_list.append(n2)
    input3 = my_list.append(n3)
    return max(input1, input2, input3)


# call functions
print(print_name("Catherine", "Moyo"))
print(add_numbers(123, 321))
print(my_max(400, 200, 300))
print(my_max2(400, 200, 300))
print(my_max3(400, 200, 300))

