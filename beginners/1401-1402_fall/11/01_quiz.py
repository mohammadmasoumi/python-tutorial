"""
# Input
3
Ali Art:20 PE:20 20
Hassan Math:20 19 18
Asghar 20 19 10


Ali 
3 
Art:20 
PE:20 
Math:20

Ali 
4
Art:20 
PE:20 
Math:20

# Output
---------------------------------------------------
| Name    | Math    | Art     | PE      | AVG     |
---------------------------------------------------
| Ali     | 20      | 20      | 20      | 20      |
---------------------------------------------------
| Ali     | 20      | 20      | 20      | 20      |
---------------------------------------------------
| Ali     | 20      | 20      | 20      | 20      |
---------------------------------------------------
"""

# n = int(input())

# counter = 0
# while counter < n:
#     counter += 1

"""
[[name, scores, avg], [], [], []]
"""
data = []

for _ in range(int(input())):
    # items: ["Ali", "20", "20", "20"]
    # name, scores
    name, *scores = input().split()

    sum_of_scores = 0
    for score in scores:
        sum_of_scores += int(score)

    # [name, *scores, sum_of_scores // len(scores)]
    # data: [["Ali", "20", "20", "20", 20]]

    # [name, scores, sum_of_scores // len(scores)]
    # data: [["Ali", ["20", "20", "20"], 20]]
    data.append([name, *scores, f"{sum_of_scores / len(scores): .2f}"])

# Name------------|
# | Name    | Math    | Art     | PE      | AVG     |
columns = ["Name", "Math", "Art", "PE", "AVG"]

# new_columns = ["Name     ", "Math      ", "Art        ", "PE         ", "AVG       "]
new_columns = []
for col in columns:
    new_columns.append(col.ljust(10))

print("-" * 56)
print("|" + "|".join(new_columns) + "|")
print("-" * 56)

for item in data:
    # item: ["Ali", "20", "20", "20", "20"]
    new_item = []

    for d in item:
        new_item.append(d.ljust(10))

    print("|" + "|".join(new_item) + "|")
    print("-" * 56)
