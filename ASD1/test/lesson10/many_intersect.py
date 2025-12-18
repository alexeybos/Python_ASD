import copy
from ASD1.test.lesson10.ext_power_set import PowerSet
# 10. Множества
# 5.* Напишите функцию, которая находит пересечение любых трёх и более множеств (принимает количество множеств >= 3 в качестве списка).
# Сложность временная и пространственная O(n)
def intersect_all(sets) -> PowerSet:
    result = copy.deepcopy(sets[0])
    for i in range(1, len(sets)):
        result = result.intersection(sets[i])
    return result
