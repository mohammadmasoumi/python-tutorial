
"""
#######
*******
 Hello
*******
#######

italic
strong
<strong><italic>Hello</strong></italic>
"""


def strong(f):
    # f: italic.wrapper
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs) # res: "<italic>Hello</italic>"
        return f"<strong>{res}</strong>" # "<strong><italic>Hello</italic></strong>"

    return wrapper


def italic(f):
    # f: fn
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        return f"<italic>{res}</italic>" #  "<italic>Hello</italic>"
    return wrapper

@strong
@italic
def fn():
    return "Hello"

"""
@italic
def fn():
    return "Hello"

italic_wrapper = italic(fn)

@strong
italic_wrapper

strong_wrapper = strong(italic_wrapper)
strong_wrapper()

"""

print(fn())