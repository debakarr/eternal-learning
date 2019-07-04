# Remove duplicate element from the list


def removeDuplicateUsingSet(arr):
    return set(arr)

def removeDuplicateUsingSorting(arr):
    arr.sort()

    index = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[index] = arr[i]
            index += 1

    return arr[:index]



if __name__ == '__main__':
    arr = [1, 5, 8, 2, 5, 1, 7, 9, 2, 6]
    print 'Before Removing:', arr, 'After Removing:', removeDuplicateUsingSet(arr)
    print 'Before Removing:', arr, 'After Removing:', removeDuplicateUsingSorting(arr)
