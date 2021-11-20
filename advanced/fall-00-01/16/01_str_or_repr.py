# from datetime import datetime
# from datetime.datetime import datetime
import datetime

# class Obj:
#
#     def __str__(self):
#         # informal representation
#         return "Python1"
#
#     def __repr__(self):
#         # formal representation
#         return


# obj = Obj()
# a = 10
# print(obj)
# print(repr(obj))
# b = eval(repr(obj))

# evaluation
# eval("print('Hello')")
# print(eval(repr(obj)))

# file_name.class_name.behaviour
d1 = datetime.datetime.utcnow()
# d1 = datetime.utcnow()

print(str(d1))
print(repr(d1))

d2 = eval(repr(d1))
print(d2)
