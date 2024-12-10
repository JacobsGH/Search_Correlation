import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
data = pd.read_csv('high_correlation_results.csv')

# Инициализация графа
G = nx.Graph()

# Добавление узлов и рёбер в граф
for index, row in data.iterrows():
    col1 = row['Name_Column1']
    col2 = row['Name_Column2']
    correlation = row['Correlation']
    
    # Добавляем узлы (если они еще не добавлены)
    G.add_node(col1)
    G.add_node(col2)
    
    # Добавляем рёбра только если коэффициент корреляции не равен 0 и не является NaN
    if correlation != 0 and pd.notna(correlation):
        G.add_edge(col1, col2, weight=correlation)

# Настройка размера графа
plt.figure(figsize=(100, 100))  # Увеличиваем размер фигуры для лучшей видимости

# Получение весов для рёбер
edges = G.edges(data=True)

# Определение ширины рёбер на основе коэффициента корреляции
edge_widths = [np.power(abs(edge[2]['weight']),7)*2 for edge in edges]  
#edge_widths = 0.3
# Рисуем граф
pos = nx.spring_layout(G, k=1, scale=1, iterations=1000)  # Позиционирование узлов
nx.draw_networkx_nodes(G, pos, node_size=70)  # Увеличиваем размер узлов для лучшей видимости
nx.draw_networkx_edges(G, pos, width=edge_widths)
nx.draw_networkx_labels(G, pos, font_size=10)

# Подпись рёбер с коэффициентом корреляции
edge_labels = {}
for col1, col2 in G.edges():
    correlation_values = data.loc[(data["Name_Column1"] == col1) & (data["Name_Column2"] == col2), "Correlation"]
    
    if not correlation_values.empty:  # Проверяем, есть ли значения
        edge_labels[(col1, col2)] = f'{correlation_values.values[0]:.2f}'

# Рисуем подписи к рёбрам только для тех, у кого есть значения
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Заголовок графика
plt.axis('off')  # Отключаем оси

# Сохранение графика в файл с высоким разрешением
plt.savefig('correlation_graph_Itog_6.png', format='png', dpi=250)
print("READY")
# Удаляем все текущие фигуры для освобождения памяти (опционально)
plt.clf()
