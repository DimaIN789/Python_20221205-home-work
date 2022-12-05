#Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
#Формат: Объясняет преподаватель

#Задача: предложить улучшения кода для уже решённых задач:

#С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension(4 задачи из прошлых семинаров переделать с использованием этих функций)


from functools import reduce
dot_1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split())) 
dot_2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))
def dot_range(dot_1, dot_2):
     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
     return round(rng, 2)
print(dot_range(dot_1, dot_2))







