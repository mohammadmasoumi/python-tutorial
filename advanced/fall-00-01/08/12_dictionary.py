# dict - dictionary

# key value pairs
d = {
    'a': 2  # key 'a' - value 2
}

print(d)
print(d['a'])

# Traceback (most recent call last):
#     print(d['b'])
# KeyError: 'b'
# print(d['b'])

# dictionary.get(key, default)
# if key is exists: return value else return default
# print(d['a', 1]) raise exception

print(d.get('b'))
print(d.get('a', 3))  # exists 'a' -> value = 2
print(d.get('b', 3))  # does not exist 'b' -> default = 3
print(d.get('b', "Hello from here"))
print(d.get('b', d['a']))


