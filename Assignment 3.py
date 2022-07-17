from random import randint


# Это алгоритм quicksort, реализованный через три списка и случайный выбор числа.
# В лучшем случае он выполнится за O(n*log n), в худшем за O(n^2).
# Он будет плохо работать с уже отсортированным массивом, и если случайное число окажется самым большим,
# или самым меньшим в массиве, но, в целом, он превосходит другие алгоритмы сортировки,
# хотя при большом массиве чисел рекурсивная часть может занять очень много памяти.

def quicksort(array):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    point = array[randint(0, len(array) - 1)]

    for x in array:
        if x < point:
            low.append(x)
        elif x == point:
            same.append(x)
        elif x > point:
            high.append(x)

    return quicksort(low) + same + quicksort(high)

