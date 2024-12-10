import pandas as pd

# Загрузка данных из CSV-файла
data = pd.read_csv('OmicsExpressionProteinCodingGenesTPMLogp1BatchCorrected.csv')

# Просмотр первых нескольких строк данных для понимания структуры
print("Первые 5 строк данных:")
print(data.head())

# Проверка названий столбцов
print("\nНазвания столбцов:")
print(data.columns)

# Инициализация списка для хранения названий столбцов с высокой корреляцией
high_correlation_columns = []
# Проход по всем столбцам
for i in range(1,len(data.columns)):
    current_column_name = data.columns[i]
    
    # Сравнение с остальными столбцами
    for j in range(i + 1, len(data.columns)):
        comparison_column_name = data.columns[j]
        
        # Расчет коэффициента корреляции
        correlation = data[current_column_name].corr(data[comparison_column_name])
        
        # Проверка на высокую корреляцию
        if abs(correlation) >= 0.75:
            high_correlation_columns.append((current_column_name, comparison_column_name, correlation))

# Сохранение результатов в CSV-файл, если есть высокие корреляции
if high_correlation_columns:
    results_df = pd.DataFrame(high_correlation_columns, columns=['Name_Column1', 'Name_Column2', 'Correlation'])
    results_df.to_csv('high_correlation_results.csv', index=False)
    print("\nРезультаты сохранены в файл 'high_correlation_results.csv'.")
else:
    print("\nНет столбцов с высокой корреляцией (коэффициент >= 0.75).")
