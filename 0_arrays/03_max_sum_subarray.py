def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    sum_arr = []
    sum_ele = 0

    for i in range(len(arr)):
        num = arr[i]
        while i < len(arr):
            sum_ele += arr[i]
            sum_arr.append(sum_ele)
            i += 1
        i = num
        sum_ele = 0

    return max(sum_arr)


def max_sum_subarray2(arr):
    """
    Second method
    """
    current_sum = arr[0] # the sum of a subarray
    max_sum = arr[0]     # maximum value of current_sum ever

    for element in arr[1:]:

        # If (current_sum + element) is higher, it denotes the addition of the element to the current subarray
        # If (element) alone is higher, it denotes the starting of a new subarray
        current_sum = max(current_sum + element, element)
        
        # Update max_sum, if it is lower than the update it with current_sum
        max_sum = max(current_sum, max_sum)   
    
    return max_sum


if __name__ == '__main__':
    arr1 = [1, 2, 3, -4, 6]
    arr2 = [1, 2, -5, -4, 1, 6]
    arr3 = [-12, 15, -13, 14, -1, 2, 1, -5, 4]

    print('Maximum of the subarray in {} : {}'.format(arr1, max_sum_subarray(arr1)))
    print('Maximum of the subarray in {} : {}'.format(arr2, max_sum_subarray(arr2)))
    print('Maximum of the subarray in {} : {}'.format(arr3, max_sum_subarray(arr3)))
    print('Maximum of the subarray in {} : {} (using second method)'.format(arr3, max_sum_subarray2(arr3)))
