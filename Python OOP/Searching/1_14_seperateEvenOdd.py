# Given a list seperate even and odd numbers


def seperate(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        if arr[start] % 2 == 0:
            start += 1
        elif arr[end] % 2 != 0:
            end -= 1
        else:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    return arr

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print 'List before Seperation:', arr, 'List after Seperation:', seperate(arr[:])

