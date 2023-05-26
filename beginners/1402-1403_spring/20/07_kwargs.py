# dict packing
#
#              **asghar
#       keyword arguments
def register(**kwargs):
    # **kwargs: name='asghar', grade=10, age=100
    # kwargs: {'name': 'asghar', 'grade': 10, 'age': 100}
    print(kwargs)
    # print(asghar)


#       key value
register(name='asghar', grade=10, age=100)
register(name='MrEskandari', grade=19.5, age=18, height=178)
