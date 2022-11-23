
"""
This module sorts lists of integers...
"""


def bubble(int_list):
    """Sorts an array using Bubble Sort.

    Args:
    int_list: the array to be sorted.
    Returns:
    Nothing. The array that is used as an argument will
    be sorted after calling this function
    Raises:
    TypeError: if theList is not an array.
    TypeError: if theList contains an element that is not an integer

    """
    for i in range(len(int_list)):
        for j in range(0, len(int_list) - i - 1):
            if int_list[j] > int_list[j + 1]:
                temp = int_list[j]
                int_list[j] = int_list[j + 1]
                int_list[j + 1] = temp


def quick(int_list, left, right):
    """Sorts an array using Quick Sort.
    Args:
    int_list: the array to be sorted.
    left: the leftmost index of the array
    right: the rightmost index of the array

    Returns:
    Nothing. The array that is used as an argument will 
    be sorted after calling this function

    Raises:
    TypeError: if theList is not an array.
    TypeError: if theList contains an element that is not an integer

    """
    if left < right:
        greatest = left - 1

        for j in range(left, right):
            if int_list[j] <= int_list[right]:
                greatest = greatest + 1
                (int_list[greatest], int_list[j]) = (int_list[j], int_list[greatest])
        (int_list[greatest + 1], int_list[right]) = (
            int_list[right], int_list[greatest + 1]
        )
        quick(int_list, left, greatest)
        quick(int_list, greatest + 2, right)


def insertion(int_list):
    """Sorts an array using Insertion Sort.

    Args:
    int_list: the array to be sorted.
    Returns:
    Nothing. The array that is used as an argument will
    be sorted after calling this function
    Raises:
    TypeError: if theList is not an array.
    TypeError: if theList contains an element that is not an integer

    """
    for i in range(1, len(int_list)):
        current = int_list[i]
        j = i - 1
        while j >= 0 and current < int_list[j]:
            int_list[j + 1] = int_list[j]
            j -= 1
        int_list[j + 1] = current
