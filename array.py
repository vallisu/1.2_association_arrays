# Имеется два массива: {"Alex", "Dima", "Kate", "Galina", "Ivan"} и {"Dima", "Ivan", "Kate"}.
# Необходимо получить результирующий массив, который будет равен первому массиву с исключёнными
# значениями из второго массива.

# 1st option - without using collections
first_list = ['Alex', 'Dima', 'Kate', 'Galina', 'Ivan']
second_list = ['Dima', 'Ivan', 'Kate']
result_list = first_list.copy()

for item in first_list:
    if item in second_list:
        result_list.remove(item)

print(result_list)


# 2nd option - using collections
first_list_coll = {"Alex", "Dima", "Kate", "Galina", "Ivan"}
second_list_coll = {"Dima", "Ivan", "Kate"}

print(first_list_coll - second_list_coll)
