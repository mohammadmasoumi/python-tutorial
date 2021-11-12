from register import register, print_register


@register
def asghar1(param1):
    print(param1)


@register
def asghar2(param1):
    print(param1)


@register
def asghar3(param1):
    print(param1)


asghar1("Akbar")
asghar2("Asghar")
asghar3("Hassan")

print_register()
