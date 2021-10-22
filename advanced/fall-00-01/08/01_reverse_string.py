# slicing
s = "mohammad-mohammad"

# 0 - len(s) - 1
# same as the range
# range(10, 1, -1)
# -------------------------------- first solution ------------------------
# start - end - step
# print(s[1:10:1])
# print(s[10:1:-1])
print(s[::-1])

# -------------------------------- second solution ------------------------

s = "mohammad-mohammad"
reversed_string = ""

for idx in range(len(s) - 1, -1, -1):
    # print(idx, len(s))
    # len(s)
    # IndexError: string index out of range
    # s.pop(idx)  'str' object has no attribute 'pop'

    print(reversed_string)
    reversed_string += s[idx]

print(f"reversed_string: {reversed_string}")

# -------------------------------- third solution ------------------------

s_list = list("mohammad-mohammad")
reversed_list = []

for idx in range(len(s) - 1, -1, -1):
    reversed_list.append(s_list.pop(idx))

print(f"reversed_string: {''.join(reversed_list)}")
