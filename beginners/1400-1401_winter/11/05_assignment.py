"""
5
ali 20
hassan 12
hossein 10
mohammad 2
asghar 20
----------------
3 
ali
mobin
hassan
"""
n = int(input())

my_names = []

# print("  mohammad    ".strip())

# [['ali', 20], ['mohammad', 10], ['hassan', 18]]
# ['ali 20', 'mohamamd 10', 'hassan 18']
# [['ali', '20'], ['mohammad', '10'], ['hassan', '18']]
for _ in range(n):
    name = input()
    # name: "ali 20"
    # name.split() # default " "
    # ["ali", "20"]
    my_names.append(name.split())

print(my_names)




