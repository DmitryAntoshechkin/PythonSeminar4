# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

def GetArray(number, count):
    array = []
    for i in range(number):
        array.append(int(input(f'Введите элемент {count} множества :')))
    print()
    return (array)


n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
array1 = set(GetArray(n,1))
array2 = set(GetArray(m,2))
new_array = list(array1.intersection(array2))
for i in range(len(new_array)):
    for j in range(i+1, len(new_array)):
        if new_array[j] < new_array[i]:
            temp = new_array[j]
            new_array[j] = new_array[i]
            new_array[i] = temp
print (new_array)

