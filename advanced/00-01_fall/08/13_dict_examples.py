# from pprint import pprint
# pretty print

# student_list = {}
#
# n = int(input())
#
# for _ in range(n):
#     name, avg = input().split()
#     # key = name
#     # value = avg
#     student_list[name] = float(avg)
#
# print(student_list)

d = {
    # immutable
    # TypeError: unhashable type: 'list'
    # [1, 2]: "asghar",  # can not define
    (1, 2): "asghar",  # can define
    (1, 2): "akbar",
    (1, 2): "asghar1",
    (1, 2): "asghar2",
}
print(d[(1, 2)])
