while True:
    try:
        # code block
        a = int(input())  # do not execute the rest of code

        print(a / 0)
        break

    except:  # catch all type of exceptions
        print("Try again.")
