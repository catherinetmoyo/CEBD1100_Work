def multiply_by_10(n: int):
    return n*10


try:
    my_integer = int(input("Enter the integer of your choice >"))
    value = multiply_by_10(my_integer)
    print(value)
except:
    print("Your number is not an integer")
finally:
    print("you are a BOSS !")

