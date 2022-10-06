
n = int(input())

reversed_n = 0


# n: 123456
# reversed_n = 6
# reversed_n = 60 + 10
while True:

    reminder = n % 10
    reversed_n = reversed_n * 10 + reminder
    n = n // 10

    if n == 0:
        print(reversed_n)
        break

