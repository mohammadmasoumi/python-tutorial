
class ValidationData:

    def __init__(self, ignore):
        self.ignore = ignore

    # def validate(self, data):
    #     pass

    def __call__(self, *args, **kwargs):
        pass


class ValidationUser:

    def __init__(self, db_connection):
        self.db = db_connection

    # def validate(self, data):
    #     pass

    def __call__(self, *args, **kwargs):
        pass


# settings.py
validation_classes = []
#                   instance        instance
validators = [ValidationData(ignore=True), ValidationUser(db="")]
# validators = [ValidationData, ValidationUser]


class A:
    pass


class B:
    pass


class C:
    pass


clss = [A, B, C]

for c in clss:
    instance = c()
    print(instance)
