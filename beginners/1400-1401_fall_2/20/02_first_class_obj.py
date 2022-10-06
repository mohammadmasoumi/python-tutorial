# 
def shout():
    print("Shoooooooooooooooout")
    # return None

# functions are variables
yell = shout

# 1773033589920
# 1773033589920
# the same box
print(id(shout))
print(id(yell))

#             None
# print(       None        )
print(       shout()        ) 
print(yell())
yell()