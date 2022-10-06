a = input()
b = input()

diff = 0

if len(b) >= len(a):
    bozorghtar = b
    kochiktar = a
else:
    kochiktar = b
    bozorghtar = a

for idx, item in enumerate(bozorghtar):
    if idx < len(kochiktar):
        # ==
        # !=
        if bozorghtar[idx] != kochiktar[idx]:
            diff += 1
    else:
        diff += 1

print(diff)
