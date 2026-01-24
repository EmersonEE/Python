"""

Dado un array de numeros y un numero goal, encuentre los dos primeros numeros del array que sumen el numero goal
y devuelva sus indices, si no existe tal combinacion devuelve none
nums = [4,5,6,2]
goal = 8
find_first_sum(nums,goal)
"""

import re


def find_fitst_sum(nums, goal):
    for i in range(len(nums)):
        print(i)
        for j in range(i + 1, len(nums)):
            if nums[1] + nums[j] == goal:
                return [i, j]

    return None


nums = [4, 5, 6, 2]
goal = 8
resutl = find_fitst_sum(nums, goal)
print(resutl)


def find_first_sum_dic(nums, goal):
    seen = {}  # Diccionario para guardar el numero y el indice
    for index, value in enumerate(nums):
        missing = goal - value
        if missing in seen:
            return [seen[missing], index]
        seen[value] = (
            index  # Guardar el numero altual a los vistos, porque no hemos encontrado
        )
        print(f"index: {index} value: {value}")


resutl = find_first_sum_dic(nums, goal)
print(f"los indices son: {resutl}")
