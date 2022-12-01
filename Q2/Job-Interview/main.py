input = str(input("what is your input? "))

if input != "":
    input_modify = input[::-1]
    input_modify = input_modify.replace(" ", "")
    input_modify = input_modify.replace("!", "")

print(input_modify)