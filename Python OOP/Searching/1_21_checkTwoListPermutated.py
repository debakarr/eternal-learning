# Check if two list are permutation of each other
import time

# Time Complexity - O(n + m)
# Space Complexity - O(n + m)
def isPermutationUsingHash(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    
    arr1CountDict, arr2CountDict = {}, {}


    for num in arr1:
        arr1CountDict[num] = arr1CountDict.get(num, 0) + 1

    for num in arr2:
        arr2CountDict[num] = arr2CountDict.get(num, 0) + 1

    for num, count in arr1CountDict.items():
        if num not in arr2CountDict or arr2CountDict[num] != arr1CountDict[num]:
            return False

    return True


# Time Complexity - O(n log n + m log m)
# Space Complexity - O(1)
def isPermutationUsingSorting(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    arr1.sort()
    arr2.sort()

    for i, num in enumerate(arr1):
        if arr2[i] != num:
            return False

    return True


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 3, 1, 4, 2]

    start_time = time.time()
    print 'Using Hash:', arr2, 'is permutation of', arr1, '?', isPermutationUsingHash(arr1, arr2)
    print "--- %s seconds ---\n" % (time.time() - start_time)

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 3, 6, 4, 2]

    start_time = time.time()
    print 'Using Hash:', arr2, 'is permutation of', arr1, '?', isPermutationUsingHash(arr1, arr2)
    print "--- %s seconds ---\n" % (time.time() - start_time)
    
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 3, 1, 4, 2]

    start_time = time.time()
    print 'Using Sorting:', arr2, 'is permutation of', arr1, '?', isPermutationUsingHash(arr1, arr2)
    print "--- %s seconds ---\n" % (time.time() - start_time)

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 3, 6, 4, 2]

    start_time = time.time()
    print 'Using Sorting:', arr2, 'is permutation of', arr1, '?', isPermutationUsingHash(arr1, arr2)
    print "--- %s seconds ---\n" % (time.time() - start_time)
