class AException(Exception):
    pass


class BException(AException):
    pass


class CException(BException):
    pass


for cls in (AException, BException, CException, Exception):

    # try:
    #     raise cls
    # except Exception:
    #     print("Exception")
    # except AException:
    #     print("AException")
    # except BException:
    #     print("BException")
    # except CException:
    #     print("CException")
    try:
        raise cls
    except CException:
        print("CException")
    except BException:
        print("BException")
    except AException:
        print("AException")
    except Exception:
        print("Exception")

# raise AException  # no input params
# raise call __init__ implicitly
# shortcut raise AException()
