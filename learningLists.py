fruits = ["apple", "banana", "cherry"]
# List index starts from 0 because it means the "offset" - how far from the beginning.
# 0 means zero steps from the beginning (zero-based index).
# example (50 = 0, 48 = 1, 41 == 2, 45 = 3).

scores = [50, 48, 41, 45]
students = []

secondScore = scores[1]
# 1 = subscript operator (indicates the zero-based position in the list of a particular value).
# In this case [1] refers to 48.

scoreCount = len(scores)
# gives back number of elements/values in the list.

lastScore = scores - 1
# negative index, lets you get the last element of a list.
