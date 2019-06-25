# Find the count of an element in a sorted List

# Time Complexity - O(n)
# Space Complexity - O(1)
def linearScan(arr, target):
    count = 0

    for num in arr:
        if num == target:
            count += 1

    return count


# Time Complexity - O(log n)
# Space Complexity - O(1)
def usingBinarySearch(arr, target):
    
    def findFirstIndex(arr, target):
        i, j = 0, len(arr) - 1

        while i <= j:
            mid = i + (j - i) // 2

            if arr[mid] == target and (mid == i or arr[mid - 1] != target):
                return mid
            elif arr[mid] < target:
                i = mid + 1
            else:
                j = mid - 1

        return -1

    def findLastIndex(arr, target):
        i, j = 0, len(arr) - 1

        while i <= j:
            mid = i + (j - i) // 2

            if arr[mid] == target and (mid == j or arr[mid + 1] != target):
                return mid
            elif arr[mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        return -1

    firstIndex = findFirstIndex(arr, target)
    lastIndex = findLastIndex(arr, target)

    return lastIndex - firstIndex + 1


if __name__ == '__main__':
    arr = [1, 2, 2, 4, 4, 4, 6, 7]

    print 'Count of number %d using linear scan in' % 4, arr, 'is:', linearScan(arr, 4)
    print 'Count of number %d using binary search in' % 4, arr, 'is:', usingBinarySearch(arr, 4)
