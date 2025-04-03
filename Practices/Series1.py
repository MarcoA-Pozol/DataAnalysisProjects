import pandas as pd
import random

employees = ["Joseph", "Jennifer", "Andrea", "Heriberto", "Michail", "Mattew"]
salaries = [] # Monthly

# Generate salaries
for _ in range(len(employees)):
    num = random.randrange(850, 1200, 10)
    salaries.append(num)
    
# Pandas serie
employees_serie = pd.Series(employees)
salaries_serie = pd.Series(salaries)

print(employees_serie)
print(salaries_serie)

# Merge two pd.Series
concat_series = pd.concat([employees_serie, salaries_serie], ignore_index=False)
print(concat_series)