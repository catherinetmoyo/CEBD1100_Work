age = input("what is your age ") #input is always giving out a string that need to be converted later into the desired type
gender = input("M or F ")

age = int(age)

if not (age < 20 and gender == 'M'):
    print("The candidate is OK")





