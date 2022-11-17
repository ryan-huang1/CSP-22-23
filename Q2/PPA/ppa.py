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