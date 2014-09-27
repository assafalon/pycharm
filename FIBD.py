__author__ = 'assafalon'
# total number of generations
n = 6
# years to death
m = 3
# define a list with first two generations
fib = [1,1]
for gen in range(2,n):
    add = fib[gen-1]+fib[gen-2]
    if gen+1 >= (m):
        add = add - fib[gen-m+1]
    fib.append(add)
print fib
