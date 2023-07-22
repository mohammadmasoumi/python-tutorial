# 1.
try:
    n = int(input())
except ValueError:
    print("value error")

else:
    try:
        print(10/n)
    except ZeroDivisionError:
        print("zerodivision error")

# 2.

try:
    n = int(input())
    print(10/n)
except (ValueError, ZeroDivisionError) as e:  # e: instance exception
    # instance: error
    if isinstance(e, ValueError):
        print("value error")
    elif isinstance(e, ZeroDivisionError):
        print("zerodivision error")

# 3.

try:
    n = int(input())
    print(10/n)
except ValueError as e:  # e: instance exception
    print("value error")
    print(e.args)
    print(e.with_traceback())
except ZeroDivisionError:
    print("zerodivision error")
