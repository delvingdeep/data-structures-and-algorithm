def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    s = ''
    for value in arr:
        s += str(value)

    number = int(s)+1

    out_list = []

    for word in str(number):
        out_list.append(int(word))

    return out_list


if __name__ == '__main__':
    arr1 = [1, 2, 3]
    arr2 = [0]
    arr3 = [9, 9, 9]

    print('Adding one at nth element to {}, results: {}'.format(arr1, add_one(arr1)))
    print('Adding one at nth element to {}, results: {}'.format(arr2, add_one(arr2)))
    print('Adding one at nth element to {}, results: {}'.format(arr3, add_one(arr3)))


