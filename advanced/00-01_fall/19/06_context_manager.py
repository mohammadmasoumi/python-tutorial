# context management


"""
error handling

1. try except
2. context manager
"""

# # file
# try:
#     file = open("file.txt", "r")
#
# except Exception:
#     file = None
#     pass
#
# finally:
#     # local variable
#     if file:  # bool(file)
#         file.close()


# key with
with open("file.txt", "r") as file:
    file.readlines()
