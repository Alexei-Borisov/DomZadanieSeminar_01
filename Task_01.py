#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.

num_1 = int(input('Введите число обозначающее день недели: '))
if 1 <= num_1 <= 5:
    print(f'число {num_1} не является выходным днём')
elif 6 <= num_1 <= 7:
    print(f'число {num_1} является выходным днём')
else:
    print('Число введено не верно')
    