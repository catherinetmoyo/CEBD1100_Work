def deposit(amount: float):

    assert(amount > 0), "Sorry, the amount deposited must be positive"


value = input("Enter an amount of  deposit >")

try:
    deposit(float(value))
except AssertionError as error_text:
    print(error_text)

except Exception as error_text:
    print("An unhandled error has occurred :" + error_text)

else:
    print("if no error has occurred, run those lines")
    # send your email of confirmation of deposit here

finally:
    print("You can deposit RRSP until March 2nd")



    ############
    #OR
    ############

# def deposit(amount: float):
#
#     assert(amount > 0), "Sorry, the amount deposited must be positive"
#
#
# value = input("Enter a deposit >")
#
# try:
#     deposit(float(value))
# except:
#     print("Sorry, an error occurred")