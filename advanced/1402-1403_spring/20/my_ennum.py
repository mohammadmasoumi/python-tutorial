def is_cls_prop(prop):
    return prop.startswith('__') or prop.endswith('__') or \
        prop.startswith('_') or prop.endswith('_')


class Member:

    def __init__(self, name, value):
        self.name = name
        self.value = value


class MetaEnum(type):

    def __iter__(cls):
        return iter(cls._members__[name] for name in cls._names__)

    def __new__(metacls, cls, bases, classdict, **kwds):
        metaclass = super().__new__(metacls, cls,  bases, classdict, **kwds)
        metaclass._members__ = {}
        metaclass._names__ = []

        dynamic_attributes = {
            k: v for c in metaclass.mro() for k, v in c.__dict__.items()
            if not is_cls_prop(k)
        }

        for k, v in dynamic_attributes.items():
            member = Member(name=k, value=v)
            setattr(metaclass, k, member)

            metaclass._members__[k] = member
            metaclass._names__.append(k)

        return metaclass


class MyEnum(metaclass=MetaEnum):
    def __new__(cls, *args, **kwargs):
        print("Called MyEnum")
        instance = super().__new__(cls, *args, **kwargs)
        return instance
