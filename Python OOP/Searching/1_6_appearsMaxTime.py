# Find the number which appears max time in an array

# Time Complexity - O(n ^ 2)
# Space Complexity - O(1)

def bruteForce(arr):
    maxCount, maxValue = 1, arr[0]

    for i, num1 in enumerate(arr):
        count = 1
        for j, num2 in enumerate(arr[i + 1:]):
            if num1 == num2:
                count += 1

        if count > maxCount:
            maxCount = count
            maxValue = num1

    return maxCount, maxValue


# Time Complexity - O(n log n)
# Space Complexity - O(1)

def sortAndScan(arr):
    maxCount, maxValue, currentCount = 1, arr[0], 1

    arr.sort()

    for i, num in enumerate(arr[1:]):
        if num == arr[i]:
            currentCount += 1
        else:
            currentCount = 1

        if currentCount > maxCount:
            maxCount = currentCount
            maxValue = num

    return maxCount, maxValue


# Time Complexity - O(n)
# Space Complexity - O(n)

def countingSearchMax(arr, maxElement):
    count = [0] * (maxElement + 1)
    maxCount, maxValue = 1, arr[0]

    for num in arr:
        count[num] += 1

        if count[num] > maxCount:
            maxCount = count[num]
            maxValue = num

    return maxCount, maxValue

if __name__ == '__main__':
    arr = [1, 2, 3,7, 3, 6, 1, 3, 8, 1, 5, 1]

    print "Maximum count in", arr, "is %d of element %d using brute force" % bruteForce(arr)
    print "Maximum count in", arr, "is %d of element %d using sort and scan" % sortAndScan(arr[:])
    print "Maximum count in", arr, "is %d of element %d using counting" % countingSearchMax(arr, max(arr))
