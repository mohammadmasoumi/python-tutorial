
# first class object

"""
def add(a, b):
    result = a + b
    return result

# c = 12

# c = 25
c = add(12, 13)
"""


def shout(n):
    # n: 10
    result = n * 10
    # result: 100
    print(f"Shouuuuuuuuuuuuut result: {result}")
    # print in the console
    # code block
    # ...
    # 
    return result
    # return n * 10

# alias

# yell_1 is a function
# shout is a method
# add another label: yell_1
yell_1 = shout
yell_2 = shout(30)

# call/invole
result_yell_1 = yell_1(10)
shout(20)

print(f"result_yell_1: {result_yell_1}")

# <function shout at 0x000001593A7D2F70>
# <function shout at 0x000001593A7D2F70>

# print(yell_1)
# print(shout)

# # yell_2 is an int
# yell_2 = shout(3)

# # 
# yell_1(4)
# shout(5)
# print("---------------")
# print(f"yell_1: {yell_1}")
# print(f"yell_2: {yell_2}")