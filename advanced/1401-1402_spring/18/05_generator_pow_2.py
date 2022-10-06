def my_pow_2(num):
    for i in range(num):
        yield pow(2, i)

# lazy loading
my_generator1 = my_pow_2(10)

print("----------------------------")
print(my_generator1)
for item in my_generator1:
    print(item)

print("----------------------------")
my_generator2 = (pow(2, i) for i in range(10))

print(next(my_generator2))
print(next(my_generator2))
print(next(my_generator2))

# print(my_generator2)
# for item in my_generator2:
#     print(item)
