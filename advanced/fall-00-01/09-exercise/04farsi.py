list1 = input("please insert some integers :\n").split()
list_1 = [int(num) for num in list1]
num = input("how many do you want that last integer go back : please insert one int number !\n")
num = int(num)
x = 1
while x <= num:
    for i in range(0, len(list_1) - 1):
        m = list_1.pop()
        list_1.insert(0, m)
    x = x + 1
print(list_1)
