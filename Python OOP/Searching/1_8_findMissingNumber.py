# Find the missing element in a array of length n
# Given that one element is absent and all the other elements from 0 to n are present

# Time Complexity - O(n)
# Space Complexity - O(1)
def findMissing(arr):
    length = len(arr)
    
    '''
    sumAllNums, sumArr = 0, 0
    for num in range(length + 1):
        sumAllNums += num

    for num in arr:
        sumArr += num

    return sumAllNums - sumArr
    '''

    return sum(range(length + 1)) - sum(arr)


# Time Complexity - O(n)
# Space Complexity - O(n)
def findMissingUsingFormula(arr):
    length = len(arr)

    return length * (length + 1) // 2 - sum(arr)


# Time Complexity - O(n)
# Space Complexity - O(1)
def findMissingUsingXOR(arr):
    sum = 0
    for num in range(len(arr) + 1):
        sum ^= num

    for num in arr:
        sum ^= num

    return sum

if __name__ == '__main__':
    arr = [1, 6, 4, 7, 5, 3, 8, 0, 9]
    print 'Missing number in', arr, '= %d' % findMissing(arr)
    print 'Missing number in', arr, '= %d' % findMissingUsingFormula(arr)
    print 'Missing number in', arr, '= %d' % findMissingUsingXOR(arr)
