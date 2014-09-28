__author__ = 'assafalon'
# total number of generations
n = 82
# years to death
m = 19
# define a list with the first couple that is as long as the amount of generations and will count how many
# couples are in each generation
n-=1
fib = [1]
for i in range(m-1):
    fib.append(0)

while n:
    add = 0
    for i in range (1,m):
        add += fib[i]
    fib.insert(0,add)
    fib.pop(m)
    n-=1
total = 0
for i in range(m):
    total+=fib[i]
print total



