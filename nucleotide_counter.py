from collections import Counter
f = open('rosalind_dna.txt', 'r')
s = f.read()
f.close()
nucleotide_count = {}
for char in s:
    if char in nucleotide_count:
        nucleotide_count[char] += 1
    else:
        nucleotide_count[char] = 1
for key, value in nucleotide_count.items():
    print(key, value)