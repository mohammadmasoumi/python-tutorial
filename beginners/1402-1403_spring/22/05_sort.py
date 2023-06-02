"""
my_list: [-1, 1, 49, 50, 51]
scores:  [51, 49, 1, 0, 1] -> sort_base_on(-1)
item_scores: [(-1, 51), (1, 49), (49, 1), (50, 0), (51, 1)]
sorted_scores: [(50, 0), (49, 1), (51, 1), (1, 49), (-1, 51)]
sorted: [50, 49, 51, 1, -1]
"""
my_list = [-1, 1, 49, 50, 51]

"""
[50, 49, 51, 1, -1]

k= 50
[49, 50, 51, 1, -1]
[49, 1, 51, 50, -1]
[49, 1, 51, -1, 50]
k=1
...
[1, 49 , 51, -1, 50]
[-1, 49 , 51, 1, 50]
...
k=51

"""


def sort_base_on(item):
    return abs(item-50)


def sort(iterable, *, key):
    def sort_me(li):
        # li = item_scores
        # [(-1, 51), (1, 49), (49, 1), (50, 0), (51, 1)]
        for i in range(len(li)):
            for j in range(len(li)):
                if li[i][1] < li[j][1]:
                    li[i], li[j] = li[j], li[i]

    item_scores = [(item, key(item)) for item in iterable]
    sort_me(item_scores)

    return [item[0] for item in item_scores]


print(sort(my_list, key=sort_base_on))
