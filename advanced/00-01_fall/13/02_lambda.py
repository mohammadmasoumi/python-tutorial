# lambda

func1 = lambda a, b: print(a + b)
# func2 = lambda a, b: a, b # exception
func2 = lambda a, b: a + b
func3 = lambda: 10 * 10  # no input

func1(10, 12)
print(func2(10, 12))
print(func3())
