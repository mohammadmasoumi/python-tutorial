# inline if else
# زمانی که مقدار یک متغیر وابسته به یک شرط است
num = int(input())

# inline if-else
# name1 = true_value if condition else false_value

# if num < 10:
#     name1 = "asghar"
# else:
#     name1 = "akbar"
name1 = "asghar" if num < 10 else "akbar"

print(name1)
print("asghar" if num < 10 else "akbar")

# inline if-else
name2 = None
if num < 10:
    # NameError: name 'name2' is not defined. Did you mean: 'name1'?
    name2 = "asghar"

# name2 = if num < 10
name2 = "asghar" if num < 10 else None
print(name2)
