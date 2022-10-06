a = 12

def func1():
    a = 13
    def func2():
        a = 14
        def func3():
            # global a
            nonlocal a
            a += 100
            print(f"[func3]a: {a}, id: {id(a)}")

        print(f"[func2/before]a: {a}, id: {id(a)}")
        func3()
        print(f"[func2/after]a: {a}, id: {id(a)}")

    print(f"[func1/before]a: {a}, id: {id(a)}")
    func2()
    print(f"[func1/after]a: {a}, id: {id(a)}")

print(f"[global/before]a: {a}, id: {id(a)}")
func1()
print(f"[global/after]a: {a}, id: {id(a)}")

