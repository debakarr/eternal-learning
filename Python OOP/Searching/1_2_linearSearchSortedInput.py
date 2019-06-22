# Linear Search - Sorted Input
# Time complexity - O(n)
# Space complexity - O(1)

def linearSearchSortedInput(arr, target):
    for num in arr:
        if num == target:
            return True
        if num > target:
            return False
    return False

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Array', arr)
    print('\nSearching for %d: %s.' % (3, 'Found' if linearSearchSortedInput(arr, 3) else 'Not Found'))
    print('\nSearching for %d: %s.' % (9, 'Found' if linearSearchSortedInput(arr, 9) else 'Not Found'))
    print('\nSearching for %d: %s.' % (18, 'Found' if linearSearchSortedInput(arr, 18) else 'Not Found'))

