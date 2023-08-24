# Validation class

from settings import validators

data = {}
# validator: cls
for validator in validators:
    # instance()
    # validator(data=data)
    # validator.validate(data=data)

    # instantiation like
    validator(data=data)
    # validator.valid()


# A = type()
# class A:
#     pass
# a = A()  # call __call__ on type
