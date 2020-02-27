first_name = input("My first name is : ")
last_name = input("My last name is : ")

initials = (first_name[0]+last_name[0])
# print("My initials are : " + initials)

print("My initials are %s and %s" % (first_name[0].upper(), last_name[0].upper()))

