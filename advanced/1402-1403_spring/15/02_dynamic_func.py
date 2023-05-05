
func_name = input()

exec(
    f"""def {func_name}():
        print("Hello")
    """
)

eval(f"{func_name}()")
