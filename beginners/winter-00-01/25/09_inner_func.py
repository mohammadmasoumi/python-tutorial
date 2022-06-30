def add(a, b):
    print("Out")
    return a  + b

def summation(my_list):
    # [(10, 11), (12, 13), (14, 15)]
    def add(a, b):
        print("In")
        return a  + b

    s = 0
    for c, d in my_list:
        # item: (10, 11)
        s += add(c, d)

    return s

print(summation([(10, 11), (12, 13), (14, 15)]))
# add(12, 13)