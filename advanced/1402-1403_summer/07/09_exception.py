

class AException(BaseException):
    pass


class BException(AException):
    pass


class CException(BException):
    pass


class DException(CException):
    pass


try:
    raise DException
except DException: # DException is instance (DException, CException, BException, AException)
    print("DException")
except CException: # CException is instance (CException, BExceptino, AException)
    print("CException")
except BException: # BException is instance (BExceptino, AException)
    print("BException")
except AException: # AException is instance (AException)
    print("AException")
