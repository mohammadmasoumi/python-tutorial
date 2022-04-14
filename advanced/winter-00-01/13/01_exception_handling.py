

# exception handlign 

"""
keywords
try
except
else
finally
"""

"""
1. 
raise exception 
except block
finally block

2. 
raise exception
except block
re-catch except
finally block
re-raise except 
"""

# print(int("Hassan"))
try:
    a = input() # "ali"
    print(int(a)) # int("ali") -> raise ecxception
    # open()
    # mongo()
except ValueError as e:
    print(f"except: {e}")
    raise e
else:
    print(f"else: {a}")
finally: 
    # 
    print("I am in the finally!")
