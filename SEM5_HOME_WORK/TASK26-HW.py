# Задача 26:  
# Напишите программу, 
# которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a=int(input('Введите число: '))
b=int(input('Введите степень: '))

def quad(num, step):
    if step == 0:
        return 1
    return quad(num, step-1)*num

print(quad(a,b))




# def fib(number):
#     if number in (1, 2):
#         return 1
#     return fib(number - 1) + fib(number - 2)


# print(fib(int(input("Введите порядковый номер числа Фибоначчи: ")) + 1))

# def rev2(num):
#     n = input("Enter: ")
#     if num == 1:
#         return n
#     return rev2(num - 1) + f" {n}"


# print(rev2(int(input("Введите длину: "))))