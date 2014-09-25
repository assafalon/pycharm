#!/usr/bin/env python

# defien a dictionary of the genetic code
decode = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
          'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
          'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
          'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
          'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
          'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
          'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
          'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
          'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
          'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
          'UAA':' ', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
          'UAG':' ', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
          'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
          'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
          'UGA':' ', 'CGA':'R', 'AGA':'R', 'GGA':'G',
          'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'} 

# open a file with the string
with open ("rna_input.txt",'r') as input_rna:
    RNA = input_rna.read()

# define an iterator that runs on the RNA code
index = 0
# define a variable to store the protein output
PROT = ""

# loop on the RNA and translate using the dictionary
while index < len(RNA):
    key = RNA[index]+RNA[index+1]+RNA[index+2]
    PROT += decode[key]
    index+=3
# output the protein 
print PROT
