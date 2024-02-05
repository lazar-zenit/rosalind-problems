from Bio import SeqIO
import os

# Import from absolut path
raw_path = r"C:\Users\Lenovo\Documents\Programiranje\rosalind-problems\LCSM - Finding a Shared Motif\rosalind_lcsm.txt"
os_path = raw_path.replace('\\', '/')
file_path = os.path.abspath(os_path)
  
# Import fasta sequences as a list usign biopython method                   
sequences = []                             
handle = open(file_path, 'r')     
for record in SeqIO.parse(handle, 'fasta'):                          
    seq = ''                               
    for nt in record.seq:                  
        seq += nt                          
    sequences.append(seq)                  
handle.close()                             

print(sequences)


# We want to sort seqences (by lenght) and use the first one to compar to others
# So we first sort sequences
srt_seq = sorted(sequences, key=len)

# Pick the shortest one
short_seq = srt_seq[0]

# And all others to compare                    
comp_seq = srt_seq[1:]

# Motif begins as an empty string                    
motif = ''
all_motifs = []
# Iterate over all substrings for a lenght of the shortest string
for i in range(len(short_seq)):
    for j in range(i, len(short_seq)): # Nested loop for ending position j
        m = short_seq[i:j + 1]         # Add one to ending position
        found = False                  # Comparison is based on boolean values, stat with False 
        for sequ in comp_seq:          # For all substrings within comp_seq          
            if m in sequ:                
                found = True           # If found change value to True
            else:                        
                found = False          # If not value stays false          
                break                  # Break the loop and starts with next postion of i          
        if found and len(m) > len(motif):  # If lenght of newly found match is longer than previous
            motif = m                  # Newly found is now our motif

# Print the answer
print("\n", "Motif is: ", motif) 



