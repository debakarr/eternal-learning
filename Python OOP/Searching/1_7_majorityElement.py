# Find the majority element in the array
# Majority element is the element which appears more than n / 2 times
# Given the size of the array is n


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

    if maxCount > len(arr) // 2:
        return maxCount, maxValue
    else:
        return 0

# Time Complexity - O(n log n)
# Space Complexity - O(1)
def sortAndScan(arr):
    arr.sort()

    maxValue, count = arr[len(arr) // 2], 0

    for num in arr:
        if num > maxValue:
            break
        if maxValue == num:
            count += 1
        
    if count > len(arr) // 2:
        return count, maxValue
    else:
        return 0

def mooreVotingAlgorithm(arr):
    maxValueIndex, count = 0, 1

    for i, num in enumerate(arr[1:]):
        if num == arr[maxValueIndex]:
            count += 1
        else:
            count -= 1

        if count == 0:
            maxValueIndex = i + 1
            count = 1

    maxValue, count = arr[maxValueIndex], 0

    for num in arr:
        if num == maxValue:
            count += 1

    if count > len(arr) // 2:
        return count, maxValue
    else:
        return 0


if __name__ == '__main__':
    arr = [1, 3, 2, 3, 5, 3, 3, 3, 3, 3]

    print "Majority element exist in", arr, "with count =  %d of element %d using brute force" % bruteForce(arr)
    print "Majority element exist in", arr, "with count =  %d of element %d using sort and scan" % sortAndScan(arr[:])
    print "Majority element exist in", arr, "with count =  %d of element %d using mooreVotingAlgorithm" % mooreVotingAlgorithm(arr)

