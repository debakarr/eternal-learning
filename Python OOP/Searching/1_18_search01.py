 # Given an array containing only 0's and 1's where all 0's come before 1
 # Find the index of first 1
import time

# Time Complexity - O(n)
# Space Complexity - O(1)
def linearSearch(arr):
     for i, num in enumerate(arr):
         if num == 1:
             return i


# Time Complexity - O(log n)
# Space Complexity - O(1)
def usingBinarySearch(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2

        if arr[mid] == 0:
            start = mid + 1
        elif arr[mid] == 1 and (mid == start or arr[mid - 1] != 1):
            return mid
        else:
            end = mid - 1


if __name__ == '__main__':
    arr = [0, 0, 0, 0, 0, 0, 1, 1, 1]

    start_time = time.time()
    print 'First index of "1" in', arr, 'using linear search is:', linearSearch(arr)
    print "--- %s seconds ---\n" % (time.time() - start_time)
    
    start_time = time.time()
    print 'First index of "1" in', arr, 'using binary search is:', usingBinarySearch(arr)
    print "--- %s seconds ---\n" % (time.time() - start_time)
