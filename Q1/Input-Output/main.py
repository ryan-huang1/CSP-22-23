name = input("What is your name?")

#if name is not a string
if not name.isalpha():
    raise TypeError

#if name is a string
else:
    name = name[0].upper() + name[1:]

    if name == "Ryan":
        print(f"Congratulations {name} your identity has been verified.")
    else:
        print(f"Sorry {name} your identity has not been verified.")

