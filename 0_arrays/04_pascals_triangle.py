def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    if n == 0:
        return [1]

    current_row = [1]    # first row

    for i in range(1, n+1):
        previous_row = current_row

        current_row = [1]    # add default first element in the list

        for j in range(1, i):

            # an element at jth position in the current row is
            ## sum of element at j and j-1 position in the previous row
            current_row.append(previous_row[j-1] + previous_row[j])

        current_row.append(1)    # add default last element in the list

    return current_row


if __name__ == '__main__':

    num = input('Enter the number of elements: ')
    number_list = [x for x in range(int(num))]

    print("Pascal's Triangle for {} elements".format(len(number_list)))
    for number in number_list:
        print(nth_row_pascal(number))
