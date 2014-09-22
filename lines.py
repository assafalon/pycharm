__author__ = 'assafalon'

# a program that accepts a file and output the even lines (1-base numbering)
# declaring an index for line number
line_num = 1
#opening the file into object f
f = open('rosalind_ini5.txt', 'r')
for line in f:
    if line_num % 2 == 0:
        print line.strip()
    line_num+=1
f.close()
