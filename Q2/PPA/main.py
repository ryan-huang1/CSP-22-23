import ppa

print('\navg(a,b)\n')
print('\t',ppa.avg(50,100))

# 2
print('\nper(n,t)\n')
print('\t',ppa.per(50,100),'%')
print('\t',ppa.per(3,5),'%')
print('\t',ppa.per(20,0),'%')


# 3
print('\nsum_1_100\n')
print('\t',ppa.sum_1_100())

# 4
print('\nprnt_ints(i,j)')
print('\t')
ppa.prnt_ints(1,5)
ppa.prnt_ints(-4,2)
ppa.prnt_ints(0,6)


# 5
print('\nsum_ints(i,j)')
print('\t',ppa.sum_ints(1,5))
print('\t',ppa.sum_ints(-4,2))
print('\t',ppa.sum_ints(0,6))

# 6
print('\nsum_ints_m(i,j)')
print('\t',ppa.sum_ints_m(1,10))
print('\t',ppa.sum_ints_m(-4,9))
print('\t',ppa.sum_ints_m(0,13))

# 7
print('\nsum_ints_m37(i,j)')
print('\t',ppa.sum_ints_m37(1,10))
print('\t',ppa.sum_ints_m37(-4,9))
print('\t',ppa.sum_ints_m37(0,13))

# 8
print('\nodd_ints_100b()')
print('\t')
ppa.odd_ints_100b()

# 9
print('\nodd_ints_b(i,j)')
print('\t')
ppa.odd_ints_b(100,42)
ppa.odd_ints_b(100,41)
ppa.odd_ints_b(10,-3)
ppa.odd_ints_b(-3,-10)

# 10
print('\neven_sum_b(i,j)')
print('\t')
print('\t',ppa.even_sum_b(100,42))
print('\t',ppa.even_sum_b(100,41))
print('\t',ppa.even_sum_b(10,-3))
print('\t',ppa.even_sum_b(-3,-10))