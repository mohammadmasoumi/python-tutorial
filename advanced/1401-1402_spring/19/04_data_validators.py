# key: []
# age: ["age must". "value of"]
errors = {

}

class BaseValidation:

    def type_validation(self, expected_type):
        if not isinstance(value, expected_type):
            key_errors = errors.get(self.key, [])
            key_errors.append(TypeError(f"value of `{self.key}` must be {expected_type}, got {type(value)}"))
            errors[self.key] = key_errors
            return False

        return True


class AgeValidate(BaseValidation):
    key = "age"

    def __init__(self, data):
        self.data = data

    def __call__(self, *args, **kwargs):
        value = self.data.get(self.key)

        if not self.type_validation(int):
            pass
        elif not (0 < value < 121):
            key_errors = errors.get(self.key, [])
            key_errors.append(ValueError("age must be between (1, 120)"))
            errors[self.key] = key_errors


class GradeValidate(BaseValidation):
    key = "grade"

    def __init__(self, data):
        self.data = data

    def __call__(self, *args, **kwargs):
        value = self.data.get(self.key)

        if not self.type_validation(int):
            pass
        elif not (-1 < value < 21):
            key_errors = errors.get(self.key, [])
            key_errors.append(ValueError("grade must be between (0, 20)"))
            errors[self.key] = key_errors


my_data = {
    "age": "ali", 
    "grade": 121
}

validators = [
    AgeValidate(data=my_data), 
    GradeValidate(data=my_data),
]

for validator in validators:
    validator()

print(errors)