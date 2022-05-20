# اگر یک کاری رو بخواهیم روی همه آیتم های یک لیست انجام دهیم.
my_list = [1, 2, 3, 4]

def double(item):
    # item --> double ---> 2 * item
    return item * 2

# print(double(2)) # invoke, call
# print(double(3))

# for idx, item in enumerate(my_list):
#     my_list[idx] = double(item)

# print(my_list)
# <map object at 0x00000154C6F6B070>
print(list(map(double, my_list)))