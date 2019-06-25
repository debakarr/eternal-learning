# Find pairs in the list whoes sum is closest to 0


# Time Complexity - O(n ^ 2)
# Space Complexity - O(1)
def bruteForce(arr):
    result, MIN = [None, None], float('inf')

    for i, num1 in enumerate(arr):
        for j, num2 in enumerate(arr[i + 1:]):
            if abs(num1 + num2) < MIN:
                MIN = abs(num1 + num2)
                result = [num1, num2]

    return result


# Time Complexity - O(n log n)
# Space Complexity - O(1)
def usingSort(arr):
    arr.sort()
    i, j = 0, len(arr) - 1

    while i < j:
        sum = arr[i] + arr[j]
        if sum == 0:
            return [arr[i], arr[j]]
        elif sum < 0:
            i += 1
        else:
            j -= 1

    return result
  


if __name__ == '__main__':
    arr = [-6, -3, -7, -4, 1, 5, 8, 9, 2, 6, 3, 7, 4]
    print 'Pair whose sums is closest to 0:', bruteForce(arr)
    print 'Pair whose sums is closest to 0:', usingSort(arr[:])
