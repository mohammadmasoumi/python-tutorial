
"""
2
asghar#hossein#farhad
sobhan#akbar#kazem
"""
n = int(input())
my_names = []

for _ in range(n):
    # input(): "asghar#hossein#farhad"
    # input().split("#"): ["asghar", "hossein","farhad"]
    # "sobhan#akbar#kazem"
    # ["sobhan", "akbar","kazem"]
    # my_names: ["asghar", "hossein","farhad", "sobhan", "akbar","kazem"]
    my_names.extend(input().split("#"))
    # [Faul] my_names += input().split("#")

print(my_names)