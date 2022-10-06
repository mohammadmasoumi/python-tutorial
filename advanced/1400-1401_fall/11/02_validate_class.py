class Validate:

    # method
    def validate_a(self, a_value):
        # data.get("a")
        if not isinstance(a_value, list):
            raise ValueError("a should list")
        # print(f"validate_a called with {a}!")

    # method
    def validate_b(self, b_value):
        pass
        # print(f"validate_b called with {b}!")


v = Validate()
# data = {"a": 1, "b": 2}
data = {"a": [1, 2, 3], "b": 2}

# print(dir(v))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'validate_a', 'validate_b']
method_names = [item for item in dir(v) if item.startswith("validate_")]

# print("mohammad"[2:3])
#  ['validate_a', 'validate_b']
for method_name in method_names:
    # method_name => "validate_b"
    method = getattr(v, method_name)

    # {"a": 1}
    attr_name = method_name[len("validate_"):]
    attr_value = data.get(attr_name)

    #
    if attr_value:
        method(attr_value)
