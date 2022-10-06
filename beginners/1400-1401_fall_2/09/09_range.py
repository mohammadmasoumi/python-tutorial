# index
# [0, ... , 9]
n = range(10)

print(n)
print(list(n))

# index range
# range(start, end, step)
# دنباله ای از اعداد
print(list(range(10, 20, 2)))

# اگر میخواهید روی آن بچرخید لازم نیست که کست کنید
for item in range(30, 20, -1):
    print(item)
