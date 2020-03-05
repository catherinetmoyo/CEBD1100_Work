student_number = input("Enter your student ID >")

if(len(student_number) < 8):
    raise Exception("sorry, student number must be 8 digits long")
