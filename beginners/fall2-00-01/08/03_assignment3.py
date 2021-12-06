"""
input: "hello-world-salam-bye-hello"
output: "hello*world*salam*bye*hello"
"""
# ctrl + / => uncomment / comment

# solution 1

# my_input = input().split("-")
# # my_input: list
# # my_input.split() ??? raise exception
# # print("item1", "item2", sep="*") =? item1*item2
#
# print(my_input, sep="*")
# print(my_input, my_input, sep="*")
#
# # print('hello', 'world', 'salam', 'bye', 'hello', sep="*")
# # * => unpacking
# print(*my_input, sep="|")

# solution 2

# my_input = input()
# print(my_input.replace("-", "*"))

# solution 3
# my_input = input().split("-")
#
# acc = ""
# # ["hello", "world", "salam", "bye", "hello"]
# # [GOAL]: hello*world*salam*bye*hello*
# # string concatenation
# for word in my_input:
#     acc += (word + "*")
#
# print(acc)

# solution 4
# join
my_input = input().split("-")
print("*".join(my_input))
