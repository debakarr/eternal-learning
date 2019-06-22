# Linear Search - Unsorted Input
# Time complexity - O(n)
# Space complexity - O(1)

def linearSearchUnsortedInput(arr, target):
    for num in arr:
        if num == target:
            return True
    return False

if __name__ == '__main__':
    arr = [1, 10, 7, 5, 4, 8, 2, 9, 3, 6]
    print('Array', arr)
    print('\nSearching for %d: %s.' % (3, 'Found' if linearSearchUnsortedInput(arr, 3) else 'Not Found'))
    print('\nSearching for %d: %s.' % (9, 'Found' if linearSearchUnsortedInput(arr, 9) else 'Not Found'))
    print('\nSearching for %d: %s.' % (18, 'Found' if linearSearchUnsortedInput(arr, 18) else 'Not Found'))

