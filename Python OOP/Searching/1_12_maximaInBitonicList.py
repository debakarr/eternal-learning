# Find the maxima in a bitonic list


# Time Complexity - O(log n)
# Space Complexity - O(1)
def usingBinarySearch(arr):
    i, j = 0, len(arr) - 1

    while i <= j:
        mid = i + (j - i) // 2

        if arr[mid - 1] < arr[mid] < arr[mid + 1]:
            i = mid + 1
        elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
            j = mid - 1
        else:
            return arr[mid]

    return -1

if __name__ == '__main__':
    arr = [1, 3, 5, 7, 6, 4, 2]
    print 'Maxima for bitonic list', arr, 'is:', usingBinarySearch(arr)
