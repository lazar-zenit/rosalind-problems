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


# Dictionaries of short and long aminoacids codes and codons
codon_table_long = {
    'UUU' : 'Phe', 'UUC' : 'Phe',
    'UUA' : 'Leu', 'UUG' : 'Leu',
    'UCU' : 'Ser', 'UCC' : 'Ser', 'UCA' : 'Ser', 'UCG' : 'Ser',
    'UAU' : 'Tyr', 'UAC' : 'Tyr',
    'UGU' : 'Cys', 'UGC' : 'Cys',
    'UGG' : 'Trp',
    'CUU' : 'Leu', 'CUC' : 'Leu', 'CUA' : 'Leu', 'CUG' : 'Leu',
    'CCU' : 'Pro', 'CCC' : 'Pro', 'CCA' : 'Pro', 'CCG' : 'Pro',
    'CAU' : 'His', 'CAC' : 'His',
    'CAA' : 'Gln', 'CAG' : 'Gln',
    'CGU' : 'Arg', 'CGC' : 'Arg', 'CGA' : 'Arg', 'CGG' : 'Arg',
    'AUU' : 'Ile', 'AUC' : 'Ile', 'AUA' : 'Ile',
    'AUG' : 'Met',
    'ACU' : 'Thr', 'ACC' : 'Thr', 'ACA' : 'Thr', 'ACG' : 'Thr',
    'AAU' : 'Asn', 'AAC' : 'Asn',
    'AAA' : 'Lys', 'AAG' : 'Lys',
    'AGU' : 'Ser', 'AGC' : 'Ser',
    'AGA' : 'Arg', 'AGG' : 'Arg',
    'GUU' : 'Val', 'GUC' : 'Val', 'GUA' : 'Val', 'GUG' : 'Val',
    'GCU' : 'Ala', 'GCC' : 'Ala', 'GCA' : 'Ala', 'GCG' : 'Ala',
    'GAU' : 'Asp', 'GAC' : 'Asp',
    'GAA' : 'Glu', 'GAG' : 'Glu',
    'GGU' : 'Gly', 'GGC' : 'Gly', 'GGA' : 'Gly', 'GGG' : 'Gly',
    'UAA' : '*', 'UAG' : '*', 'UGA' : '*', 
    }

codon_table_short = {
    'UUU' : 'F', 'UUC' : 'F',
    'UUA' : 'L', 'UUG' : 'L',
    'UCU' : 'S', 'UCC' : 'S', 'UCA' : 'S', 'UCG' : 'S',
    'UAU' : 'Y', 'UAC' : 'Y',
    'UGU' : 'C', 'UGC' : 'C',
    'UGG' : 'W',
    'CUU' : 'L', 'CUC' : 'L', 'CUA' : 'L', 'CUG' : 'L',
    'CCU' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P',
    'CAU' : 'H', 'CAC' : 'H',
    'CAA' : 'Q', 'CAG' : 'Q',
    'CGU' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R',
    'AUU' : 'I', 'AUC' : 'I', 'AUA' : 'I',
    'AUG' : 'M',
    'ACU' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T',
    'AAU' : 'N', 'AAC' : 'N',
    'AAA' : 'K', 'AAG' : 'K',
    'AGU' : 'S', 'AGC' : 'S',
    'AGA' : 'R', 'AGG' : 'R',
    'GUU' : 'V', 'GUC' : 'V', 'GUA' : 'V', 'GUG' : 'V',
    'GCU' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A',
    'GAU' : 'D', 'GAC' : 'D',
    'GAA' : 'E', 'GAG' : 'E',
    'GGU' : 'G', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G',
    'UAA' : '*', 'UAG' : '*', 'UGA' : '*', 
    }
# Take codons from sequence
#codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]

# Main function
def dna_to_protein(sequence, codon_table_short):
    if len(sequence) % 3 == 0:
        protein = ''
        for i in range(0, len(sequence), 3):
            codons = sequence[i:i + 3]
            if codons in codon_table_short:
                protein += codon_table_short[codons]
            else:
                protein += '?'
    else:
        print('Your sequence length is not divisible by 3')
            
    return protein

print('\nProtein translation: ', dna_to_protein(sequence, codon_table_short))

