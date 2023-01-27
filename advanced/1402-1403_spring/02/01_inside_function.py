# [1]: declare function1 in memory
def function1():
    # [3]
    print("Inside function1")
    # [4]: declare function2 in memory
    
    # function2() WRONG
    def function2():
        # [6]
        print("Inside function2")

    # [5]
    # function2() # [7]

    return function2

# [2]
f = function1() # [8]
print(f)
# <function function1.<locals>.function2 at 0x000002CC2884EF80>
# f() # function2()
    