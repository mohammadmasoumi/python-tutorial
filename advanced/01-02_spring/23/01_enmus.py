from enum import Enum

# direction - constant
RIGHT = "right"
LEFT = "left"


class Color(Enum):
    RED = 1 # object (name, value) 
    GREEN = 2 # 
    BLUE = 3

    # RED = Color() # .name, ,value

print(Color.RED) # 
print(Color.RED.name)
print(Color.RED.value)

for color in Color:
    print(color)