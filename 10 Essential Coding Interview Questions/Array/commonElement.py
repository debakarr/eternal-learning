def commonElement(arr1, arr2):
    i = 0
    j = 0
    commonElement = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            commonElement.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return commonElement


print(commonElement([1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10]))
