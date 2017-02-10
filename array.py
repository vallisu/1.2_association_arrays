# Имеется два массива: {"Alex", "Dima", "Kate", "Galina", "Ivan"} и {"Dima", "Ivan", "Kate"}.
# Необходимо получить результирующий массив, который будет равен первому массиву с исключёнными
# значениями из второго массива.

first_list = ['Alex', 'Dima', 'Kate', 'Galina', 'Ivan']
second_list = ['Dima', 'Ivan', 'Kate']

for item in first_list:
    if item in second_list:
        first_list.remove(item)

print(first_list)
