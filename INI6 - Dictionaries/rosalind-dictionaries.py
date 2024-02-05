#Opening the file
raw_text=open("rosalind_ini6.txt", "r") 

#Create empty dictionary
d = dict()
    
#Iterate through lines in text
for line in raw_text:
    # Remove newline character
    line = line.strip()

    # Convert to lowercase so no mismatch occurs
    # Good thing to do, but rosaling won't accept lowercase solutions
    #line = line.lower()
    
    # Split words based on space (creates list from big string)
    words = line.split(" ") 
                         
    # Iterate over each word within wprd-spliting loop 
    for word in words: 
        if word in d: 
            d[word] = d[word] + 1
        else:
            # if there is no previous mention of the word in dictionary this is first
            d[word] = 1
            
print(d)

# Cosmetically pleasing way to display values
for key, value in d.items():
    print(key, value)