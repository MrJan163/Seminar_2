# 3) Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых


z_p = int(input())
count = 0
while(z_p > 0):
    if z_p > 25:
        print(f'25ти рублёвых купюр - {z_p // 25}')
        count += z_p // 25
        z_p %= 25
    elif z_p >= 10:
        print(f'10ти рублёвых купюр - {z_p // 10}')
        count += z_p // 10
        z_p %= 10
    elif z_p >= 7:
        print(f'7ми рублёвых купюр - {z_p // 7}')
        count += z_p // 7
        z_p %= 7
    elif z_p >= 3:
        print(f'3х рублёвых купюр - {z_p // 3}')
        count += z_p // 3
        z_p %= 3
    else:
        print(f'рублёвых купюр - {z_p // 1}')
        count += z_p // 1
        z_p %= 1
print('Минимальное количество купюр = ', count)