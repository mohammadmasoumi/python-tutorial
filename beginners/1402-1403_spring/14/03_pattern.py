"""
1.
*

2.
*
** 

3.
*
**
***
"""
n = int(input())

# list(range(3)) [0,1,2]
# generate index
for idx in range(n): # sequence [start:end:step]
    print("*" * (idx + 1))

for idx in range(n):
    print(("*" * (idx + 1)).rjust(n))
    
for idx in range(n):
    # "*" + "*" => "**" => [1:]
    # "**" + "**" => "****" => "***"
    print(("*" * (idx + 1)).rjust(n) + ("*" * (idx + 1))[1:])