import pandas as pd

data = {
    'Возраст': [21, 28, 33, 39, 26, 22, 23, 25, 27, 29],
    'Зарплата': [50000, 52000, 53000, 54000, 55000, 49000, 52000, 53000, 54000, 59000]
}

df = pd.DataFrame(data)

print(df.describe())

print(f'Средний возраст - {df["Возраст"].mean()}')
print(f'Медианный возраст - {df["Возраст"].median()}')
print(f'Мода возраста - {df["Возраст"].mode()}')
print(f'Стандартное отклонение возраста - {df["Возраст"].std()}')

print(f'Средняя зарплата - {df["Зарплата"].mean()}')
print(f'Медианная зарплата - {df["Зарплата"].median()}')
print(f'Мода зарплаты - {df["Зарплата"].mode()}')
print(f'Стандартное отклонение зарплаты - {df["Зарплата"].std()}')