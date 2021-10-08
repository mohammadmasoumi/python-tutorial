import random

# filter and break and continue

a_list = ["apple", "orange", "peach"]

for item in a_list:
    if item == "orange":
        # break  # break
        continue  # skip
    # else:
    #     print(item)
    # print(item)

# --------------------------------------------------
# filter
your_list = []
for idx in range(20):
    # your_list[idx] = idx % 10
    your_list.append(random.randint(0, 1))


def skip_zeros(item):
    if item != 0:
        return item

    # return None


# --------------------------------------------------
# print(your_list)
# print(list(filter(skip_zeros, your_list)))

# در زمانی که روی یک لیست می چرخید دقت کنید که اگر همان لیست را تغییر دهید ممنکن است نتایج دلخواه رو مشاهده نکنید.
# مثل عمل pop remove
my_list2 = [0, 1, 0, 1, 0, 0, 1]
temp_list = []
print(my_list2)

for idx, item in enumerate(my_list2):
    # if item != 0:
    #     temp_list.append(item)
    print(idx, len(my_list2))
    if item == 0:
        my_list2.remove(item)
        # my_list2.pop(idx)

# my_list2 = temp_list
print(my_list2)

# for functionality

# our_list = [5, 4, 3, 2, 1, 0]
# counter = 0
# for item in our_list:
#     elem = our_list.pop()
#     print(elem, counter, len(our_list))
#     counter += 1


# append
print("---------------------------------------------")
# infinitive loop
from time import sleep

their_list = [1, 2]
for idx, item in enumerate(their_list):
    print(idx, item, len(their_list))
    sleep(1)
    # sleep(0.1)
    their_list.append(idx)
