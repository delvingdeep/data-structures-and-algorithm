def string_reverser(input_string):
    """
    Reverse the input string

    Args:
       input_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    return input_string[::-1]


def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    str1 = sorted((str1.lower().replace(' ', '')))
    str2 = sorted((str2.lower().replace(' ', '')))

    answer = False

    if str1 == str2:
        answer = True

    return answer


def word_flipper(input_string):
    """
    Flip the individual words in a sentence

    Args:
       input_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    input_list = input_string.split()
    output_string = ''

    for word in input_list:
        output_string += word[::-1] + ' '

    return output_string.strip()


def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """

    output = None

    if len(str1) == len(str2):
        output = 0
        for index, word in enumerate(str1):
            if str2[index] != word:
                output += 1

    return output


if __name__ == '__main__':
    s = 'This is a string'

    print('Input string: {}'.format(s))
    print('Reverse string: {}'.format(string_reverser(s)))
    print('Flipped string: {}'.format(word_flipper(s)))

    s1 = 'Dormitory'
    s2 = 'Dirty room'
    print('Are strings {} and {} anagram? {}'.format(s1, s2, anagram_checker(s1, s2)))

    str1 = 'ACTTGACCGGG'
    str2 = 'GATCCGGTACA'
    print('Hamming distance between strings {} and {} : {}'.format(str1, str2, hamming_distance(str1, str2)))



