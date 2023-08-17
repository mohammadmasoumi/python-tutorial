scores = [20, 20, 20, 19]

# map, any, all
print(all(scores))

# map(function, iterable)
# print(map(all, scores)) # for each item in scores -> all(item) 

# all([True, True, True, False]) -> False
print(all(map(lambda score: score == 20, scores)))
print(any(map(lambda score: score == 20, scores)))
print(all(map(lambda score: score != 20, scores)))

# scores = [[20], [20], [20], [20]]
# result = []
# for score in scores:
#     # all(iterable)
#     # all(int) -> WRONG
#     result.append(all(score))

# print(map(all(scores)))

print(
    all( # result: [True, True, True, False]
        map(
            lambda score: score == 20, 
            scores # [20, 20, 20, 19]
        )
    )
)


