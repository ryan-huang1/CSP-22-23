#while loop
input = int(input("Enter a positive number between 1 and 25: "))

cycles = 0
while cycles == 0:    
    for i in range(input+1):
        print(i*"*")
    for i in range(input+1):
        print((input-i)*"*")
    cycles += 1
   