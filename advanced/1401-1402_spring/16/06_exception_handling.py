class AsgharException(BaseException):
    
    def __init__(self, code, desc):
        self.code = code
        self.desc = desc

        super().__init__()

    def __str__(self):
        return f"desc: {self.desc}, code: {self.code}"


class MyInt(int):

    def __truediv__(self, x):
        if x == 0:
            raise AsgharException(code=400, desc="ZeroDevision!")

        return super().__truediv__(x)

    def __floordiv__(self, x):
        if x == 0:
            raise AsgharException(code=400, desc="ZeroDevision!")

        return super().__truediv__(x)


try:
    # a = int(12)
    my_int = MyInt(12)

    print(my_int / 0)

except AsgharException as e:
    print(e)



# try:
#     # print(12/0)
    
#     instance = AsgharException(code=404, desc="you encountered asghar exception.")
#     # raise AsgharException(code=404, desc="you encountered asghar exception.")
#     raise instance

#     print("hello")

# except AsgharException as e:
#     print(f"catched asghar exception | e: {e}")