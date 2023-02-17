# 12
# 12 % 10 = 2

n = 12345
mv = 0

while n != 0:
    mv = n % 10  # yekan
    # mv: 5
    # mv: 4
    # n = n // 10
    # n: 12345
    # n: 1234
    # n: 123
    # n: 12
    # n: 1
    # n: 0
    n //= 10

print(mv)

n = 12345
#     01234
# n: "12345"
# n[0]
print(int(str(n)[0]))
