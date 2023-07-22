n = int(input())

try:
    res = 10/n
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print(f"res is: {res}")
    print("no exception has occured.")


try:
    pass
    # conn = connect to DB
    a = 12
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print(a)
    # conn = connect to DB
    # curoser = conn.cursor()
    # query ...
    print("no exception has occured.")
