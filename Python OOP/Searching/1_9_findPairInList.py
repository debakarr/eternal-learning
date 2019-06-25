# Find pairs in the list whoes sum is equal to the target

# Time Complexity - O(n)
# Space Complexity - O(n)
def findPairsUsingSet(arr, target):
    setOfNums, result = set(), []

    for num in arr:
        if target - num in setOfNums:
            result.append([num, target - num])
        setOfNums.add(num)

    return result


# Time Complexity - O(n log n)
# Space Complexity - O(1)
def findPairsUsingSort(arr, target):
    arr.sort()

    i, j, result = 0, len(arr) - 1, []

    while i < j:
        sum = arr[i] + arr[j]
        if sum == target:
            result.append([arr[i], arr[j]])
        elif sum < target:
            i += 1
            continue
        else:
            j -= 1
            continue
        i += 1
        j -= 1

    return result



if __name__ == '__main__':
    arr = [1, 5, 8, 9, 2, 6, 3, 7, 4]
    print 'Pairs of numbers which sums up to 10 using set:', findPairsUsingSet(arr, 10)
    print 'Pairs of numbers which sums up to 10 using sort:', findPairsUsingSort(arr[:], 10)
