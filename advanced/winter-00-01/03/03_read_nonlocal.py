
# global, nonlocal
a, b, c = 1, 2, 3

def func1():
    a, b, c = 10, 20, 30

    def func2():
        #a, b, c = 100, 200, 300

        def func3():
            global a, b, c
            a += 1
            print("inside func3", a, b, c)

        print("before func3", a, b, c)
        func3()
        print("after func3", a, b, c)

    print("before func2", a, b, c)
    func2()
    print("after func2", a, b, c)
    

print("before", a, b, c)
func1()
print("after", a, b, c)
