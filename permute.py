#!/usr/bin/env python
n=7

# a function that returns the factorial of n
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
        
# a function to generate a list with numbers that go from 1 to n        
def gen_permute(n):
    permute = []
    for x in range(n):
        permute.append(x+1)
    return permute

# a function to print n    
def plp():
    for i in xrange(n):
        print permute[i],
    print    

def switch(pos1,pos2):
    temp=permute[pos1]
    permute[pos1]=permute[pos2]
    permute[pos2]=temp

permute = gen_permute(n)
print factorial(n)

def print_permute(position):
    if position == len(permute):
        plp()
    else:
        for current in range(position,len(permute)):
            switch(position,current)
            print_permute(position+1)
            switch(current,position)
            


print_permute(0)
