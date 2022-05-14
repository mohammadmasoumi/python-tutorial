n = int(input())

"""
دوره تناوب 9

36 => 9
35 => 8
34 => 7
33 => 6
32 => 5
31 => 4
30 => 3
29 => 11 => 2
28 => 10 => 1
27 => 9 
26 => 8 
"""

# reminder = n % 9
#
# if reminder == 0:
#     print(9)
# else:
#     print(reminder)

# n = int(input())
print(9 if n % 9 == 0 else n % 9)


# ---------- Other solution ----------
# n: str
n = input()

while True:
    s = 0
    for num in n:
        s += int(num)

    if s < 10:
        print(s)
    else:
        n = str(s)

