my_list = [1, 2, 3, 4]

# def func(item):
#     return item * 2

# anonymous - inline function
#          lambda inputs: outputs
# func = lambda a, b: a * 2, b * 3

# print(list(map(func, my_list)))
print(list(map(lambda a: a * 2, my_list)))

# with inputs
func1 = lambda x: x * 2
print(func1(2))
print(func1(3))

# no inputs
func2 = lambda : 10 * 2
print(func2())
print(func2())

# multiple inputs and one output
func3 = lambda a, b: a + b
print(func3(10, 20))
print(func3(20, 30))