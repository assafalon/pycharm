__author__ = 'assafalon'
s = "TATTTCTCCCACTCATGATGACGCCCCAAACGTAGAAACCTCTCTGAACTCGGCTCAATGGTGCAAGCTAACATCATTGTGCCTGCCCACTGCCCTGAATGGATAGCGGCTGTGCTGAGCATACGCGGGCAGTGCATGGACGTTTGGTTAAACACGTGAGGATGTTTGCGGTTTACCCTACATCCGAATCGTGTAACACCCCATGTGCATTTTTCGCAGCCGAGTGTTTACGCACAAACCTCTAGTCCTTAACCTCCCTACCATGTGTACTTTTCACAAAGCGCTCGCACACCTTCCAGGTTGATAATTTCTAGTGGTAAATGTGTTTCAGTGCACTCGTTCGTAAAAAAGCCATAAATGAATGTCGATGGCTGACGCAATGCGGTGAGCGCGATGGTGTGTATACCCGCTAAAGTTCCGTATTGCAGTGGCTTAAGGTAGTCTTCTTGACATTGCCCAATAGCCGTCTTTATCATACGGATTGATCGTCCCTGACGCATACAGCGCACGTGGCACACCCAATGCTAAGCTCGGCATTCGTTCATTTACACGCCATGGTTCAGCGTCACAGGTCAGCGCGTACCTACAGTTTTCTATTTTGCGCCTAAGCGGATTGAAGAAGATGGAGAGATAACCGTTCCCCTCCTGGCTCGCTTAAGGGACGTGTAACTAAATAATCTGAACAACGTCCTGGCCCTCATGCGCGCAACCTATGATGGATTCTGTCCTAGGATCTCGGAGGCAGACCCTGCGCCATCAGCATCTCCATTGATGCCACAAACAAAAGAGCAACATAGTGAAACCAATGGAACGTGAGCGATGATTATATGCTATCAGCTCCCAGATAAAC"
RC=""
dic = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
for i in s:
    RC = dic[i]+RC
print RC