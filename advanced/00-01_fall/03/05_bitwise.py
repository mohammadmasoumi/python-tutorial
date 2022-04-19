# args = input().split('*')
args = input().split()
# print(args)

n = int(args[0])
k = int(args[1])

# print(range(2))
# a = [1, 2, 3, 4]
# b =[2, 3, 4, 5]
# b =[3, 4, 5]

max_and = 0
max_or = 0
max_xor = 0

for a in range(1, n):
    for b in range(a + 1, n + 1):
        res_and = a & b
        res_or = a | b
        res_xor = a ^ b

        if res_and < 4:
            max_and = max(max_and, res_and)

        if res_or < 4:
            max_or = max(max_or, res_or)

        if res_xor < 4:
            max_xor = max(max_xor, res_xor)

print(max_or)
print(max_and)
print(max_xor)
