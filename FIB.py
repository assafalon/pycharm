__author__ = 'assafalon'

# initial parameters:
# number of generations
n = 28
# rabbits per litter
k = 4
# we start with 1 rabbit pair and an incubation period of one generation
gen_1 = 1
gen_2 = 1
# we start from generation 3 so we reduce n by 2
n-=2
# a while loop until all generations end
while n:
    n-=1
    # calculate next generation by multiplying first generation with k and adding the second generation
    gen_3 = gen_1 * k + gen_2
    # updating generations for the next loop entry
    gen_1 = gen_2
    gen_2 = gen_3
print gen_3