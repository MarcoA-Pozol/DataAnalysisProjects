import pandas as pd
import random

# Options for data generation
ranges = (0, 100)
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"] 

# Lists of data
numbers_list = []
characters_list = []

# Adding data to lists
for _ in range(5):
    numbers_list.append(random.randint(ranges[0], ranges[1]))
    characters_list.append(random.choice(characters))
    
print(numbers_list)
print(characters_list)

# Arrays to pandas Series
numbers_series = pd.Series(numbers_list)
characters_series = pd.Series(characters_list)

print(numbers_series)
print(characters_series)

# Merging series
merged_series = pd.concat([numbers_series, characters_series])
print(merged_series)

# Mergin series interleaving values
mixed_series = pd.Series([val for pair in zip(numbers_series, characters_series) for val in pair])
print(mixed_series)