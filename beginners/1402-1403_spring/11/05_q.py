# get the first four digits of encoded number

code1 = "||1234"
code2 = "|12345"
code3 = "12345|"
code4 = "1234||"

# Wrong
# print(code1[-4:])
# print(code2[-4:])

print(code1.replace("|", "")[:4])
print(code2.replace("|", "")[:4])
print(code3.replace("|", "")[:4])
print(code4.replace("|", "")[:4])


