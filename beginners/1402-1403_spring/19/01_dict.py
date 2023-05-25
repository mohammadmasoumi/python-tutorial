
"""
Datatypes:
 - int
    - immutable
 - float
    - immutable
 - bool
    - immutable
 - str
    - immutable
    - iterable
 - set
    - iterable
    - mutable
    - duplication is not allowed {1, 1, 2, 2} => {1, 2}
    - unordered -> no index
    - items must be hashable 
            f
        a ----> b

        hash_function(a) => b
                        </=
        application:
           - store password in DBs

        unhashable:
            - set
            - list
            - list or set in tuple

            hash function

            ali -> ord('a') * (index+1) + ord('l') * (index+1) +ord('i') * (index+1) 
            lia -> ...
 - list
    - mutable
    - iterable
    - duplication is allowed
    - ordered -> index
    - various datatype as item => [1, 1.1, [1, 2], (1, 2), "1"]
 - tuple
    - immutable
    - iterable
    - duplication is allowed
    - ordered -> index
    - various datatype as item => [1, 1.1, [1, 2], (1, 2), "1"]
 - dict  
"""

"""
Dictionary
    - ordered, python 3.6 >
    - mutable
    - duplicated key is not allowed
    - iterable
    - ordered -> key (is not important)
    - various datatype as value
    - keys must be hashable

key: value

"""

# braces ()

# curly braces
d1 = {} # empty dict
d2 = dict()

# built-in function
# constructor 
s1 = set()

# DO NOT FORGET COMMA ,
d3 = {'k1': 'v1', 'k2': 'v2'}
print(f"d3: {d3}")

d4 = {
    # key:value,
    'k1': 'v1',
    'k2': 'v2',
}
print(f"d4: {d4}")

d5 = {'k1': 'v1',} # is no JSON: Java script object notation
# {"k1": "v1", "k2": "v2"} 
#   - must declared with double qoute
#   - must'n put comma at the end

print(f"d5: {d5}")

d7 = {
    "k1": "v2", # d7: {"k1": "v2"}
    "k2": "v2", # d7: {"k1": "v2", "k2": "v2"}
    "k1": "v3", # d7: {"k1": "v3", "k2": "v2"} UPDATE VALUE OF k1
    "k3": "v3", # d7: {"k1": "v3", "k2": "v2", "k3": "v3"}
}
print(f"d7: {d7}")

d6 = {
    1: "Hello",  # {1: "Hello"}
    True: "Bye" # {1: "Bye"}
}

print(f"d6: {d6}")

d8 = {
    True: "Hello",  # {True: "Hello"}
    1: "Bye"  #  # {True: "Bye"}
}

print(f"d8: {d8}")

# Dictionary entries must contain key/value pairs
d9 = {
    True: ("Hello", "Bye"),  # {True: "Hello"}
    1: "Bye"  #  # {True: "Bye"}
}

print(f"d9: {d9}")

d10 = {
    'k1': {
        'k11': {
            'k111': {
                'k1111': 'v1'
            }
        },
        'k1': 'v1'
    }
}

print(f"d10: {d10}")
