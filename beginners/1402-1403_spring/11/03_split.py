string = "2helloworld2"

"""
"2helloworld2"
"" "helloworld2"
["", "helloworld", ""]
"""

print(string.split("2"))

string = "h**el**lo"

# "h||el||lo"
# ["h", "", "el", "", "lo"]
print(string.split("*"))

string = "h****el****lo"
# ['h', '', '', '', 'el', '', '', '', 'lo']
print(string.split("*"))

string = "h****el****lo"

# ['h', '', 'el', '', 'lo']
print(string.split("**"))

string = "h****el****lo"

# ['h', '*el', '*lo']
# "h*el*lo"
print(string.split("***"))

# SyntaxError: invalid decimal literal
# print(12.split())

# string = "123456"
# string.split("") ValueError: empty separator
# print(string.split(""))

string = "123456"
print(list(string))