__author__ = 'assafalon'
f = open('rosalind_gc.txt','r')
fasta = {}
for line in f:
    if line[0] == ">":
        key = line[1:].strip()
        fasta[key] = ""
    else:
        fasta[key]+=line.strip()
f.close()
for key in fasta:
    GC=0.0
    AT=0.0
    for c in fasta[key]:
        if c == "G" or c=="C":
            GC+=1
        else:
            AT+=1
    score = (GC * 100) / (GC+AT)
    fasta[key] = score
higest_key = ""
highest_value = 0.0
for key in fasta:
    if fasta[key] > highest_value:
        higest_key = key
        highest_value = fasta[key]

print higest_key
print highest_value




