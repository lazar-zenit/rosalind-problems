# open file and split into two string based on newline
with open('rosalind_hamm.txt', 'r') as file:
    data = file.read().strip()
    s1, s2 = data.split('\n', 1)

# Print s1 and s2 for troubleshooting
print('\nSequence 1: ', s1, '\nLenght: ', len(s1))
print('\nSequence 2: ', s2, '\nLenght: ', len(s2))

# Define function
def hamming_distance(s1, s2):
    diff_ind = []
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_ind.append(i)
    else:
        print('Sequences are not of equal length')
    
    print('\nIndices of differing base pairs:', diff_ind)
    print('\nHamming distance:', len(diff_ind))

# Call function
hamming_distance(s1, s2)