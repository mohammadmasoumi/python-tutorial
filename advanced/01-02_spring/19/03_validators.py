
class ValidatorKey1:
    key = "key1"
    
    def __init__(self, data):
        self.data = data

    def __call__(self, *args, **kwargs):

        # kwargs : {"key": "key1"}
        key = kwargs.get("key") # key1
        value = self.data.get(key)

        print(f"args: {args}, kwargs: {kwargs}, key: {key}, value: {value}")

        if not isinstance(value, str):
            raise ValueError(f"Expected str, got {type(value)}")
        

class ValidatorKey2:

    def __init__(self, data):
        self.data = data


    def __call__(self, *args, **kwargs):

        print()


class ValidatorKey3:
    
    def __init__(self, data):
        self.data = data


    def __call__(self, *args, **kwargs):

        print()


my_data = {
    "key1": 2,
    "key2": 2, 
    "key3": True
}

validators = [
    ValidatorKey1(data=my_data),   # instance
    # ValidatorKey2(data=my_data),  # instance
    # ValidatorKey3(data=my_data),  # instance
]

keys = list(my_data.keys())
for idx, validator in enumerate(validators):
    validator(key=keys[idx])