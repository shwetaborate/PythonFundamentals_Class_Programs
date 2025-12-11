
#raise Statement
try:
    name = input("Enter Your Name: ")
    age = int(input("Your Age Please: "))

    if age<18 or age >60:
        raise ValueError("Invalid Age! ")
    else:
        print(f"Welcome {name} your age is {age}")
except Exception as e:
    print(e)

#Custom Error class
class youngAgeError(Exception):
    def __init__(self, msg):
        self.msg = msg
class oldAgeError(Exception):
    def __init__(self, msg):
        self.msg = msg

try:
    name = input("Enter Your Name: ")
    age = int(input("Your Age Please: "))

    if age<18 :
        raise youngAgeError("Too young to enter")
    elif age >60:
        raise oldAgeError("Too old to enter")
    else:
        print(f"Welcome {name} your age is {age}")
except youngAgeError as e:
    print(e)
except oldAgeError as e:
    print(e)
except Exception as e:
    print(e)
