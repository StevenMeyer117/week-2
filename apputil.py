import numpy as np


# Question 1

def ways_simple(n):
    """
    Returns the number of ways to make n cents using pennies and nickels


    Args:
        n (int): Total number of cents

    Returns:
        int: Number of distinct ways
    """
    count = 0

    # Looks over all possible numbers of nickels (0 up to n // 5)
    for nickels in range(n // 5 + 1):
        # Remaining cents are filled with pennies
        pennies = n - 5 * nickels

        # Each combination of nickels determines exactly one way
        count += 1
    return count

def ways(cents, coin_types=[1,5]):
    """
    Return the number of ways to make 'cents' using the given coin denominations


    Args:
        cents (int): Total number of cents
        coin_types (list[int]): Available coin denominations

    Returns:
        int: Number of distinct ways
    """

    # Stores the number of ways to make i cents
    num_ways = [0] * (cents + 1)

    # Base case -- there is exactly one way to make 0 cents
    num_ways[0] = 1 

    # For each coin, update the ways to make higher amounts
    for coin in coin_types:
        for i in range(coin, cents + 1):

            # Add ways to make (i - coin) cents
            num_ways[i] += num_ways[i - coin]
    
    return num_ways[cents]


# Question 2

names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])

def lowest_score(names, scores):
    """
    Return the name of the student with the lowest score

    Args:
        names (array): Array of student names
        scores (array): Array of corresponding scores

    Returns:
        str: Name of the student with the lowest score
    """

    # Index of the minimum score
    index = np.argmin(scores)
    return names[index]

#print(lowest_score(names, scores))

def sort_names(names, scores):
    """
    Return student names sorted by score in descending order

    Args:
        names (array): Array of student names
        scores (array): Array of corresponding scores

    Returns:
        array: names sorted from highest to lowest score
    """

    # Gets the indices that would sort the scores in descending order
    desc_order = np.argsort(scores)[::-1]
    return names[desc_order]

print(sort_names(names, scores))