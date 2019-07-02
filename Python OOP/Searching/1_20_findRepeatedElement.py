# Find the first repeating element in the given list
import time

# Time Complexity - O(n ^ 2)
# Space Complexity - O(1)
def bruteForce(arr):
    for i, num1 in enumerate(arr):
        for num2 in arr[i+1:]:
            return num2

    return -1


# Time Complexity - O(n)
# Space Complexity - O(n)
def usingHash(arr):
    numSet = set()

    for num in arr:
        if num in numSet:
            return num

    return -1

if __name__ == '__main__':
    arr = [1, 7, 3, 6, 2, 7, 3, 6]

    start_time = time.time()
    print "First repeating element in", arr, "using brute force is:", bruteForce(arr)
    print "--- %s seconds ---\n" % (time.time() - start_time)

    start_time = time.time()
    print "First repeating element in", arr, "using hashing is:", bruteForce(arr)
    print "--- %s seconds ---\n" % (time.time() - start_time)
