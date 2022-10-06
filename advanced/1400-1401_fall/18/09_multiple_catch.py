while True:
    try:
        # code block
        a = int(input())  # do not execute the rest of code

        print(a / 0)
        break

    except (ValueError, ZeroDivisionError):
        # catch both exceptions, and do one task for both
        print("Try again.")
