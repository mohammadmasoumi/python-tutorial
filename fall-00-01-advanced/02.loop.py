arr1 = [idx for idx in range(10)]
# copy of array
arr7 = arr1.copy()
arr6 = []

print(f"arr6: {arr6}")
print(f"arr7: {arr7}")

# for idx in range(len(arr7)):
#     arr7[idx]

# for item in arr7:
#     item

for idx, item in enumerate(arr7):
    print(f"idx: {idx} - item: {item} - size: {len(arr7)}")
    a = arr7.pop()
    arr6.append(a)

print(f"arr6: {arr6}")
print(f"arr7: {arr7}")
