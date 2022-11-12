def runner(n):
    def decorator(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                f(*args, **kwargs)

        return wrapper

    return decorator


# decorator = runner(2) n: 2
# wrapper = decorator(chineese_greeting)
# wrapper(name='Asghar', gender='female')

@runner(2)
def chineese_greeting(name, gender):
    print(
        f"Hello, How are you? {'Mr.' if gender == 'male' else 'Miss/Mrs.'}{name}")
    return name


print(chineese_greeting(name='Asghar', gender='female'))
