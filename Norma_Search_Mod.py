import pandas as pd
import numpy as np

def Normal_Search(list1, list2):
    difference = 0
    denominator = 0

    # Преобразование списков в массивы NumPy для удобства вычислений
    list1 = np.array(list1)
    list2 = np.array(list2)

    # Вычисление разности и знаменателя
    for i in range(len(list1)):
        if list1[i] > 0 and list2[i] > 0:
            difference += np.linalg.norm(list1[i] - list2[i])
            denominator += np.linalg.norm(list2[i])
    # Предотвращение деления на ноль
    if denominator == 0:
        return None

    return difference / denominator

# Загрузка данных из CSV-файла
data = pd.read_csv('OmicsExpressionProteinCodingGenesTPMLogp1BatchCorrected.csv')

# Просмотр первых нескольких строк данных для понимания структуры
print("Первые 5 строк данных:")
print(data.head())

# Проверка названий столбцов
print("\nНазвания столбцов:")
print(data.columns)

# Инициализация списка для хранения названий столбцов с высокой нормализацией
high_normalization_columns = []

# Проход по всем столбцам
for i in range(1, len(data.columns)):
    current_column_name = data.columns[i]
    
    # Сравнение с остальными столбцами
    for j in range(i + 1, len(data.columns)):
        comparison_column_name = data.columns[j]
        
        # Расчет коэффициента нормализации
        normalization = Normal_Search(data[current_column_name], data[comparison_column_name])
        
        # Проверка на высокую нормализацию
        if normalization is not None and abs(normalization) >= 0.75:
            high_normalization_columns.append((current_column_name, comparison_column_name, normalization))

# Сохранение результатов в CSV-файл, если есть высокие нормализации
if high_normalization_columns:
    results_df = pd.DataFrame(high_normalization_columns, columns=['Name_Column1', 'Name_Column2', 'Normalization'])
    results_df.to_csv('high_normalization_results.csv', index=False)
    print("\nРезультаты сохранены в файл 'high_normalization_results.csv'.")
else:
    print("\nНет столбцов с высокой нормализацией (коэффициент >= 0.75).")
