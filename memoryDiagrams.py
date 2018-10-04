#  Author: Roxanne Lai
#  CMPT 120L 113
#  Introduction to programming
#  Date: 9/27/18
# Numbers = [17,23,4,72,45,9]
# looking for the largest number


#import math
#def MaxOf(nums):
# nums = 17, 23, 4, 72, 45, 9
# maxSoFar = - infinity
# nextNum = 17
# is nextNum > maxSoFar ?
# if so then
#    set maxSoFar == nextNum
# replace - infinity with 17 if nextNum is > maxSoFar
# keep going if nextNum is not > maxSoFar

import math


def maxOf(nums):
    maxSoFar = - math.inf
    for i in range(0, len(scores)):
        nextNum = nums[i]
        if nextNum > maxSoFar:
            maxSoFar == nextNum
# end of the loop
# # what will diagram look like when control reaches line but has not run it (diagram B)
    return maxSoFar


scores = [84, 66, 97, 71, 92]
# what will diagram look like when control reaches line but has not run it (diagram A)
print("The highest score is" + str(maxOf(scores)) + ".")