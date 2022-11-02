input = int(input("What is your number?"))

if input < 0:
    print("Your number is negative.")
    raise TypeError

#add all numbers from 1 to input
sum = 0
for i in range(1, input + 1):
    sum += i

print(f"The sum of all numbers from 1 to {input} is {sum}.")