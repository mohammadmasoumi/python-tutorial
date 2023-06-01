a1 = 12
b1 = [12, 13]

def do_sth(a2, b2):
    print("------------------------------")    
    print(f"[before in function] a2: {a2}, id: {id(a2)}")
    print(f"[before in function] b2: {b2}, id: {id(b2)}")
    print("------------------------------")    
    a2 = "ali"
    b2.append(14)
    print(f"[after in function] a2: {a2}, id: {id(a2)}")
    print(f"[after in function] b2: {b2}, id: {id(b2)}")
    print("------------------------------")    

print(f"[before call] a1: {a1}, id: {id(a1)}")
print(f"[before call] b1: {b1}, id: {id(b1)}")
do_sth(a1, b1)
print(f"[after call] a1: {a1}, id: {id(a1)}")
print(f"[after call] b1: {b1}, id: {id(b1)}")




