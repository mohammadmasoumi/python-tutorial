

def change_list(iterable):

    return [item * 2 if item % 2 else item // 2 for item in iterable]

print(change_list([1, 2, 3 ,4]))