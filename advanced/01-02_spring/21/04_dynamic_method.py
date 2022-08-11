# dynamic function
c = input()

# def asghar():
#     pass

# "x ^ 1000 + 3 * x ^ 10"
# "2 * (2 + 10 / (10 ** 2) + 10 ** 2)"
# eval("2 * (2 + 10 / (10 ** 2) + 10 ** 2)")

# print(asghar)
print(eval("2 + 2"))
exec("print(2 + 2)")

exec(
    f"""def {c}(): 
        print('a')
    """
)
exec(f"{c}()")
exec(f"print({c})")