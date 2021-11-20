# logical operator


"""
and
or
not

AND

bool = [] and []

True = [true] and [true]
False = [false] and [true]
False = [true] and [false]
False = [false] and [false]

OR یا
True = [true] or [true]
True = [true] or [false]
True = [false] or [true]
False = [false] or [false]

math_score = 20
physics_score = 19

True = math_score == 20 or physics_score == 20
score

score >= 0 and score <= 20
0 <= score <= 20
"""

"""

or => True
and => False
"""

math_score = 20
physics_score = 19
art_score = 12

# print(math_score == 20 and physics_score == 20 and art_score == 20 and [] and [] and [])
# اگر حداقل یکی از شرط های غلط باشد نتیجه نهایی غلط است

print(math_score == 20 and physics_score == 20 and art_score == 20)
# print(True and False and False)
# print(False and False)
# print(False)


# اگر حداقل یکی از شرط ها درست باشد نتیجه نهایی درست است.
print(math_score == 20 or physics_score == 20 or art_score == 20)
# print(True or False)
# print(True)


# ----------------------------------

"""
Bitwise

| or
& and
^ xor
~ not
"""

"""
OR - MAX

7 =   (111)
5 = | (101)
____________
       111 -> 10 -> 7   

AND - MIN
7 =   (111)
5 = & (101)
____________
       101 -> 10 -> 5

XOR
اگر تعداد 1 ها فرد باید خروجی 1 میشود.
     a   b   res
    ____________
     1   1    0
     1   0    1
     0   1    1
     0   0    0
     
     a   b   c   res
    ________________
     1   1   1    1
     1   1   0    0
     1   0   1    0
     1   0   0    1
     0   0   0    0
     0   0   1    1
     0   1   0    1
     

7 =   (111)
5 = ^ (101)
____________
        010 -> 10 -> 2

12 =  (1100)
7 = ^ (0111)
____________
       1011 -> 10 -> 11 

NOT 
1  -> 0
0  -> 1


"""

print(7 | 5)
print(7 & 5)
print(7 ^ 5)
print(~0)

print("a \t b")
print("a \tb")
print("a\t b")
print("a\tb")
