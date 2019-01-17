# recursion version of binary search


def binary_search(target, value, low=0, high=0):
    try:
        mid = (low + high) // 2

        if value == target[mid]:
            return mid
        elif value < target[mid]:
            high = mid - 1
        else:
            low = mid + 1
        return binary_search(target, value, low, high)
    except RecursionError:
        return 'not exist!!!'


if __name__ == '__main__':

    # the index 0  1  2  3  4  5  6  7  8  9   10  11  12  13  14  15  16  17  18
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    value = 16
    index = binary_search(sequence, value, 0, len(sequence)-1)
    print('the index of {val} is {index}'.format(val=value, index=index))

