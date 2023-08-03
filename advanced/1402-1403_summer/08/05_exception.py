
"""
try

except

else

finally
"""
# 1.
# ValueError -> n: non other than digit
# ZeroDivisionError -> 12/0

# float("12.2")
# int("12.2") raise Exception
 
# try -> raise exc catch -YES-> except -> finally
#                        -NO-> else -> finally
#                  not catch exit 0
# try:
#     # n = float(input())
#     n = int(input())
#     m = 12 / n
# except ValueError:
#     print("ValueError")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# else:
#     print(f"m: {m}")
# finally:
#     # close opened resources
#     print("I am in finally.")

# 2.

# try -> raise ValueError -> except -> re-raise ValueError -> catch ValueError [STOP] finally -> re-raise ValueError

# try -> raise exce -> except -> re-raise exception -> catch re-raised exception
# -> finally -> re-raised catched exception 
# try:
#     n = int(input())
#     m = 12 / n
# except ValueError as e:
#     print("ValueError")
#     # raise ZeroDivisionError()
#     raise e
# except ZeroDivisionError as e:
#     print("ZeroDivisionError")
#     # raise ValueError()
#     raise e
# else:
#     print(f"m: {m}")
# finally:
#     # close opened resources
#     print("I am in finally.")

# 3. 
# def run():
#     try:
#         raise ValueError()
#     except ValueError as e:
#         print("ValueError")
#         raise e # skip
#     except ZeroDivisionError as e:
#         print("ZeroDivisionError")
#         raise e # skip
#     else:
#         print("else!")
#     finally:
#         # close opened resources
#         print("I am in finally.")
#         return True

# print(run())

# 4. 
def run():
    try:
        # raise ValueError()
        m = 12
    except ValueError as e:
        print("ValueError")
        raise e
    except ZeroDivisionError as e:
        print("ZeroDivisionError")
        raise e
    else:
        print(f"m: {m}")
        return False # skip
    finally:
        # close opened resources
        print("I am in finally.")
        return True

print(run())