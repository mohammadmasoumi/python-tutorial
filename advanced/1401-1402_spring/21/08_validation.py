
data = {
    "age": "20",
    "gender": "male"
}


class Valiator:

    def __init__(self, data):
        self.data = data

    def age_validator(self, age):
        if not isinstance(age, int):
            raise TypeError(f"expect int, got {type(age)}")

    def gender_validator(self, gender):
        pass

    def validate(self):
        # filter(lambda x: x.endswith("_validator"), dir(self))
        # ["age_validator", "gender_validator"]
        for func_name in filter(lambda x: x.endswith("_validator"), dir(self)):
            # func = self.age_validator
            func = getattr(self, func_name)
            key = func_name.replace("_validator", "")
            func(self.data.get(key))


Valiator(data=data).validate()