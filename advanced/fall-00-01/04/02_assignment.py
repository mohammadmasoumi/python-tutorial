a=input().split()
print(a)

a1 = int(a[0])
a2 = int(a[1])
a3 = int(a[2])

print(a1)
print(a2)
print(a3)

if a1 > a2 > a3:
    print(a3, a2 ,a1)
elif a1 > a3 > a2:
    print(a1 , a3,a2)
elif a2 > a1 > a3:
    print(a2 , a1 , a3 )
elif a2 > a3 > a1:
    print(a2 , a3 , a1)
elif a3 > a1 > a2:
    print(a3 , a1 , a2)
elif a3 > a2 > a1:
    print(a3 , a2 , a1)

