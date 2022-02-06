a, b, c = 10, 11, 12


def function():
    # change global variables
    global a, b, c
    a, b, c = 1, 2, 3
    print(
        f"[INSIDE] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")


print(
    f"[BEFORE] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")

function()

print(
    f"[AFTER] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")
