def shout(name):
    print(f"Shoooooooooooooout {name}")


# invoke a function
# call function

# shout()
# <function shout at 0x00000144CCD94DC8>
# my function is a variable
# type: <class 'function'>
# name: shout
# value: 
print(shout, type(shout))

a = 12
b = a

# assign a new name
yell = shout
print(yell, type(yell))

shout("ahmad")
yell("asghar")