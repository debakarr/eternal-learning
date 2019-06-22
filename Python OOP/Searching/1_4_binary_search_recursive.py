# Binary Search - Sorted Input
# Time complexity - O(log n)
# Space complexity - O(log n) [For system stack maintained during recursion]

def binarySearch(arr, target):
    return binarySearchHelper(arr, target, 0, len(arr) - 1)


def binarySearchHelper(arr, target, low, high):
    if low > high:
        return False

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binarySearchHelper(arr, target, mid + 1, high)
    else:
        return binarySearchHelper(arr, target, low, mid - 1)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Array', arr)
    print('\nSearching for %d: %s.' % (3, 'Found' if binarySearch(arr, 3) else 'Not Found'))
    print('\nSearching for %d: %s.' % (9, 'Found' if binarySearch(arr, 9) else 'Not Found'))
    print('\nSearching for %d: %s.' % (18, 'Found' if binarySearch(arr, 18) else 'Not Found'))

