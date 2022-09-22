#skip count from -1 to -50 by user input

input = int(input("What is your number?"))

if input < 0:
    print("Your number is negative.")
    raise TypeError

for i in range(50):
    if i % input == 0:
        print(f'-{i}')