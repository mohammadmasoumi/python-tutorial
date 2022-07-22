s = input()
character_count = {}

# char = 'h'
# KeyError: 'h'
# print(character_count[char])

"""
1. 
character_count[key]

if key exists:
    return value
else:
    raise exception(KeyError: 'h')

2.
character_count.get(key) default_value: None
character_count.get(key, 0) default_value: 0
character_count.get(key, 'asghar') default_value: 'asghar'

if key exists:
    return value
else:
    default value (None, defined default value)
"""
for char in s:
    # s: "hello world"
    # why?
    # if character_count[char]:
    #     pass
    # KeyError: 'h'

    # if char does not exist:
    #   None
    # false values: 0, False, 0.0, [], {}, set(), tuple(), None
    # if one the false values:
    #    pass
    if character_count.get(char):
        character_count[char] = character_count[char] + 1
        # character_count.update(char=character_count[char] + 1)
    else:
        # first time
        character_count[char] = 1
        # character_count.update(char=1)

print(character_count)