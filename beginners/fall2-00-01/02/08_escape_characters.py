# \ backslash

# SyntaxError: EOL while scanning string literal
# tab
print("ali\tali")  # 4 spaces
print("ali\t" "ali")
print("ali\t" + "ali")
print("-------------------------")

# next line
print("ali\nali\n\n\n")
print("-------------------------")

# carriage return
print("ali\ali")
print("a\rlriali")
print("\raliali")
print("aliali\r")  # تاثیری ندارد
print("alial\ri")
print("-------------------------")

# \ backslash
print("\\\n")
print('\\')
print("\\\\")
print("\\\\\t")
print("-------------------------")

# "
print("\"")
print('"')
print('\'')
print("'")
print("-------------------------")

# b - backspace
print("ali\bali")
print("a\bliali")
print("aliali\b")
print("-------------------------")

# d - nothing
print("ali\dali")

# special character
print("\245")
