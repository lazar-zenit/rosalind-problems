# Import libraries
from itertools import product
import math

'''
# SIMPLE WAY: probabilities are hard coded

# Calculate all combinations of k, m and n given their repetitions
def calculate_parent_combos(repetitions):
    # Assign number of individuals given problem's input
    k_reps, m_reps, n_reps = repetitions
    
    # Get all_combinations, given number of repetitions for the pairs
    all_combinations = {
        'km' : math.comb(k_reps + m_reps, 2), 
        'kn' : math.comb(k_reps + n_reps, 2),
        'mn' : math.comb(m_reps + n_reps, 2),
        'kk' : math.comb(k_reps, 2),
        'nn' : math.comb(n_reps, 2),
        'mm' : math.comb(m_reps, 2),
        }

    return all_combinations

# Copy input of prioblem into list
repetitions = [2, 2, 2]

# Call function and print output
results = calculate_parent_combos(repetitions)
total_count = sum(results.values())
k_reps, m_reps, n_reps = repetitions
total_count_2 = math.comb(k_reps + m_reps + n_reps, 2)
print(total_count_2)
# Calculate probability of dominant allele, probabilities of sertain combinations
# are hand calculated
dominant_probability = (((results.get('kk', 0))/total_count) 
                        + ((results.get('km', 0))/total_count)
                        + ((results.get('kn', 0))/total_count)
                        + (((results.get('mm', 0))/total_count) * 0.75)
                        + (((results.get('mn', 0))/total_count) * 0.5)
                        )

print(results)
                        
print(dominant_probability)

'''

'''
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
    
    print(combination_count)
    
    # Empty dictionary to hold calculated probabilities
    probabilities = {}
    
    # Loop for counting items and calculating probabilities
    for combo, count in combination_count.items():
        probability = count / total_combinations
        probabilities[combo] = probability

    return print(probabilities, '\n')
'''


populationList = [2, 2, 2]

total = 0
homoDominant = float(populationList[0])
heterozygous = float(populationList[1])
homoRecessive = float(populationList[2])

for p in populationList:
	total += float(p)

dominantTotal = homoDominant/total
heterozygousDominantTotal = (heterozygous/total) * ((homoDominant/(total-1)) + (heterozygous-1)/(total-1) * 0.75 + ((homoRecessive/(total-1)) * 0.5))
domHeterRecesTotal = (homoRecessive/total) * (homoDominant/(total-1) + heterozygous/(total-1) * 0.5)


print(dominantTotal)
print(heterozygousDominantTotal)
print(domHeterRecesTotal)

completeProbablity = dominantTotal + heterozygousDominantTotal + domHeterRecesTotal

print(completeProbablity)



