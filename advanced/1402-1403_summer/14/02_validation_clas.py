import inspect

"""
data = {
    'age': 22,
    'name': 'asghar',
    'city': 'New Varamin'
}

"""


class A:

    def validate_age(self, age):
        pass

    def validate_a(self, data):
        pass

    def validate_b(self, data):
        pass

    def validate_c(self, data):
        pass


a = A()
validator_functions = []
for name, method in inspect.getmembers(a):
    if name.startswith('validate_'):
        validator_functions.append(method)
        # print(name, method)

data = {'key': 1, 'value': 2}
for validate_method in validator_functions:
    validate_method(data)
