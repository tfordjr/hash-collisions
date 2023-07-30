import math

probability = 0.5
n = math.sqrt(-2 * 16**64 * math.log(1 - probability))              
print(f"Unique hash values needed to reach a 50% probability of collision: {n:.2e}")