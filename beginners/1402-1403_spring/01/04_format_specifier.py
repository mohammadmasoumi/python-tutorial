# backspace
print("Hello \bworld")
# "Helloworld"
print("Hello \bworld", sep="*")
# "Hello*\bworld"
print("Hello", "\bworld", sep="*")
# "HelloC\bworld"
print("Hello", "\bworld", sep="C")
# "HelloASGHAR\bworld"
# print("Hello", "\b\b\b\b\b\b\b\b\b\bworld", sep="ASGHAR")
print("Hello", "\b\b\b\b\b\bworld", sep="ASGHAR")
