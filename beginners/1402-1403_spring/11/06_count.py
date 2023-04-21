#         0123456789
string = "helloworld"
#                  -1
#        -10

#                     start end
print(string.count("d", 4, 9)) # 0, end is not included
print(string.count("d", 4, 20)) # 1, you are allowed use indexes out of index range 
print(string.count("o", 4, 4)) # 0
print(string.count("o", 4, 5))
print(string.count("w", 4, 5))
print(string.count("l", -10, 5))
print(string.count("l", -10, -5))
print(string.count("h", 0, -10))
print(string[-10:5])

string = " hello world  "
print(string.count(" ")) # space is a character
print(string.count(" ", 100, 200))
print(string.count(" ", 4, 2)) # string[4:2] => "".count(" ")
