def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        print("fibo", x, y)
        yield x

def square(nums):
    # nums: fibonacci_numbers(10)
    # next(nums)
    # num: 1
    for num in nums:
        print("num", num)
        yield num**2

# next(square)
# s = 0
# for item in square(fibonacci_numbers(10)):
#     s += item
    # print(item)

print(sum(square(fibonacci_numbers(10))))