
# methods

def calc_s_circle1(radius):
    # 3.14 * radius ** 2
    return 3.14 * pow(radius, 2)

def calc_s_circle2(radius):
    # radius = 4
    # 3.14 * radius ** 2
    print("calc_s_circle2(1): ", 3.14 * pow(radius, 2)) 

def calc_s_circle3(radius):
    # radius = 4
    # 3.14 * radius ** 2
    print("calc_s_circle3(1): ", calc_s_circle2(radius)) 


print("calc_s_circle3(2): ", calc_s_circle3(4))

#s = calc_s_circle1(4) 
#print(s)
#print("--------------")
#print("calc_s_circle1: ", calc_s_circle1(4))
#print("--------------")
#calc_s_circle2(4)
#print("--------------")
# print("calc_s_circle2(2): ", None)
# print("calc_s_circle2(2): ", calc_s_circle2(4))