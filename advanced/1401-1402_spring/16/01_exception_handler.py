# exception handling 
"""

try:

except:

else:

finally:


exception:
    ValueError
    NameError
    ZeroDivisionError
    AttributeError
    IndexError
    ....
"""

print("Before exception")


try:
    # code block
    print(12/0) # raise exception, EXIT!
    print("After exception in code block")

# except ZeroDivisionError:
except ValueError:
    # exception handling
    print("raised ZeroDivisionError!")


print("After exception")




