__author__ = 'assafalon'
import numpy as np
s="19743 18986 19093 16558 16710 17334"
couples = [int(n) for n in s.split()]
odds = [1.0, 1.0, 1.0, 0.75, 0.5, 0]
result = 0
for i in range(6):
    result+=couples[i]*odds[i]*2
print result
