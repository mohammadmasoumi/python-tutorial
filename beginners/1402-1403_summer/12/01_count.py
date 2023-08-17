"""
my_list = ["hello", "bye", "bye", 1, 2, "12", 12.2, "12", 2]

key -> value (pair)
item -> count

result = []

1. "hello"
 - search item in result
    - exist -> ++count
    - not exist -> append 
2. "bye"
 - search item in result
    - exist -> ++count
    - not exist -> append 

search item in result
```python
# result: [
#      0     1
#   [item, count], 0  
#   [item, count], 1
#   [item, count], 2
#   [item, count]  3
# ]
result = []
item: "hello"

# result = [["bye", 1], ["hello", 2], [2, 2]]
# search item in result
for elem in result:
    #          0     1
    # elem: [item, count]
    # elem: ["bye", 1]
    if item == elem[0]:
        # exist -> ++count
        elem[1] += 1 
        break
    else:
        result.append([item, 1])

```


 


"""