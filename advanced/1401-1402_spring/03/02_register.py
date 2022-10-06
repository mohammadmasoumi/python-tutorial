from spy import register

@register
def func1(username, password):
    print(f"username: {username}, password: {password}")

@register
def func2(a, b, c, d):
    print(f"{a}-{b}-{c}-{d}")


func1(username="mohammad", password="1234")
func2(10, 11, 12, 13)
