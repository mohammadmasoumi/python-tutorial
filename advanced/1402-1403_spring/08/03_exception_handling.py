# Solution1

class Int:

    def __truediv___(self, o):
        if isinstance(o, int) and o==0:
            raise ZeroDivisionError()

try:
    n = int(input())
    print(12//n)
    raise OSError()

except Exception as e: # ValueError, ZeroDivision
    if isinstance(e, ValueError):
        print("ValueError")
    elif isinstance(e, ZeroDivisionError):
        print("ZeroDivisionError")
    else:
        print("OtherError")

# Solution2
try:
    n = int(input())
    print(12/n)
    raise OSError()
    
    print("Hello")
    print("Hello")
    print("Hello")

except ValueError: # ValueError, ZeroDivision
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")

print("Hello")