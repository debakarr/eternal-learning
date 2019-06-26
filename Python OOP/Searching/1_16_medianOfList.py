# Find the median of an array


def medianUsingSort(arr):
    arr.sort()

    if len(arr) % 2:
        return arr[len(arr) // 2]
    else:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2.0


if __name__ == '__main__':
    arr = [1, 3, 6, 9, 2, 4, 5, 7, 8]
    print 'Median of', arr, 'is:', medianUsingSort(arr[:])
    arr = [1, 3, 6, 9, 2, 4, 5, 7, 8, 10]
    print 'Median of', arr, 'is:', medianUsingSort(arr[:])
