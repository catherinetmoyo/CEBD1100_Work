# define Python user-defined exceptions
class Error(Exception):
    pass

# ValueTooSmallError is a type of error
class ValueTooSmallError(Error):
    pass

num = -3

try:
    if num<0:
        raise ValueTooSmallError
except ValueTooSmallError:
    print("you reached this because you value was too small")
except Exception as e:
    print("An unknown has error occurred" + str(e))
