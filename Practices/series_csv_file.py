import pandas as pd

# Sample data
data = {
    'Name': ['Carolina Steward', 'Nahum Correa', 'Aline Pascal', 'Steve Hordward', 'Henrry Crawford', 'Robert Kutz', 'Andrea Schutzman', 'Camila Martinez', 'Antonio Silva', 'Dewey Johnson'],
    'Ocupation': ['Data Engineer', 'QA Assistance', 'FrontEnd Developer', 'QA Specialist', 'Project Manager', 'Product Owner', 'BackEnd Developer', 'Hiring and Recruiting', 'FullStack Developer', 'Data Engineer'],
    'Salary': [3200, 2650, 2250, 2800, 3800, 3670, 2690, 1890, 2900, 3160],
    'Age': [24, 28, 32, 37, 43, 49, 20, 39, 25, 34]
}

# Comprobe every value list for key in data dict has 10 values for DataFrame consistency
print(len(data['Name']), len(data['Ocupation']), len(data['Salary']), len(data['Age']))

# Convert data to DataFrame 
df = pd.DataFrame(data)
print(df) # Dataframe has a similar to a list apearance in console and structure, easy to read and understand

# Save dataframe to csv file
df.to_csv('DataSets/employees.csv', index=False)
print('CSV file created successfully!')

# Add more rows to the existing dataframe
new_rows = {
    'Name': ['Yael Pratz', 'Patrick Hassberg', 'Louise Cambell'],
    'Ocupation': ['FrontEnd Developer', 'BackEnd Developer', 'Hiring and Recruiting'],
    'Salary': [1260, 2050, 1960],
    'Age': [19, 26, 28],
}
new_df = pd.DataFrame(new_rows)
updated_df = pd.concat([df, new_df], ignore_index=True)
print(updated_df)

# Add single rows to the dataframe
updated_df.loc[len(updated_df)] = ['Kevin Mckense', 'IT Support', 1450, 22]
updated_df.loc[len(updated_df)] = ['Torey Pudwill', 'IT Support', 1620, 31]
print(updated_df)

# Update employees csv file
updated_df.to_csv("DataSets/employees.csv", index=False)

# Read CSV file
import csv

with open('DataSets/employees.csv', newline='') as file:
    file_data = csv.reader(file)
    for row in file_data:
        print(row)