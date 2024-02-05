'''
# Non-optimal way - simple recursive function for Fibonacci rabbit problem
# Start timer
start=time.time()

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

'''
#EXPLICIT MEMOIZATION OF THE FUNCTION
# Start timer
start=time.time()

n=100000

# Create empty dictionary for cache storage
fibonacci_cache = {}

def fib(n):
    # First, check if function is already in cache
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    # Meat of the function, first compute value, cache it and return
    if n == 1 or n == 2:
        value = 1
    elif n > 2:
        value = fib(n - 1) + fib(n - 2)
        
    # cache function
    fibonacci_cache[n] = value
    
    # Return
    return value
    
# Display each step    
for n in range (1, n + 1):
        print(n, ":", fib(n))
        
# End timer        
end=time.time()
print('Time elapsed (minutes):', 
      round((end-start)/60, 2), 
      '\nTime elapsed (seconds):', 
      round(end-start, 2))
'''

'''
import time
from functools import lru_cache

# Start timer
start=time.time()

@lru_cache(maxsize = 1000)
def fib_mem(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fib_mem(n - 1) + fib_mem(n - 2)
n = 10000

# Display each step    
for n in range (1, n + 1):
        print(n, ":", fib_mem(n))
        
# End timer        
end=time.time()
print('Time elapsed (minutes):', 
      round((end-start)/60, 2), 
      '\nTime elapsed (seconds):', 
      round(end-start, 2))
'''

# ACTUAL SOLUTION, n number of months and k number of pair offspring
import time
from functools import lru_cache

# Start timer
start=time.time()


# Open the dataset
with open('rosalind_fib.txt', 'r') as file:
    content = file.read().strip()

# Split numbers based on space and allocate to proper variables    
numbers = content.split()   
n = int(numbers[0])
k = int(numbers[1])

# When presented with problem of different number of pairs as an offspring
@lru_cache(maxsize = 1000)
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
    
# End timer        
end=time.time()
print('Time elapsed (minutes):', 
      round((end-start)/60, 2), 
      '\nTime elapsed (seconds):', 
      round(end-start, 2))
  