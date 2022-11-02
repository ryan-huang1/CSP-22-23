input = int(input("What is your number?"))

if input < 0:
    print("Your number is negative.")
    raise TypeError

#add numbers which are multiples of 3 or 4 from 1 to input
sum = 1
for i in range(1, input + 1):
    if i % 3 == 0 or i % 4 == 0:
        sum += i

print(f"The sum of all numbers from 1 to {input} is {sum}.")