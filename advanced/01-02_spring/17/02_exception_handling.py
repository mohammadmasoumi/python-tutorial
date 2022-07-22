class AException(BaseException):
    pass

class BException(AException):
    pass
      
class CException(BException):
    pass

class DException(CException):
    pass


try:
    raise DException()
except AException:
    print(f"catched AException")
except BException:
    print(f"catched BException")
except CException:
    print(f"catched CException")
except DException:
    print(f"catched DException")


try:
    raise DException()
except DException:
    print(f"catched DException")
except CException:
    print(f"catched CException")
except BException:
    print(f"catched BException")
except AException:
    print(f"catched AException")


