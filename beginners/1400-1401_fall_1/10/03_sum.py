# builtin functions sum
# list, str, int, float, bool, enumerate

# فقط برای لیست های یک بعدی
my_list = [10, 20, 30]

# unsupported operand type(s) for +: 'int' and 'list'
# my_list = [[10, 20, 30]]

# print(sum(my_list))

my_list2 = [
    [10, 20, 30],
    [40, 50, 60]
]

s = 0
for item in my_list2:
    s += sum(item)
print(s)
