func_name = input()

exec(
    f"""def {func_name}():
        print("You are so khafan")
    """
)

a = exec(f"{func_name}()")
print(a)
# eval(f"{func_name}()")
