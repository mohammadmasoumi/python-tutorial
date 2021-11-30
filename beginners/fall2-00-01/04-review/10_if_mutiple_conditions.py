"""
math
science
art

________________________

art 20, math 20, science 20 => Bravo!


اگر همه نمراتش 20 نبود
art 19, math 19, science 19 => no Bravo!
"""

math_score = int(input("Enter math score: "))
science_score = int(input("Enter science score: "))
art_score = int(input("Enter art score: "))

# debug
# debugger
print(f"math_score: {math_score}")
print(f"science_score: {science_score}")
print(f"art_score: {art_score}")

if math_score == 20 and science_score == 20 and art_score == 20:
    print("Bravo!")

# اکر هیچ کدوم از درس هایش 20 نبود
# if math_score < 20 and science_score < 20 and art_score < 20:

# اگر حداقل یکی از درس هایش 20 نباشد
# if math_score < 20 or science_score < 20 or art_score < 20:

"""
math_score: 20 
science_score: 20 
art_score: 19

math_score != 20 or science_score != 20 or art_score != 20
False or False or True
False or True
True
"""

if math_score != 20 or science_score != 20 or art_score != 20:
    print("no Bravo!")

"""
math_score: 20 
science_score: 20 
art_score: 19

not (math_score == 20 and science_score == 20 and art_score == 20)
not (True and True and False)
not (True and False)
not (False)
True
"""
if not (math_score == 20 and science_score == 20 and art_score == 20):
    print("no Bravo!")
