import time

# Start timer
start=time.time()


# Non-optimal way - simple recursive function for Fibonacci rabbit problem
'''
# Define fibonacci sequence function called "rabbits"
def rabbits(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return rabbits(n - 1) + rabbits(n - 2)

# Display each step    
for n in range (1, 46):
        print(n, ":", rabbits(n))
        
# End timer        
end=time.time()
print('Time elapsed (minutes):', 
      round((end-start)/60, 2), 
      '\n', 'Time elapsed (seconds):', 
      round(end-start, 2))
'''




# ACTUAL SOLUTION, n number of months and k number of pair offspring
# Open the dataset
with open('rosalind_fib.txt', 'r') as file:
    content = file.read().strip()

# Split numbers based on space and allocate to proper variables    
numbers = content.split()   
n = int(numbers[0])
k = int(numbers[1])

# When presented with problem of different number of pairs as an offspring
def rabbits_k (n, k):
    if n == 1:
        return 1 # second month
    elif n == 2:
        return k # third month
    
    oneGen = rabbits_k(n - 1, k) # fourth month
    twoGen = rabbits_k(n - 2, k)
    
    if n <= 4: # fifth month and beyond
        return (oneGen + twoGen)
    
    return (oneGen + (twoGen * k))

print(rabbits_k(n, k))

print("\nPairs through generations ")

# For displaying number of pairs through generations
for n in range (1, n + 1):
    print(n, rabbits_k(n, k))
    