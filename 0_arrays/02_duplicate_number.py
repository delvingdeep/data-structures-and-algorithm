def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    sorted_arr = sorted(arr)

    next_value = 0

    for value in sorted_arr:
        if value != 0 and value == next_value:
            return value
        next_value = value
    return 0


def duplicate_number2(arr):
    """
    Second method
    """
    current_sum = 0
    expected_sum = 0

    for num in arr:
        current_sum += num

    for i in range(len(arr) - 1):
        expected_sum += i

    return current_sum - expected_sum


if __name__ == '__main__':
    arr1 = [0, 0]
    arr2 = [0, 2, 3, 1, 4, 5, 3]
    arr3 = [0, 1, 5, 4, 3, 2, 0]
    arr4 = [0, 1, 5, 5, 3, 2, 4]

    print('Duplicate number in the array {}: {}'.format(arr1, duplicate_number(arr1)))
    print('Duplicate number in the array {}: {}'.format(arr2, duplicate_number(arr2)))
    print('Duplicate number in the array {}: {}'.format(arr3, duplicate_number(arr3)))
    print('Duplicate number in the array {}: {}'.format(arr4, duplicate_number(arr4)))
    print('Duplicate number in the array {}: {} (using second method)'.format(arr4, duplicate_number2(arr4)))


