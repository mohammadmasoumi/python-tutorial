# partial function

def adder(a, b):
    return a + b

def partial_function():
    return adder(10, 12)

print(partial_function())


"""
tkinter

def clickme():
    print("Clicked!")

#               function
<Button onClick={clickme}>
</Button>

# ----------------------------------
def clickme(a, b):
    print(a + b)

# wrap
def partial():
    return clickme(10, 12)

#               function
<Button onClick={partial}>
</Button>

"""

# 