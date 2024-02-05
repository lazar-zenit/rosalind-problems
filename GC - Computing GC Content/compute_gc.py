# Biopython-based way
# Import libraries
import os
import time
from Bio import SeqIO
# Start the timer
start = time.time()

# For importing fil via absolute path
raw_path = r"... 3. Computing GC Content\rosalind_gc.txt"
os_path = raw_path.replace('\\', '/')
file_path = os.path.abspath(
    os_path)

def read_fasta_biopython(file_path):
    # Open the empty dictionary
    sequences = {}
    
    # Parse the file
    for record in SeqIO.parse(file_path, 'fasta'):
        sequences[record.id] = str(record.seq)
    
    return sequences

def compute_gc_content(sequences):
    gc_contents_all = {}
    
    # Go through dictionary using .items() function
    for seq_name, sequence in sequences.items():
        gc_content = ((sequence.count('G') + sequence.count('C')) / \
            len(sequence)) * 100
            
        gc_contents_all[seq_name] = gc_content
    
    return gc_contents_all


# Call a function
sequences = read_fasta_biopython(file_path)
gc_contents_all = compute_gc_content(sequences)
print(sequences,'\n')
print(gc_contents_all)

# Find out max value
# Get max key pair
max_key = max(gc_contents_all, key=gc_contents_all.get)
max_value = gc_contents_all[max_key]

# Print the key and the corresponding value
print(f'\n{max_key}\n{max_value}')

# Stop the timer and calculte time elapsed
end=time.time()
print('\nTime elapsed (minutes):', 
      round((end-start)/60, 2), 
      '\nTime elapsed (seconds):', 
      round(end-start, 2))


#%%
# Explicit way to read FASTA into dictionary
# Import libraries
import os
import time

# Start the timer
start = time.time()

# For importing fil via absolute path
raw_path = r"... 3. Computing GC Content\rosalind_gc.txt"
os_path = raw_path.replace('\\', '/')
file_path = os.path.abspath(
    os_path)


# Explicit way to read FASTA into dictionary
def read_fasta(file_path):
    # Dictionary for sequences
    sequences = {}

    # Temporary empty string for sequence names (headers)
    current_seq_name = ''

    #temporary string for sequence itself
    current_seq = ''

    # Open and read FASTA file
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip() # Remove whitespaces
        
            # For headers when line starts with '>'
            if line.startswith('>'):
                # If seqence is not empty
                if current_seq_name != '':
                    # Put header (sequence name in dictionary) with temporary variable
                    sequences[current_seq_name] = current_seq
                    # Clear temporary string
                    current_seq = ''
       
                    # If it starts with '>' take whole first line without '>'       
                current_seq_name = line [1:]
        
            # If it is not header line
            else:
                # Add line to temporary string
                current_seq += line
                # If the variables are NOT empty (true) - this is to it does not double some things ot put empty strings
                
        if current_seq_name and current_seq:
                # Relate strings in dictionary
                sequences[current_seq_name] = current_seq           
    return sequences

# Define GC content calculation function
def compute_gc_content(sequences):
    gc_contents_all = {}
    
    # Go through dictionary using .items() function
    for seq_name, sequence in sequences.items():
        gc_content = ((sequence.count('G') + sequence.count('C')) / \
            len(sequence)) * 100
            
        gc_contents_all[seq_name] = gc_content
    
    return gc_contents_all

# Call functions
sequences = read_fasta(file_path)
gc_contents_all = compute_gc_content(sequences)
print(sequences,'\n')
print(gc_contents_all)

# Find out max value
# Get max key pair
max_key = max(gc_contents_all, key=gc_contents_all.get)
max_value = gc_contents_all[max_key]

# Print the key and the corresponding value
print(f'\n{max_key}\n{max_value}')

# Stop the timer and calculte time elapsed
end=time.time()
print('\nTime elapsed (minutes):', 
      round((end-start)/60, 2), 
      '\nTime elapsed (seconds):', 
      round(end-start, 2))
