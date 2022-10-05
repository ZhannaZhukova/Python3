#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#*Пример:*

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

from random import randint

num = int(input('Введите размер списка: '))
arr = []
arr2 = []

for i in range(num):
    arr.append(randint(0, 7))

for i in range(len(arr)):
    while i < len(arr)/2 and num > len(arr)/2:
        num = num - 1
        a = arr[i] * arr[num]
        arr2.append(a)
        i += 1

print(arr)
print(arr2)