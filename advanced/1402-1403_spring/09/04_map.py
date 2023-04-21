# map

my_list = [1, 2, 3, 4]
my_map = map(str, my_list) # iterator ["1", "2", "3", "4"]
 
print("------------------------")
for item in my_map: # next(my_map) -> StopIteration 
    # exhausted
    print(item)
    # next() next() next() next() 

print("------------------------")
for item in my_map: # next() -> StopIteration
    print(item)