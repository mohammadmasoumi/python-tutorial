# ["A\n", "B\n", "C\n"]
# [SEP]: "A\n*B\n*C\n"
# [END]:"A\n*B\n*C\n" + "*" => 
# "A\n*B\n*C\n*"

# ["D\t\t\n", "E\n"]
# [SEP]: "D\t\t\n$E\n"
# [END]: "D\t\t\n$E\n" + "\n" =>
# "D\t\t\n$E\n\n"

# Formatted string
# printf => print formatted
"""
A
*B
*C
*D         
$E


"""
# first quiz
print("A\n",                "B\n", "C\n", sep="*", end="*")
print("D\t\t\n", "E\n", sep="$")

# second quiz
# "Hell\roooo\rworld\rBye"
# Hell
# oooo
# => oooo
# oooo
# world
# => world
# world
# Bye
# => Byeld

print("Hell\roooo\rworld\rBye")