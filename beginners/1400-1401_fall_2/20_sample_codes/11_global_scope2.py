# scope1 - read global variables


a, b, c = 10, 11, 12


def function():
    # if you want to change global variable you need to use global keyword, see scope3.py
    a, b, c = 1, 2, 3
    print(
        f"[INSIDE] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")


print(
    f"[BEFORE] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")

function()

print(
    f"[AFTER] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")
