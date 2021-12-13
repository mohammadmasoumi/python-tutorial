
# assignment1
# first solution

"""
سوال اول :

لیست زیر به شما داده شده است.

لطفا به اول همه المان های این لیست مقدار " Hello" رو اضافه کنید و مقدار نهایی رو در خروجی چاپ کنید.
my_list = ["Ali", "Hassan", "Fatemeh", "Asghar"]

نمونه خروجی:
["Hello Ali", "Hello Hassan", "Hello Fatemeh", "Hello Asghar"]
"""

my_list = ["Ali", "Hassan", "Fatemeh", "Asghar"]


"""
What should I do?
Where should I start?

# general ideas
1. write down the final answer
2. approach to get the final answer

# 
1. I should change each element of `my_list` 
2. First I should meet each element of `my_list`
3. Then I should add `"Hello "` to the each element of `my_list`
4. Update that item in `my_list`. index is needed!
5. Check each elements of `my_list` is whether `MUTABLE` or `IMMUTABLE`
6. Print final result
"""

index = 0

# 1. 2. use for
for word in my_list:
    
    # 3. update element
    word = "Hello " + word

    # 4. update element of list 
    my_list[index] = word

    # update index
    index += 1


# 6. print final result
print(my_list)