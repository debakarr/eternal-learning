# Binary Search - Sorted Input
# Time complexity - O(log n)
# Space complexity - O(1)

def binarySearch(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Array', arr)
    print('\nSearching for %d: %s.' % (3, 'Found' if binarySearch(arr, 3) else 'Not Found'))
    print('\nSearching for %d: %s.' % (9, 'Found' if binarySearch(arr, 9) else 'Not Found'))
    print('\nSearching for %d: %s.' % (18, 'Found' if binarySearch(arr, 18) else 'Not Found'))

