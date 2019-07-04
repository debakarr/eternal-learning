# Given a 2 dimensional list. Each row and column are sorted in ascending order. How would you find an element in it?

# Time Complexity - O(m + n)
# Space Complexity - O(1)
def searchElementIn2DArrayHelper(arr2D, target):
    i, j = 0, len(arr2D[0]) - 1
    while i <= len(arr2D) - 1 and 0 <= j:
        if arr2D[i][j] == target:
            return i + 1, j + 1
        elif arr2D[i][j] < target:
            i += 1
        else:
            j -= 1

    return -1, -1

def printMatrix(arr2D):
    for row in arr2D:
        print row


def searchElementIn2DArray(arr2D, target): 
    cord = searchElementIn2DArrayHelper(arr2D, target)
    if cord != (-1, -1):
        print "\nSearching for %d in..." % target
        printMatrix(arr2D)
        print "Found in (%d, %d)!!!" % (cord)
    else:
        print "\nSearching for %d in" % target
        printMatrix(arr2D)
        print "Not Found"

if __name__ == '__main__':
    arr2D = [[1, 3, 6, 8, 9], [2, 5, 7, 10, 11], [3, 8, 9, 11, 13], [4, 9, 10, 12, 14]]

    searchElementIn2DArray(arr2D, 12)
    searchElementIn2DArray(arr2D, 7)
    searchElementIn2DArray(arr2D, 8)
    searchElementIn2DArray(arr2D, 22)

