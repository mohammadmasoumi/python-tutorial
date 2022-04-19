# as alias
from time import sleep as sleep2  # sleep <--> sleep2

while True:
    try:
        sleep2(0.1)
        # code block
        a = int(input())  # do not execute the rest of code

        print(a / 0)
        break

    except (ValueError, ZeroDivisionError) as e:
        # e is an instance of ValueError
        # catch both exceptions, and do one task for both
        if isinstance(e, ValueError):
            print("[ValueError] Try again.")
        else:
            print("[ZeroDivisionError] Try again.")
            break
