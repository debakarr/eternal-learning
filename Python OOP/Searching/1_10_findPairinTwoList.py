# Find Pairs in two list which sums up to a target value


# Time Complexity - O(n ^ 2)
# Space Complexity - O(1)
def bruteForce(arr1, arr2, target):
    result = []

    for num1 in arr1:
        for num2 in arr2:
            if num1 + num2 == target:
                result.append([num1, num2])

    return result


# Time Complexity - O(n)
# Space Complexity - O(n)
def usingSet(arr1, arr2, target):
    result = []

    setOfNums2 = set(arr2) # O(n)

    for num in arr1:
        if target - num in setOfNums2:
            result.append([num, target - num])

    return result


# Time Complexity - O(n * log m)
# Space Complexity - O(1)
def usingSort(arr1, arr2, target):
    def binarySearch(arr, value):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == value:
                return True
            elif arr[mid] < value:
                low = mid + 1
            else:
                high = mid - 1

        return False

    arr2.sort()
    result = []

    for num in arr1:
        if binarySearch(arr2, target - num):
            result.append([num, target - num])

    return result

if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 6, 7, 8, 9]

    print 'Pairs of number which sums up to 10:', bruteForce(arr1, arr2, 10) 
    print 'Pairs of number which sums up to 10:', usingSet(arr1, arr2, 10) 
    print 'Pairs of number which sums up to 10:', usingSort(arr1, arr2[:], 10) 
