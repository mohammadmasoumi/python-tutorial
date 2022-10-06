n = int(input())
my_list = []

for i in range(n):
    point=int(input('enter a number for your list '))
    if point>20 or point<0:
        print('your number is incorrect')
        break
    else:
        my_list.append(point)
my_listfake=my_list.copy()
for idx in my_listfake:
    if idx<10:
        my_list.remove(idx)
print(my_list)