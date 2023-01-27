def multi(n):
    def bounded(m):
        return n * m

    return bounded

# multi3: function
multi3 = multi(3)
print(multi3(4))
print(multi3(5))
print(multi3(6))

# ctrl + shift + alt + down arrow
multi4 = multi(4)
print(multi4(4))
print(multi4(5))
print(multi4(6))
