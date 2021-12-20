"""
11 33
"""
h, l = input().split()
h, l = int(h), int(l)

for i in range((h - 1) // 2):
    print(("|*|" * ((2 * i) + 1)).center(l, '-'))

print("Hello world".center(l, '-'))

#           4 , 0
#                    4, 3 , 2, 1, 0
#                     start        end  step
for i in range(((h - 1) // 2) - 1, -1, -1):
    print(("|*|" * ((2 * i) + 1)).center(l, '-'))
