
def add_by_two(*inputs):
    print(f"inputs: {inputs}, type: {type(inputs)}")


my_nums = map(int, input().split())

# my_nums = [1, 2, 3]
#           *my_nums
#            1, 2, 3

# add_by_two(1, 2, 3)
print(f"my_nums: {list(my_nums)}") 
add_by_two(*my_nums)
