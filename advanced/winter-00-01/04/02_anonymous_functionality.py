# map, filter

my_list = [1, 2, 3, 4]
my_list2 = ["1", "2", "3", "4"]

def multiply_by_2(item):
    return item * 2

# map( function , iterable  )
# my_list
# multiply_by_2(1)
# multiply_by_2(2)
# multiply_by_2(3)
# multiply_by_2(4)
print(list(map(multiply_by_2, my_list)))
print(list(map(lambda item: item * 2, my_list)))
#                     vorodi   khuruji
print(list(map(lambda vorudi: vorudi * 2, my_list)))
# "a" * 2 = "aa"
# "a" * 3 = "aaa"
print(list(map(lambda vorudi: vorudi * 2, my_list2)))
print(list(map(lambda vorudi: int(vorudi) * 2, my_list2)))
print(list(map(int, my_list2)))

# filter( function , iterable  )
def filter_only_2(item):
    # True, False
    # True if item == "2" else False
    return item == "2"

# false true false false
# ["1", "2", "3", "4"]
# ["2"]

print(list(filter(lambda item: item == "2", my_list2)))
#print(list(filter( lambda vorodi: , my_list2)))