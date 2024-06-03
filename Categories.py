import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'gender': ['female', 'male', 'male', 'male', 'female', 'male', 'female', 'male', 'female', 'male'],
    'department': ['Engineering', 'Employees', 'Engineering', 'Employees', 'Engineering', 'Employees', 'Engineering', 'Medical', 'Employees', 'Employees']
}

df = pd.DataFrame(data)

df['gender'] = df['gender'].astype('category')

df['department'] = df['department'].astype('category')

df['department'] = df['department'].cat.add_categories(['Finance'])
print(df['department'].cat.categories)

df['department'] = df['department'].cat.remove_categories(['Employees'])
print(df['department'].cat.categories)

print(df)