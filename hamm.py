__author__ = 'assafalon'
# get two strings
s1 = "GAGCCTACTAACGGGAT"
s2 = "CATCGTAATGACGGCCT"

# define iterator for loop
i = 0
# define counter for mismatches
mismatch = 0
while i < len(s1):
    if not s1[i] == s2[i]:
        mismatch+=1
    i+=1
print mismatch

