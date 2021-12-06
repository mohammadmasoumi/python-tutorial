# int([1, 2, 3, 4])
# TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
# numbers = int(input().split())
numbers = input().split()

print(numbers)
_sum = 0
for number in numbers:
    print(f"sum: {_sum}, num: {number}")
    _sum += int(number)

print(_sum)
