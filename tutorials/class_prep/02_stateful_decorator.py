
def call_counter(f):
    call_counter.count = 0

    def wrapper(*args, **kwargs):
        call_counter.count += 1
        print(f"Calling {f.__name__} for the {call_counter.count} times.")
        res = f(*args, **kwargs)
        return res
    
    return wrapper

@call_counter
def function():
    pass


function()
function()
function()