# Bubble sort


def bubbleSort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                swap = True
                print "Swap %d <--> %d" % (arr[i], arr[j])
                arr[i], arr[j] = arr[j], arr[i]

        if not swap:
            break

    return arr


if __name__ == '__main__':
    arr = [6, 2, 8, 1, 5, 3, 9, 7]
    print "\nBefore Sort:", arr 
    sort = bubbleSort(arr)
    print "After Sort:", sort
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print "\nBefore Sort:", arr 
    sort = bubbleSort(arr)
    print "After Sort:", sort
