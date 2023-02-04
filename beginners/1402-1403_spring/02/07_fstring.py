# fstring - formatted string
name = "ahmad"
age = 12

print("Hello,", name)

sentence = "Hello, " + name 
print(sentence)

sentence = "Hello, " + name + " How are you, " + name + "?"
print(sentence)

print(f"Hello, {name} How are you, {name}?")
print("Hello, {name} How are you, {name}?")
print(f"Hello, {name} Happy {age}th birthday {name}?")

print(f"Hello, {name}{name} How are you, {name}?")
print(f"Hello, {name + name}{name} How are you, {name}?")
print(f"Hello, {{name + name}}{name} How are you, {name}?")
# TypeError: can only concatenate str (not "set") to str
# print(f"Hello, {name + {name}}{name} How are you, {name}?")
print(f"Hello, name {name} Happy {age}th birthday {name}?")

# 
# print(f"Hello, name {"ahmad"} Happy {age}th birthday {name}?")
# print(f'Hello, name {'ahmad'} Happy {age}th birthday {name}?')
print(f'Hello, name \' {name} \' Happy {age}th birthday {name}?')
print(f"Hello, name ' {name} ' Happy {age}th birthday {name}?")
print(f"Hello, name \" {name} \" Happy {age}th birthday {name}?")
print(f"Hello, name \\ {name} \\ Happy {age}th birthday {name}?")
print(f"Hello, name \\\ {name} \\\ Happy {age}th birthday {name}?")
print(f"Hello, name \\\\ {name} \\\\ Happy {age}th birthday {name}?")
print(f"Hello, name \\\\\ {name} \\\\\ Happy {age}th birthday {name}?")

print(f"Hello, name {'ahmad'} Happy {age}th birthday {name}?")
print(f'Hello, name {"ahmad"} Happy {age}th birthday {name}?')

# print(f"Hello, {name name}{name} How are you, {name}?") # INVALID

"""
~ tilda
` backtick .md
' single quote
" double quote
^ hat caret
& ampersand
| pipe
# hashtag
@ at sign
% percentage sign
$ dollar sign
* asterisk
! Exclamation mark
\ back slash
/ slash
 space
: colon
; semicolon
"""