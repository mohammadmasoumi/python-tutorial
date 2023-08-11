# single line
eval("print('Hello')")

# multi line 
exec("""
print('Hello')
print('Hello')
print('Hello')
print('Hello')
""")

func_name = input()

exec(f"""
def {func_name}():
    print('bye')
    print(f'calling {func_name}')
{func_name}()
""")