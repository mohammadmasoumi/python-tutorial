
try:
    a = int(input())
    print(12 / a)

except ValueError:
    print("ValueError")

except ZeroDivisionError:
    print("ZeroDivisionError")
