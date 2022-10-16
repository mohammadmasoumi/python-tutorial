
"""
3
Mohseni 18 17 19
Mobin 20 20 20 
Sabour 15 12 13

---------------------
| Name    | Art | Math |
---------------------
| Mohseni | 20  |  20  |
---------------------
| Mobin   | 20  |  20  |
---------------------
| Sabour  | 20  |  20  |
---------------------
"""

# a, *b = 12, 13, 14
# b: [12, 14]
# *b
# 12, 13

# my_list = ["ali", "asghar", "hassan", "mohammad"]
# for idx, name in enumerate(my_list[1:]):
#     print(idx, name)

n = int(input())

my_list = []

for _ in range(n):
    # items: "Mohseni 18 17 19"
    # items: ["Mohseni", "18", "17", "19"]
    items = input().split()
    name = items.pop(0) # index
    # items: ["18", "17", "19"]
    #                    0     1     2 
    #      items[1:] = ["18", "17", "19"]
    for idx, score in enumerate(items):
        # idx: 0, score: "18"
        score = int(score)

        # if int(score) <= 18:
        #     items[idx] = int(score) + 2
        # else:
        #     items[idx] = int(score)
        
        if score <= 18:
            score += 2
           
        items[idx] = str(score).center(10)
    
    # items: ["     19     ", "     19     "]
    # *items: "     19     ", "     19     "
    # [ *items ]
    # [   "     19     ", "     19     "     ]
    # -----------------
    # solution 1
    # a = [*items] => ["     19     ", "     19     "]
    # a = [items] => [ ["     19     ", "     19     "]  ]
    # solution 2
    # a = []
    # a.extend(items)
    # -----------------
    # unpacking
    # [name.center(20), *items]
    # ["       sabour      ", "     19     ", "     19     "]
    # [name.center(20), items]
    # ["       sabour      ", ["     19     ", "     19     "]]
    # [name.center(20), *items]
    # ["       sabour      ", "     19     ", "     19     "]
    my_list.append(f'|{"|".join([name.center(20), *items])}|')
    # ["       sabour      ", "     19     ", "     19     "]
    # "       sabour      |     19     |     19     "
    # items: [20, 19, 19]

for item in my_list:
    print("-" * 44)
    print(item)

    
"""
20
"    20    "
"    20    "

  20         10     10 
-------------------------
| Name    | Art  | Math |
-------------------------
| Mohseni |  20  |  20  |
-------------------------
| Mobin   |  20  |  20  |
-------------------------
| Sabour  |  20  |  20  |
-------------------------
"""







