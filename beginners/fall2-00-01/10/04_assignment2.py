"""
سوال دوم:

لیست زیر به شما داده است.

لطفا به همه المان های این لیست مقدار "orange" را اضافه کنید.

my_list = [["apple", "apricat"], ["watermelon", "cucumber"], ["cherry", "pomegranate"]]

نمونه خروجی:
my_list = [["apple", "apricat", "orange"], ["watermelon", "cucumber", "orange"], ["cherry", "pomegranate", "orange"]]
"""

my_list = [["apple", "apricot"], ["watermelon", "banana"]]


# best solution
for item in my_list:

    # item is a list
    # mutable

    # ["apple", "apricot", "orange"]
    item.append("orange")

    # ["orange", "apple", "apricot"]
    # item.insert(0, "orange")

    # ["apple", "orange", "apricot"]
    # item.insert(1, "orange")


# another solution
for index, item in enumerate(my_list):

    # ["orange", "apple", "apricot"]
    # y_list[index] = ["orange"] + item

    # ["apple", "apricot", "orange"]
    # my_list[index] = item + ["orange"] 

    # ["apple", "orange", "apricot"]
    my_list[index] = item[:1] + ["orange"] + item[1:]

    
print(my_list)