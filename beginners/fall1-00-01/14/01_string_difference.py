input1 = input()
input2 = input()

if len(input1) > len(input2):
    str1, str2 = input1, input2
else:
    str1, str2 = input2, input1

diff = 0
for idx, char in enumerate(str1):
    if idx < len(str2):
        if char != str2[idx]:
            diff += 1
    else:
        diff += 1

print(diff)
