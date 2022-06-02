
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!
# 4! = 4 * 3 * 2 * 1



# FIRST IN LAST OUT
# FILO
#
# number: 5
# 5! = 5 * 4! 
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 
# numbber: 4
#          5  * factoril(4)
#          4  * factoril(3)
#          3  * factoril(2)
#          2

# factoril(5) = 120
# factoril(5) = 5 * factoril(4)[24]
# factoril(4) = 4 * factoril(3)[6]
# factoril(3) = 3 * factoril(2)[2]
# factoril(2) = 2


# factoril(3) = 3 * factoril(2)
# 

def factoril(number):
    # number: 3

    if number == 2:
        return 2

    return number * factoril(number - 1)
    


# |                    |
# |                    |
# |                    |
# |                    |
# |                    |
# |                    |
# |                    |
# |                    |
# |   --------------   |
#       STACK
# پشته

print(factoril(5))