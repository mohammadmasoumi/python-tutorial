def italic(func):
     
    def wrapper():
        return '<i>' + func() + '</i>'
     
    return wrapper
 
def strong(func):
     
    def wrapper():
        return '<strong>' + func() + '</strong>'
     
    return wrapper
 
 
@italic
@strong
def introduction():
    return 'This is a basic program'
 
print(introduction())