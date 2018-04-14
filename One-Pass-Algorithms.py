# Example Problems Solvable by One-pass Algorithms

# Given an list as an input:
# (1) Count the number of elements
# Method 1: use list comprehension
l=list['aasadfsdslkllad']
l.count('a')
# Return a list of list
[[x,l.count(x)] for x in set(l)]

# Method 2: use the python counter
import collections
a=collections.Counter(l)

#(2) Find the nth element from the end(or report the list has fewer than n elements)

# (3) Find the k largest(smallest)elements,,k given in advance
c=[5,4,1,2,9]
n=9
sorted(c)[-n]

# (4) Find the sum, mean, variance and standard deviation of the elements of the list


# Example Problems Not Solvable by One-pass Algorithms

# Find the median
# Find the modes
# Sort the list
