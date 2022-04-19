
try:
    a = int(input())
    print(12 / a)

except (ValueError, ZeroDivisionError) as e:
    if isinstance(e, ValueError):
        print("ValueError")
        
    elif isinstance(e, ZeroDivisionError):
        print("ZeroDivisionError")
