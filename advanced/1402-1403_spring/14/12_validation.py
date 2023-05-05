
class Validation:

    def validate_name(self, name):
        pass

    def validate_age(self, age):
        pass

    def __call__(self, data):
        pass


ValidationClass = Validation()
ValidationClass(data={})
