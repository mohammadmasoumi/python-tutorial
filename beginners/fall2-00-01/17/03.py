# assignment

my_dict = {"a": 1, "b": 2, 30: 1, "a": False}

# 1
if "a" in my_dict:
    print("i found a")
else:
    print("Where is a?")

# 2
# be careful!
# if False
if my_dict.get("a"):
    print("i found a")
else:
    print("Where is a?")