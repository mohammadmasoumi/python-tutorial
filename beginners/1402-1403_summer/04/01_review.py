
print("ab")
# "ab" + "\n" => "ab\n"

print("a",                           "b", "c")  # sep: " ", "a b c" + "\n"

"""
print("ab") # "ab\n"
print("abc", end="") # "abc"
print("abcd") # "abcd\n"

__________________
ab
abcabcd 
 
^ 
pointer, cursor
__________________
"""

# -------------------
# logical operator vs bitwise operator

"""
# logical operator
and or not

conditions

# bitwise operator

& | ^ ~

5 & 7

5 => 101
7 => 111

10 -> 2 -> 10

    101 => 5
  & 111 => 7
  _____
    101 => 5

AND
1 and 1 = 1
1 and 0 = 0
0 and 1 = 0
0 and 0 = 0

OR 
1 or 1 = 1
1 or 0 = 1
0 or 1 = 1
0 or 0 = 0

    101 => 5
  | 111 => 7
  _____
    111 => 7
    
2'complement
https://en.wikipedia.org/wiki/Two%27s_complement


not

~5 => ~101 => 010 => 2

"""

print(~5)  # 00000101 => 11111010 + 1 => 11111011 => 00000100 => ...
