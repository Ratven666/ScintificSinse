from Считывание_точек import *

# Считываение точек с блокнота
data=Points.create_point_from_input()
data.remove('end')
print(data)

# Для вывода отдельной точки
# print(Points.find_point(data))

# Для вывода диапазона точек
# print(Points.list_of_points(data))
