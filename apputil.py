
import numpy as np

# update/add code below ...

# Exercise 1

# Given enough pennies (1 cent) and nickels (5 cents) write a function ways(n)
# which calculates the# number of ways you can make change for a given amount 
# of cents n. The function should return the number of ways to yield n cents 
# using only pennies and nickels.

def ways(n):
    """
    Function returns number of ways to make change for n cents using pennies 
    and nickels.
    """
    if n < 0:
        return 0
    
    return n // 5 + 1


print(ways(0))


# Exercise 2

# Suppose we have students 'names', and test 'scores' for each student, 
# respectively.  For example, we could have:

# names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
# scores = np.array([99, 71, 85, 62, 91]) 

# Part 1

# Use NumPy to write a function lowest_score(names, scores) that returns the 
# 'name' of the student with the lowest 'score'.

# Hint: Look at the argmin function.


def lowest_score(names, scores):
    """Return the name of the student with the lowest test score."""
    lowest_index = np.argmin(scores)
    return names[lowest_index]


# Part 2
# Write a similar function sort_names(names, scores) that will list the names 
# of students in descending order of test score (i.e., a list of names, with 
# associated scores in order from highest to lowest).


def sort_names(names, scores):
    """Return student names sorted by score from highest to lowest."""
    sorted_indices = np.argsort(-scores)
    return names[sorted_indices]

# Example usage:
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 99, 91])
print(lowest_score(names, scores))
print(sort_names(names, scores))