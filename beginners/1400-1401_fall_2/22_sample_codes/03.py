
def my_reverse(string):
    reversed_string = ""
    
    for idx in range(len(string)):
        reversed_string += string[len(string) - idx - 1]

    return reversed_string

print(my_reverse("hello"))