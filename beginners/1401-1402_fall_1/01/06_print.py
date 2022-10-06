# built-in function

name = "Ali"
score = 19.2

# sep: ' '
# end: \n
"""
sys.stdout
standard output

print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
"""
# change sep
print(name, score, 20,  "name")
print(name, score, sep="*")
print(name, score, sep="")
print(name, score, "name" ,sep="-")
print(name, score, "name" ,sep="if")

# change output
file = open('file.txt', 'a')
print("--------------------")
print(name, score, "name" ,sep="#", file=file)

# change end
# value1[sep]value2[sep]value3[end]
print(name, score, "name" ,sep="-", end="*********\n")
# \n newline
print("Hello\n")
print("--------------------")

# flush
print("Hello", flush=False)

# flush
print("Hello", end="\\n")
