# array
arr1 = [1, 2, 3]
arr2 = [0, 6, 7]
arr3 = [0] * 10

# append at the end of the list
arr1.append(4)
arr1.extend(arr2)
arr1.insert(1, 100)
arr1.insert(2, 100)

arr5 = arr1

# double ctrl + arrow down
print(f"address of {id(arr1)}")
print(f"address of {id(arr5)}")

arr1.append(200)
# arr4 = arr1.copy()


# the first one
print(arr1.index(100))

# {1, 2, 3, 4}
# arr1.append(1)
# arr1.append(2)
# arr1.append(3)

print(arr1)
print(arr5)
print(arr3)

# copy of array
arr7 = arr1.copy()
# arr6 = []
#
# print(f"arr6: {arr6}")
# print(f"arr7: {arr7}")
#
# for item in arr7:
#     a = arr7.pop()
#     print(f"a: {a}")
#     arr6.append(a)
#
# print(f"arr6: {arr6}")
# print(f"arr7: {arr7}")

# clear
arr8 = [1, 2]
print(arr8)
# arr8.clear()
# 000002535F35F3C0
print(id(arr8))
print(arr8.clear)
print(arr8.clear())  # return None
print(arr8)
