# Duplicate element in a list

# Time Complexity - O(n ^ 2)
# Space Complexity - O(1)

def bruteForce(arr):
    print "\n\nDuplicate element(s) using brute force in", arr, ":"

    for i, num1 in enumerate(arr):
        for j, num2 in enumerate(arr[i + 1:]):
            if num1 == num2:
                print num1,


# Time Complexity - O(n log n)
# Space Complexity - O(1)
def sortAndScan(arr):
    print "\n\nDuplicate element(s) using sort and scan in", arr, ":"

    arr.sort()

    for i, num in enumerate(arr[1:]):
        if num == arr[i]:
            print num,


# Time Complexity - O(n)
# Space Complexity - O(n)
def usingHashTable(arr):
    print "\n\nDuplicate element(s) using hash table in", arr, ":"

    hashTable = set()

    for num in arr:
        if num in hashTable:
            print num,
        else:
            hashTable.add(num)


# Time Complexity - O(n)
# Space Complexity - O(n)
def countingSearch(arr, maxElement):
    print "\n\nDuplicate element(s) using counting search in", arr, ":"

    count = [0] * (maxElement + 1)

    for num in arr:
        if count[num] == 1:
            print num,
        else:
            count[num] += 1

if __name__ == '__main__':

    arr = [1, 6, 3, 7, 2, 9, 1, 4, 7, 2, 8, 3, 9, 6]
    bruteForce(arr)
    sortAndScan(arr[:]) # Sending copy of arr, because if arr is send then it will change the original arr
    usingHashTable(arr)
    countingSearch(arr, 9)

