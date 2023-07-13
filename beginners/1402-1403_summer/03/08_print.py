print("A", "B", sep="\n", end="*")  # "A\nB" + "*" => "A\nB*"
print("C\t", "D\n", end="-")  # default sep: " " | "C\t D\n-"
print("E", "A\b", sep="&\n")  # default end:\n | "E&\nA\b\n"
print("Bye")
# \n new line
# \t 4 spaces
# \b back space

# ------------------
# Terminal
# A
# B*C     D
# -E&
# A
# Bye
