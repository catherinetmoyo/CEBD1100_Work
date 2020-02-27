def is_divisible_by_3(n):
    return n % 3 == 0


test = input("Enter a number :")
if is_divisible_by_3(int (test)):
    print("yes, it is divisible by 3")
else:
    print("not divisible by 3")
