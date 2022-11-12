#
# closure (sth) binding (fuction)

# closure
def binding(n):

    def wrapper(m):
        return n * m

    return wrapper


# 3 <=> wrapper
binding_3 = binding(3)
print(binding_3(10))
print(binding_3(11))
