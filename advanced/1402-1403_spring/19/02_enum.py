
class MyEnum:
    
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls, *args, **kwargs)

        members = []
        props = [prop for prop in dir(self) if not (prop.startswith('__') or prop.endswith('__'))]

        for prop in props:
            # 'RIGHT', 'LEFT'
            members.append((prop, getattr(cls, prop)))

        print(members)

        return self

    def __iter__(self):
        return  self

    def __next__(self):
        return next()
        # pass

class Direction(MyEnum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    # prop = 1
    # props = 10

d = Direction()


# iter(direction) ==> __iter__

# WRONG
# direction = Direction()
# for item in direction:
#     pass