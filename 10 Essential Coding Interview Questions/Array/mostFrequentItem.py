def mostFrequentItem(arr):
    hashTable = {}
    mostCount = 0
    mostFrequentItem = None
    for num in arr:
        if num in hashTable:
            hashTable[num] += 1
            if hashTable[num] > mostCount:
                mostCount = hashTable[num]
                mostFrequentItem = num
        else:
            hashTable[num] = 1

    return mostFrequentItem


print(mostFrequentItem([1, 2, 1, 3, 1, 3, 1, 3, 3, 3]))
