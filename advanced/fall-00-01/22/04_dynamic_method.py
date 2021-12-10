# dynamic function
c = input()
exec(

    f"""def {c}(): 
        print('a')
    """
)
exec(f"{c}()")
exec(f"print({c})")
