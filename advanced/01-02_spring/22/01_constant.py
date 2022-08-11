# https://docs.python.org/3/library/enum.html

# DIRECTION
"""
1. hard to change
2. memory efficiency
3. easy to make mistake
4. easy to forget values
"""

def move1(direction):
    # 1
    convention = {
        "راست" : "right"
    }
    direction = convention.get(direction, direction)

    # 2
    if direction == "راست":
        pass

    if direction == "right":
        pass

    elif direction == "lef":
        pass


move1("right")
move1("asghar")
move1("راست")
move1("up")
move1("EAST")
move1("WEST")


# constant - convention
RIGHT = "راست" # right
LEFT = "left" # no momery efficiency
UP = 3 # "up"
DOWN = "down"

# 
IS_ALIVE = "YES"
IS_ALIVE = True

# const String RIGHT = "right"
# final Int RIGHT
# RIGHT = 1

def move2(direction):
    if direction == RIGHT:
        pass
    elif direction == LEFT:
        pass


move2("up")
move2(3)



# f"""
# Hello james,
# how are you james?
# Goodbye Tom.
# """

# f"""
# Hello asghar,
# how are you asghar?
# Goodbye Tom.
# """
# name = "asghar"

# f"""
# Hello {name},
# how are you {name}?
# Goodbye Tom.
# """