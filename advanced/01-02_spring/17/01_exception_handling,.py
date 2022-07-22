# exception handling
class AException(BaseException):
    pass


try:
    a = int(input())
    # exception = AException()
    # raise exception
    print(12/a)

except ZeroDivisionError as asghar:
    print(asghar)
    # code block
    # exception handler

except ValueError as exc:
    print(exc)
    # code block
    # exception handler
