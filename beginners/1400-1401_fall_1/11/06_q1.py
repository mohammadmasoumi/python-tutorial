s = input().split()
a = int(input())

a %= len(s)

print("".join(s[a:]) + "".join(s[:a]))
