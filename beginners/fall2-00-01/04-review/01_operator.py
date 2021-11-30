# operator


"""
logical operator

and
or
not


AND

 [True] and [True] => True
 [True] and [False] => False
 [False] and [True] => False   اکر اولی غلط باشد دومی را اصلا اجرا نمیکند.
 [False] and [False]  => False


OR
 [True] or [True] => True در صورتی اولی درست باشد دومی را بررسی نمیکند
 [True] or [False] => True
 [False] or [True] => True
 [False] or [False]  => False


NOT

not [True] => False
not [False] => True

not (True and False) => True
not (True and False and ...) => True
not ((True and False) or (False and False)) => True


12 and 13 => bool(12) and bool(13) => True
condition => boolean
_________________________
likewise
bitwise operator


& and
| or
^ xor
~ not


***********************************
12 & 7 =>

12 =>   1100
7  => & 0111
_____________
        0100 => 4

5 =>   101
7 => & 111
___________
     101

***********************************
12 | 7 =>
12 =>   1100
7  => | 0111
_____________
        1111 => 15

5 =>   101
7 => | 111
___________
       111
***********************************
تعداد یک ها فرد باشهد => یک میشود
12 | 7 =>
12 =>   1100
7  => ^ 0111
_____________
        1011 => 11

5 =>   101
7 => ^ 111
___________
       010 => 2

***********************************
~  0 => 1
   1 => 0

"""

# one's compliment and two's compliment
# 0000
# 1111


"""
one's compliment 

sign
1 0001

two's compliment  = one's compliment + 1 


1111 =>~(1111) =>  0000 one's compliment 
15 => 0


 0000 0101
        1 
 1111 1010 one's compliment
+        1
____________
 1111 1101 -5
 


__________________________
Overflow


  positive number
+ positive number
_______________
  negative
  
  

00001000 +8

0000 1000
__________ invert - flip 0->1, 1->0
1111 0111 -8 one's compliment

      111
 1111 0111
+        1
___________
  1111 1000 (-8) two's compliment


___________________________________
___________________________________
___________________________________
NOT OVERFLOW

 (+3)   0000 0011
+(−8)   1111 1000
___________________
        1111 1011  two's compliment
        
1111 1011 - flip
_________
0000 0100

 0000 0100 
+        1
___________
  0000 0101  => -5
  
____________________________
____________________________
____________________________
 (−7)   1001
+(−6)   1010
______________
        10011 two's compliment

10011 -> flip
01100

 01100
+    1
_______
 01101  -> -13 

____________________________
____________________________
____________________________


  0100
+ 0101
_______
  1001  two's compliment - negative
  
1001 - flip
______
0110

 0110
+   1
_______
  0111 -> (-7) 


0001
1110

 1110
+   1
______
 1111 -> 15

"""

print(~0)
print(5 | 7)
print(5 & 7)
print(5 ^ 7)
