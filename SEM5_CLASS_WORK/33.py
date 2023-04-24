# Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.
# [1,2,3,4,4,5,5,3,2] -> [1,2,3,4,4,1,1,3,2]

arr = [1, 2, 3, 4, 4, 5, 5, 3, 2]


def change_nums(arr):
    max_num = max(arr)
    min_num = min(arr)

    for i in  range(len(arr)):
        if arr[i] == max_num:
            arr[i] = min_num
    return (arr)


print(change_nums(arr))


# def sumNumbers(n):
#  summa = 0
#  for i in range(1, n + 1):
#  summa += i
#  return summa


# lst = list(map(int, input("list: ").split()))


# def downgrade(some_list, max_grade, min_grade):
#     if max_grade not in lst:
#         return some_list
#     ind = lst.index(max_grade)
#     lst[ind] = min_grade
#     return downgrade(some_list, max_grade, min_grade)


# print(downgrade(lst, max(lst), min(lst)))


