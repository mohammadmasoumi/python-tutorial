# built-in
# exhaustion
# exhausted

my_list = [1, 2, 3, 4]

def function(x):
    return x % 2

# [1, 0, 1, 0]
b = map(function, my_list)
print(b)

# m = []
# for item in b:
#     m.append(item)

# print(list(b))

print("--------------------")
for item in b:
    print(item)