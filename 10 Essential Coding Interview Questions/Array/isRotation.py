def isRotation(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for i, num in enumerate(arr2):
        if num == arr1[0]:
            pos = i
            break

    for i, num in enumerate(arr1):
        index = (pos + i) % len(arr1)
        if num != arr2[index]:
            return False

    return True


print 'Checking [1, 2, 3, 4, 5, 6] and [5, 6, 1, 2, 3, 4]: ', isRotation([1, 2, 3, 4, 5, 6], [5, 6, 1, 2, 3, 4])
print 'Checking [1, 2, 3, 4, 5, 6] and [5, 6, 1, 2, 3, 8]: ', isRotation([1, 2, 3, 4, 5, 6], [5, 6, 1, 2, 3, 8])
