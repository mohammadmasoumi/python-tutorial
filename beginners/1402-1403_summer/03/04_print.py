# print
word = "hello"

# \n
"""
Under the hood

print(*values, sep, end)
*values: object,
sep: str | None = ...,
end: str | None = ...,

"hello", "bye", sep="*", end="\n"

printf("hello*bye\n")
"""
print("Hello")  # end: "\n", sep: " " (space)
print(word)  # print the value of variable

print("a", "b", "c")  # abc, a,b,c , "abc", a_b_c
# "a b c\n"
# --------------

"""
C
printf("hello \n")
printf("Bye")

format string
\n: new line
\t: new tab
\r: return carriage
\b: back space

hello
Bye

# ---------------------
# hello bye
# 1.
printf("hello ")
printf("bye")
# 2.
printf("hello")
printf(" bye")
# ---------------------
# hello
# bye
# how are you
# 1.
printf("hello\nbye\nhow are you")
# 2.
printf("hello\n")
printf("bye\n")
printf("how are you")
# ---------------------
"\\" -> \
"\\\\" -> \\
"\"" -> "
# ---------------------
@ 1.
printf("hello\n\n")
printf("bye\n")
printf("how are you")

# 2.
printf("hello\n")
printf("\nbye\n")
printf("how are you")
hello

bye
how are you

"""

# 1.
print("Hello\n")  # "Hello\n\n"
print("Bye")  # "Bye\n"
print("How are you")  # "\n"

print("------------")
print("Hello", end="")  # "Hello"
print("Bye", end="")  # "Bye"
print("How are you", end="")  # ""
# HelloByeHow are you
# "HelloByeHow are you" "Hello Bye How are you"
print("Hello", "Bye", "How are you", end="")  # "Hello"
# Hello Bye How are you

print("Hello", end=" ")  # "Hello "
print("Bye", end=" ")  # "Bye "
print("How are you", end=" ")  # "How are you "
# Hello Bye How are you

print("Hello", "Bye", "How are you", sep="*", end="")  # "Hello"
# sep: " ", end="\n"
# join by sep + end
# "Hello*Bye*How are you" + ""
print("Hello", "Bye", "How are you")
