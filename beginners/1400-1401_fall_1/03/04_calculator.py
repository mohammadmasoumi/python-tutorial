a = int(input("عدد اول را واد کنید"))
opt = input()
b = int(input("عدد دوم را وارد کنید"))

# a = input()
# a = int(a)
# int()
# float()
# str()
# bool()
if opt == '+':
    print(a+b)

elif opt == '-':
    print(a-b)

elif opt == '/':
    if b == 0:
        print("division by")
    else:
        print(a/b)

elif opt == '*':
    print(a*b)



print(a)
print(opt)
print(b)









