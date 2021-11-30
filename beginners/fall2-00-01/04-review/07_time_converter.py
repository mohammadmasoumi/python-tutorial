"""
Comments

60 hours

----------------------
hours => minutes
1     => 60   1 * 60
2     => 120  2 * 60


hours => minutes => seconds

----------------------
hours => seconds
1     => 3600 1 * 3600 (60 * 50)
2     => 7200 2 * 3600
3     => ?    3 * 3600

minutes
seconds
"""

# single-line comment - hash-tag
# multiline comment - three double quotes

"""""
comment line 1
comment line 2
comment line 3
"""""

hours = int(input())

minutes = hours * 60
seconds = minutes * 60
# seconds = hours * 3600

print(f"hours to minutes: {minutes} min")
print(f"hours to seconds: {seconds} sec")
