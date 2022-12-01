# 2) Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.



x = int(input('Введите число: '))
temp = 0
max_1 = 0
max_2 = 0
for i in range(x):
    number: int = int(input())
    if number > max_1 or number > max_2:
        if number > max_1:
            max_1 = number
        else:
            max_2 = number

print(max_1, max_2)