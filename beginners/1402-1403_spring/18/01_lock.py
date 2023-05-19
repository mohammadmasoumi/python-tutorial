
current = input()
password = input()


"""
current: 1234
password: 9574

1234
4321
UUURURDRDDDO

1111
1111
RRRO

9999
4444
UUUUURUUUUURUUUUURUUUUUO

1234
9574
DDRUUURUUUURO
"""
for idx in range(len(current)):
    c = int(current[idx])  # c:1
    d = int(password[idx])  # d: 9
    # 1 -> 9
    # DD

    if c > d:
        # c: 9
        # d: 2
        if c - d >= 5:
            print("U" * (10-(c-d)), end="")
        else:
            print("D" * (c-d), end="")
    elif c < d:
        # c: 4
        # d: 6
        if d - c <= 5:
            print("U" * (d-c), end="")
        else:
            # c: 3
            # d: 9
            # 10 - (d-c)
            print("D"*(10-(d-c)), end="")

    if idx == len(current)-1:
        print("O", end="")
    else:
        print("R", end="")
