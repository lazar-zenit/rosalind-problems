
# Open file, trip whitespaces and split based on last line (motif)
with open('rosalind_subs.txt', 'r') as file:
    content = file.read().strip()
    sequence, motif = content.rsplit('\n', 1)
    
# Check splitting
print('Sequence: ', sequence)
print('\nMotif: ', motif)

positions = []
start = 0

# Approach 1: while loop
while start < len(sequence):
    pos = sequence.find(motif, start)
    if pos != -1:
        positions.append(pos)
        start = pos + 1
    else:
        break
    
print("\npositions (Whie loop):\n", positions)

# Approach 2: list comprehension
positions = [i for i in range(len(sequence)) if sequence.startswith(motif, i)]
print("\nPositions (list comprehension):\n", positions)

# Add plus one because computers count from zero (zero is first letter in sequence)
positions_fixed = [x+1 for x in positions]

# Print the output as per assignment
output = ' '.join(str(positions_fixed) for positions_fixed in positions_fixed)
print('\nOutput:\n', output)

