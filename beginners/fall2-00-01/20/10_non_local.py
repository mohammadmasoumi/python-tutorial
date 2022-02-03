a = 2000

def func1():
    # local scope func1
    a = 12
    print(f"a[func1]: {a}")

    def func2():
        # nonlocal a # a which is not in global scope
        global a # a which is in global scope
        # without using nonlocal
        # 1. search a in local variables
        # 2. search a in outer scope (if you want to read)
        # 3. search in global scope (if you want to read)
        
        print(f"a[func2]: {a}")
        a += 1
        # print(f"a: {a}")

    func2()
    print(f"a[func1]: {a}")

func1()
print(f"a[outer]: {a}")
