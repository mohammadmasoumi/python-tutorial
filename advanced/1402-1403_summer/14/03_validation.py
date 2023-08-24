import inspect

data = {
    'age': 22,
    'name': 'asghar',
    'city': 'New Varamin'
}


class MyValidator:

    def __init__(self, name, logger):
        self.name = name
        self.logger = logger

    def validate_age(self, age):
        return age

    def validate_name(self, name):
        return '(Mr/Mrs/Miss)' + name

    def validate_city(self, city):
        return city

    def __call__(self, data):
        validated_data = {}
        for name, method in inspect.getmembers(self):
            if name.startswith('validate_'):  # name: validate_age
                key = name[len('validate_'):]  # key: age
                validated_value = method(data.get(key))  # validate_age(22)
                validated_data[key] = validated_value

        return validated_data


# instace
# MyValidator("my-validator", "")
# instance(data)
print(MyValidator("my-validator", "")(data))
