def checkVarOuter():
    count = 10
    def changeVarInner():
        nonlocal count
        count += 5
        print("count of inner function: ", count)
    changeVarInner()
    print("Modified value in inner function:", count)

checkVarOuter()

# Globar Variable
globeVar = 100
count = 10

def checkglobalVar():
    print("Checking value of globar variable:", globeVar)

checkglobalVar()


def increment_counter():
    global count
    count += 5
    print("After increment: ", count)

increment_counter()

# python closures

def outer(x):
    def inner(y):
        return x+ y
    return inner # encosing fn has to return nested fn

result = outer(5)


print(' Sum (result): ', result(7))
