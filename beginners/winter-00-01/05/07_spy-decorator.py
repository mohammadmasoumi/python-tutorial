from spy import logger


@logger
def greeting(name, last_name):
    print(f"Hello, {name} - {last_name}")
    # return None


a = greeting(name="Aliakbar", last_name="mohajer") # key: value
print("---------------")
greeting("Aliakbar", "mohajer") # positional arguement