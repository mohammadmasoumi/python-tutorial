from time import sleep

n = int(input())
path = input()

jumps = 0
current_cloud = 0

while current_cloud < len(path) - 1:
    if current_cloud + 2 < len(path) and not int(path[current_cloud + 2]):
        current_cloud += 2
        jumps += 1

    elif current_cloud + 1 < len(path) and not int(path[current_cloud + 1]):
        current_cloud += 1
        jumps += 1

print(jumps)
