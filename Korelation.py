import pandas as pd

# Загрузка данных из CSV-файла
data = pd.read_csv('OmicsExpressionProteinCodingGenesTPMLogp1BatchCorrected.csv')

# Просмотр первых нескольких строк данных для понимания структуры
print("Первые 5 строк данных:")
print(data.head())

# Проверка названий столбцов
print("\nНазвания столбцов:")
print(data.columns)

# Расчет коэффициента корреляции для всех числовых столбцов, начиная со второго
correlation_matrix = data.iloc[:, 1:].corr()

# Сохранение матрицы корреляций в CSV-файл
correlation_matrix.to_csv('correlation_matrix.csv', index=True)

print("\nМатрица корреляций сохранена в файл 'correlation_matrix.csv'.")
