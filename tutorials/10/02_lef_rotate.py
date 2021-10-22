
n, shift = map(int, input().split())
my_list = tuple(map(int, input().split()))
my_list2 = [0] * n

for idx in range(n):
    my_list2[idx - shift] = my_list[idx]
    print(f"{idx - shift} | {my_list[idx]} | {my_list2}")

print(my_list2)