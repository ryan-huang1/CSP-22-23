def avg(a, b):
    return (a + b) / 2

def per(n, t):
    if t == 0:
        return 'LOSER GO AWAY YOU CANT DIVIDE BY ZERO IDIOT DUMB DUMB STUPID'
    else:
        return n / t * 100

def sum_1_100():
    sum = 0
    for i in range(1, 101):
        sum = sum + i
    return sum

def prnt_ints(i, j):
    for k in range(i, j + 1):
        print(k)

def sum_ints(i, j):
    sum = 0
    for k in range(i, j + 1):
        sum = sum + k
    return sum

def sum_ints_m(i, j):
    sum = 0
    for k in range(i, j + 1):
        if k % 3 == 0:
            sum = sum + k
    return sum

def sum_ints_m37(i, j):
    sum = 0 
    for k in range(i, j + 1):
        if k % 3 == 0 or k%7 == 0:
            sum = sum + k
    return sum

#prints in order the odd numbers from 100 back to 42



def odd_ints_100b():
    k = 100
    while True:
        if k % 2 != 0:
            print(k)
        if k == 0:
            break
        k -= 1
        
    j = 0
    while True:
        if j % 2 != 0:
            print(j)
        if j == 42:
            break
        j += 1
    
def odd_ints_b(a,o):
    k = a
    while True:
        if k % 2 != 0:
            print(k)
        if k == 0:
            break
        k -= 1
        
    j = 0
    while True:
        if j % 2 != 0:
            print(j)
        if j == o:
            break
        j += 1

def even_ints_b(a,o):
    k = a
    while True:
        if k % 2 != 0:
            print(k)
        if k == 0:
            break
        k -= 1
        
    j = 0
    while True:
        if j % 2 != 0:
            print(j)
        if j == o:
            break
        j += 1

def factorial(input):
    if input == 0:
        return 1
    else:
        return input * factorial(input - 1)

# make a method which uses the taylor series to approximate e^x using n terms
def e_to_x(e, x):
    sum = 0
    for i in range(0, e + 1):
        sum = sum + (x ** i) / factorial(i)
    return sum

def factor(input):
    for i in range(1, input + 1):
        print(i)
        if input % i == 0:
            print(i)

#make a method given a positve integer number n, determine and print out the frequency(number of times it appears) of a diget in d, in all possible values from 0 up to and including n
def dig_freq(n, d):
    count = 0
    for i in range(0, d + 1):
        for j in str(i):
            if j == str(n):
                count = count + 1
    return count