# Given a sorted list of n interger which is rotated unknow number of times, find the element
import time


def binarySearch(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid


def searchInSortedRotatedList(arr, target):
    low, high = 0, len(arr) - 1
    mid = None

    if arr[low] < arr[high]:
        return binarySearch(arr, target)

    while low <= high:
        mid = low + (high - low) // 2
       
        if arr[mid] > arr[low]
        if arr[low] < key and arr[mid] > key:
            high = mid - 1
        elif arr[high] < key and arr[mid] > key:
            start = mid + 1
        else:
            return mid



if __name__ == '__main__':
    arr = [6, 5, 4, 1, 2, 3] # [1, 2, 3, 4, 5, 6] - Original array
    
    start_time = time.time()
    print "Position of 2 in", arr, "is:", searchInSortedRotatedList(arr, 2)
    print "--- %s seconds ---\n" % (time.time() - start_time)
