
class AException(BaseException):
    pass

class BException(AException):
    pass

class CException(BException):
    pass

class DException(CException):
    pass

d = DException()
print(isinstance(d, AException)) # True  
print(isinstance(d, BException)) # True
print(isinstance(d, CException)) # True
print(isinstance(d, DException)) # True

c = CException()
print(isinstance(c, DException)) # False
print(isinstance(c, CException)) # True
print(isinstance(c, BException)) # True
print(isinstance(c, AException)) # True


# try:
#     # raise DException()
#     raise BException()
# except AException: # isinstance( DException(), AException)
#     print("AException")
# except BException:
#     print("BException")
# except CException:
#     print("CException")
# except DException:
#     print("DException")
        
try:
    # raise DException()
    # raise CException()
    raise BException()
except DException:
    print("DException")
except CException:
    print("CException")
except BException:
    print("BException")
except AException: # isinstance( DException(), AException)
    print("AException")


try:
    pass
except Exception:
    pass
except ValueError:
    pass
except ZeroDivisionError:
    pass

