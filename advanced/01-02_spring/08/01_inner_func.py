def avg_list_items(list_items):
    # items: [[], [], []]

    def get_avg(items):
        return sum(items) / len(items)

    avgs = []
    for items in list_items:
        # items: [1, 2] 
        # items: [3, 4]
        avgs.append(get_avg(items))

    return avgs

print(avg_list_items([[1, 2], [3, 4]]))
