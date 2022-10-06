from random import randint

name = input("Name: ")
pet_name = input("Pet name: ")
birth_year = input("Birth year: ")
birth_month = input("birth month: ")
birth_day = input("Birth day: ")

words = [name, pet_name, birth_year, birth_month, birth_day]
random_passwords = []

for word1 in words:
    for word2 in words:
        random_passwords.append(word1 + word2)

for word1 in words:
    for word2 in words:
        random_passwords.append(word1 + word2)
        for char in ["@", "#", "$", "%", "*", "&", "^", "!", "~"]:
            random_passwords.append(word1 + char + word2)

for word1 in words:
    for word2 in words:
        for word3 in words:
            random_passwords.append(word1 + word2 + word3)
            for char in ["@", "#", "$", "%", "*", "&", "^", "!", "~"]:
                random_passwords.append(word1 + char + word2 + char + word3)
                random_passwords.append(word1 + char + word2 + word3)
                random_passwords.append(word1 + word2 + char + word3)

for word1 in words:
    for word2 in words:
        for word3 in words:
            for word4 in words:
                random_passwords.append(word1 + word2 + word3 + word4)
                for char in ["@", "#", "$", "%", "*", "&", "^", "!", "~"]:
                    random_passwords.append(word1 + char + word2 + char + word3 + char + word4)
                    random_passwords.append(word1 + char + word2 + word3 + word4)
                    random_passwords.append(word1 + word2 + char + word3 + char + word4)

#           file name      mode
with open("password.txt", "w") as file:
    for password in random_passwords:
        file.write(password + "\n")
