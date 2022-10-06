# map and filter
my_list = [None, 1, "Hello", True, False, [1, 2], [], None]

my_list2 = ["1", "2", "3"]

print([item for item in my_list if item != None])
print([int(item) * 2 for item in my_list2 if int(item) % 2])
print([int(item) * 2 if int(item) % 2 else  int(item) // 2 for item in my_list2])
print([item * 2 for item in my_list2 if int(item) % 2])

# input() "ali 20 20 19"
# input().split() ["ali", "20", "20", "19"]
# name, *scores = ["ali", "20", "20", "19"]
# name: "ali", scores: ["20", "20", "19"]
name, *scores = input().split() 
scores = list(map(int, scores))
# name: "ali", scores: [20, 20, 19]

