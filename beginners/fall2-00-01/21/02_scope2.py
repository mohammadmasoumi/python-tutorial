# global variables

a, b, c = 11, 12 ,13


def function():
    # change
    # a = a + 1
    # UnboundLocalError: local variable 'a' referenced before assignment
    global a, b, c
    a += 1
    b += 1
    print(f"[function] a: {a}, b: {b}, c: {c}")


print(f"[before] a: {a}, b: {b}, c: {c}")
function()
print(f"[after] a: {a}, b: {b}, c: {c}")
