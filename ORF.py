__author__ = 'assafalon'
#f = open('rosalind_orf.txt','r')
dna_seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
#for line in f:
#    if not line[0] == ">":
#        dna_seq += line.strip()
#f.close()

# generate reverse compliment:
dic = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
dna_seq_RC = ""
for i in dna_seq:
    dna_seq_RC = dic[i] + dna_seq_RC

#print dna_seq
#print dna_seq_RC

start = "ATG"
it = 0
while len(dna_seq[it:])>=3:
    if dna_seq[it:it+3] == start:
        print it
    if dna_seq_RC[it:it+3] == start:
        print it
    it += 1

