# a = set(input().split())
a = set(input().split())
# b = set(input().split())
b = set(input().split())

# print(list(a))
# print(set(a))
# print("----------")
# print(list(b))
# print(set(b))

a.symmetric_difference_update(b)
print(a)