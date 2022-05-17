# closure

def multipler(x):
    # x: 3

    # x bind my_function 
    def my_function(n):
        # n: 10
        return x * n

    return my_function


# multipler_by_3: my_function
# type multipler_by_3: function
multipler_by_3 = multipler(3) # binding

print(multipler_by_3(10))
print(multipler_by_3(20))
print(multipler_by_3(30))

multipler_by_4 = multipler(4) # binding

print(multipler_by_4(10))
print(multipler_by_4(20))
print(multipler_by_4(30))

