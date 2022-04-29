# 
# my_list = ['ali', 'hassan', 'hossein']

"""
Ali
Hossein
Hassan
Asghar
Akbar
"""
# my_names = []
# for _ in range(5):
#     name = input()
#     my_names.append(name)


"""
Ali Hossein Hassan Asghar Akbar
"""
my_names = input().split()
print("-".join(my_names))

for name in my_names:
    # end: \n  sep: " "
    print(name, end=" ")

