import copy


def rotateArrayInplace(arr, n):
    for i in range(n / 2):
        for j in range(i, n - i - 1):
            current_i, current_j = i, j
            temp = [-1, -1, -1, -1]
            for k in range(4):
                temp[k] = arr[current_i][current_j]
                current_i, current_j = rotateSubtitution(current_i, current_j, n)
            for k in range(4):
                arr[current_i][current_j] = temp[(k + 3) % 4]
                current_i, current_j = rotateSubtitution(current_i, current_j, n)
    return arr


def rotateArray(arr, n):
    rotatedArray = copy.deepcopy(arr)
    for i in range(n):
        for j in range(n):
            new_i, new_j = rotateSubtitution(i, j, n)
            rotatedArray[new_i][new_j] = arr[i][j]
    return rotatedArray


def rotateSubtitution(i, j, n):
    return j, n - 1 - i


def printArr(arr):
    for row in arr:
        for col in row:
            print '%2d' % col,
        print


arr = [[7, 8, 9], [1, 2, 4], [5, 6, 3]]
print 'Normal Array\n'
printArr(arr)
print '\nAfter rotating 90 degree clockwise, using extra array method\n'
printArr(rotateArray(arr, 3))
print '\nAfter rotating 90 degree clockwise, using inplace method\n'
printArr(rotateArrayInplace(arr, 3))
