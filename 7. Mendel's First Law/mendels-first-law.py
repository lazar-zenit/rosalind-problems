# Import libraries
from itertools import product

# Define the Punnet square function
def punnet_square(parent1, parent2):
    # Split allele strings into letters in list
    alleles_p1 = [allele for allele in parent1]
    alleles_p2 = [allele for allele in parent2]
    
    # List of all combination using itertools.product() function
    combinations = list(product(alleles_p1, alleles_p2))
    
    # Ttotal number of combination is lenght of the list
    total_combinations=len(combinations)

    # Empty dictionary to house combinations anf their number
    combination_count = {}
    
    # Loop for counting distinct combinations 
    for combo in combinations:
        if combo in combination_count:
            combination_count[combo] += 1
        else:
            combination_count[combo] = 1
            
    # Empty dictionary to hold calculated probabilities
    probabilities = {}
    
    # Loop for counting items and calculating probabilities
    for combo, count in combination_count.items():
        probability = count / total_combinations
        probabilities[combo] = probability

    return probabilities

k = 'AA'
m = 'Aa'
n = 'aa'

print(punnet_square(k, m))