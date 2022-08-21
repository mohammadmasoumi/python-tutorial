# 3.10
direction = "right"

if direction == "right":
    pass
elif direction == "left":
    pass
elif direction == "up":
    pass
elif direction == "down":
    pass

match direction:
    case "right":
        print("Right")
    case "left":
        print("Left")
    case "up":
        print("Up")
    case "down":
        print("Down")

number = 10
match number:
    case "right" | "left":
        print("Right")
    case "left":
        print("Left")
    case "up":
        print("Up")
    case "down":
        print("Down")
    case _:
        print("Nothing")


def alarm(item):
    match item:
        case [time, action]:
            print(f'Good {time}! It is time to {action}!')
        case [time, *actions]:
            print('Good morning!')
            for action in actions:
                print(f'It is time to {action}!')

alarm(['afternoon', 'work'])
alarm(('morning', 'have breakfast', 'brush teeth', 'work'))
