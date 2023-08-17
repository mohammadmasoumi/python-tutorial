"""
jump ?
pos ?  
          O
clouds = [1, 1, 0, 1, 1, 0, 1, 1]

             O
clouds = [1, 1, 0, 1, 1, 0, 1, 1]

                   O
clouds = [1, 1, 0, 1, 1, 0, 1, 1]

                      O
clouds = [1, 1, 0, 1, 1, 0, 1, 1]

                            O
clouds = [1, 1, 0, 1, 1, 0, 1, 1]

                               O       O index out of range
clouds = [1, 1, 0, 1, 1, 0, 1, 1]
"""

clouds = [1, 1, 0, 1, 1, 0, 1, 1]
pos = 0
jump = 0 

# len(clouds): 8
# pos: 7
# pos: 2
# pos+2: 4
# update
# clouds[pos] = clouds[pos+2]

#           0  1  2  3  4  5  6  7
# clouds = [1, 1, 0, 1, 1, 0, 1, 1]
# pos: 0, len(clouds): 8
# while pos < len(clouds): 
#     # pos: 7, jump: 5, len(clouds): 8
#     if pos+2 < len(clouds) and clouds[pos+2] == 1:
#         pos += 2
#         jump += 1
    
#     elif pos+1 < len(clouds) and clouds[pos+1] == 1:
#         pos += 1
#         jump += 1
#     else:
#         break

while pos < len(clouds) - 1: 
    # pos: 7, jump: 5, len(clouds): 8
    if pos+2 < len(clouds) and clouds[pos+2] == 1:
        pos += 2
        jump += 1
    else:
        pos += 1
        jump += 1

print(f"jump: {jump}")