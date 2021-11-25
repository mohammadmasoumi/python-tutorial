while True:
    try:
        # code block
        a = int(input())  # do not execute the rest of code

        print(a / 0)
        break

    except ValueError:
        print("Try again.")

    except ZeroDivisionError:
        print("ZeroDivisionError")
        break
