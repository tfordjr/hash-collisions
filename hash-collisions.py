# CS 4732 Project 3 Hash Collisions with SHA-256

from hashlib import sha256
import fileinput
import time
start = time.time()

filename = 'HP Books.txt'
count = 0
hashmap = {}

with open(filename, encoding="utf-8") as f:
    for line in f:                
        hash = sha256(line.encode('utf-8')).hexdigest()      

        if hash not in hashmap.keys():    # If hash value not present in hashmap
            hashmap[hash] = line          # Assign this key-value (hash-plaintext) keypair. 
        elif(hashmap[hash] != line):      # collision exists and isn't result of same input
            print(hash, "hash - line", hashmap[hash], "line - hash", line)  
                          
        count = count + 1

end = time.time()

# print(hashmap)
# for hash in hashmap:
#     print(hashmap[hash])
print(count, 'lines hashed in', (end-start), 'seconds')