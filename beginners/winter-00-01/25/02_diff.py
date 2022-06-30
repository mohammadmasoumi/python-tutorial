a = input()
b = input()


"""
a="aab"
b="ac"
diif=2

a="ali"
b="asghar"
diff=5

a="aaa"
b="aab"
diff=1
"""
diff = 0
for item1, item2 in zip(a, b):
    diff += 1 if item1 != item2 else 0

diff += abs(len(a) - len(b))
print(diff)

diff = 0
print("-----------------------------")
for idx in range(max(len(a), len(b))):

    if idx < len(a) and idx < len(b):
        if a[idx] != b[idx]:
            diff += 1
    else:
        diff += 1

print(diff)






