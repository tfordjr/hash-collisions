# CS 4732 Project 3 Hash Collisions with SHA-256

from hashlib import sha256

input_ = input('Enter something: ')
print(sha256(input_.encode('utf-8')).hexdigest())