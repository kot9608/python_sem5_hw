# 35. Напишите функцию, которая принимает
# одно число и проверяет, является ли оно простым

# *Напоминание: Простое число - это число,
# которое имеет 2 делителя: 1  и n(само число)*


def prime_num(num):
    for i in range(2,num-1):
        if num%i==0:
            return('NO')
    return('YES')
            
            

n=int(input('Введите число: '))
print(prime_num(n))



def prime(number, n=2):
    if n >= number:
        return "yes"
    if number % n == 0:
        return "no"
    return prime(number, n + 1)


print(prime(10))
for i in range(100):
    if prime(i) == 'yes':
        print(i, end=' ')