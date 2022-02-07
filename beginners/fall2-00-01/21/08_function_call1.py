# recursive function

#                 retry=default_value
def function1(num, retry=3):
    print(f"num: {num}, retry: {retry}")


#         num=12, retry=3
function1(12)
#         num=12, retry=5
function1(12, 5)

# kw - positional
function1(retry=12, num=5)