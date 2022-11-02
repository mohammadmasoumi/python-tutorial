def add(*asghar):
    # asghar: (10, 12)
    # [*asghar]: [10, 12]
    # [*asghar] * 2: [10, 12, 10, 12]
    return [*asghar] * 2

# 
# 1. 44 
# 2. 20, 24, 44
# 3.  

print(sum(add(10, 12)))
print(sum(add(10, 12, 14)))