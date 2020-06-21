def check_sudoku(sudoku):
    """
    Checks if a 2d array is a sudoku or not
    :param sudoku: A 2d array of dimension nxn
    :return: True if it's a valid sudoku
    """

    # check for row
    for row in sudoku:

        check_list = list(range(1, len(sudoku[0])+1))

        for num in row:
            if num not in check_list:
                return False
            check_list.remove(num)

    # check for columns
    for n in range(len(sudoku[0])):

        check_list = list(range(1, len(sudoku[0])+1))

        for row in sudoku:
            if row[n] not in check_list:
                return False
            check_list.remove(row[n])

    return True


if __name__ == '__main__':

    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]

    incorrect = [[1,2,3,4],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,4]]

    print('Correct: ', check_sudoku(correct))
    print('Incorrect: ', check_sudoku(incorrect))
