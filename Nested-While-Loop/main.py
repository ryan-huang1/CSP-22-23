#while loop
input = int(input("Enter a positive number between 1 and 25: "))

cycles = 0
var_one = 0
var_two = 1
while cycles == 0:    
    while var_one < input+1:
        print(var_one*"*")
        var_one += 1
    print(input*"*")
    while var_two < input+2:
        print((input-var_two)*"*")
        var_two += 1
    cycles += 1
   