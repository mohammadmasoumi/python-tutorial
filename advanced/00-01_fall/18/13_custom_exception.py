class AException(Exception):
    pass


class BException(AException):
    pass


class CException(BException):
    pass


raise AException  # no input params
# raise call __init__ implicitly
# shortcut raise AException()


