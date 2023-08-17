# all 
# any

"""
# built-in function
int
print
input
type
ord
chr
id
sum
max
min

# reserved keyword
for 
if else elif
from 
import 

# string
"".format()
"".split()

syntax
r""
f""
"""
# def any(__iterable: Iterable[object]) -> bool:
"""
Return True if bool(x) is True for any x in the iterable.
If the iterable is empty, return False.
"""
print(any([1, 0, 11, 10])) # bool(1), bool(0), bool(11), bool(10)
print(any([0.0, 0, "", []])) # bool(0.0), bool(0), bool(""), bool([])

"""
Return True if bool(x) is True for all values x in the iterable.

If the iterable is empty, return True.
"""
# and -> all(conditions)
# or -> any(conditions)
print(all([1, 2, 3]))
print(all([1, 0, 1])) 