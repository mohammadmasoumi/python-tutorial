names = ["hassan","asghar", "mina"]
grades = [10, 20, 19.9, 15.2]


def my_zip(a, b):
    # merged_list = []
    # min_len = len(b) 
    # if len(a) < len(b):
    #     min_len = len(a)
    # for idx in range(min_len):
    #     merged_list.append((a[idx], b[idx]))
    # return merged_list
    return [(a[idx], b[idx]) for idx in range(min(len(a), len(b)))] 
    
print(my_zip(names, grades))