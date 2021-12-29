# input: Hassan Fatemeh Asghar Mohammad
names = input().split()

for name in names:

    if name == "Asghar":
        print("I found Asghar")

        # What will happed if you omit `break`?
        break

else:
    print("Where is Asghar")


