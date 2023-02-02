def function1():
    """This is a function1"""
    pass

function1.count = 12
def function2():
    """This is a function2"""
    pass

function2.__dict__ = function1.__dict__.copy()
function2.__name__ = function1.__name__
function2.__qualname__ = function1.__qualname__
function2.__doc__ = function1.__doc__

print(function1.__name__, function2.__name__)
print(function1.__qualname__, function2.__qualname__)
print(function1.__doc__, function2.__doc__)
print(function1.__dict__, function2.__dict__)
print(function1.count, function2.count)
function2.count = 13
print(function1.count, function2.count)
