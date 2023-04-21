# chr ord

# 'A' -> 65
print(ord('A'))
print(chr(65))
print(ord(chr(65)))

"""
Application ?:
    - check english alphabetic
    - uppercase or lowercase
    - string comparison ali[greater], Ali
    - "12" -> 12
        s = 0

        "0", "1", "2", ...
        for char in "12":
            #  22       21
            num = ord(char) - ord("0")
    - mapping characters to numbers and vise versa
    - ... 
    
"""

number = "2134"
# number = 1234
# print(int(number))

"""
a 97
b 98
c 99

A 65
B 66

"0" 20
"1" 21
"2" 22 -> ord("2") - ord("0") -> 22 - 20 = 2
"""

