def update(*args, **kwargs):
    print(f"args: {args}, type(args): {type(args)}")
    print(f"kwargs: {kwargs}, type(kwargs): {type(kwargs)}")
    print("-------------------------------------")

update(12, 13)
update(a=14, b=15)
update(12, 13, a=14, b=15)