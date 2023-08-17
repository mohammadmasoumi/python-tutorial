# 12 13 14

n = input() # "12" 

print(n, type(n)) # "12 13 14"
# "12 13 14"
# ["12", "13", "14"]
# [12, 13, 14]

# "12 13 14".split(" ") default: " "
# ["12", "13", "14"]
# "ali|20|20|19"
# ["ali" "20" "20" "19"]
print(n.split())

result = n.split() # ["ali", "20", "20", "19"]
scores = result[1:] # ["20", "20", "19"]
# map, filter

#                   range(len(scores))
for idx, score in enumerate(scores):
    # idx: 0, score: "20"
    # scores[0] = 20
    scores[idx] = int(score)
