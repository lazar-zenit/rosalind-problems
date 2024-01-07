# Open file and strip white spaces
with open('rosalind_prot.txt', 'r') as file:
    sequence = file.read().strip()

    
# Biopython solution
from Bio.Seq import Seq

rna = Seq(sequence)
protein = rna.translate()
print(protein)

codons = []
chunk = ''

print(len(sequence))

# Explicit solution

# Take codons from sequence
codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]

print(codons)