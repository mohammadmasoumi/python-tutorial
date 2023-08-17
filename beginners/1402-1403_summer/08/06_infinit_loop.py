import time
import sys

my_list = [1, 2, 3, 4]
for item in my_list:
    time.sleep(0.1)
    # sys.exit()
    my_list.append(item)
    print(len(my_list), my_list)

print(my_list)