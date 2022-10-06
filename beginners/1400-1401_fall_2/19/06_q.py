# methods

def calc_s_circle2(radius):
    print("Hello")
    print("calc_s_circle2(1): ", 3.14 * pow(radius, 2)) 
    return 
    print("Bye")

def calc_s_circle3(radius):
    print("Hello")
    return
    print("calc_s_circle3(1): ", calc_s_circle2(radius)) 
    print("Bye")

print("calc_s_circle3(2): ", calc_s_circle3(4))