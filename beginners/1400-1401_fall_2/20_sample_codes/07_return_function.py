# return function as a return value


def function1():
    def function2():
        def function3():
            return "Hello"

        return function3

    return function2


# function1()()()
# [ [ [ function1() ] () ] () ]
# [function2 = function1()]()()
# [function3 = function2()]()
# ["Hello" = function3()]
result = function1()()()
print(result)
