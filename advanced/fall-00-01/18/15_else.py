while True:
    try:
        # code block
        a = int(input())  # do not execute the rest of code

    except ValueError:
        print("Try again.")
    else:
        # did not raise exception
        print("I passed!")
        break

# for idx in range(10):
#     # print()
#
#     # if idx == 20:
#     if idx == 9:
#         print("I could find the 9!")
#         break
# else:
#     print("I couldn't find the 20!")
