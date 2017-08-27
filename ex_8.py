""" With the best time complexity, please come up with a code to find the minimum delta of two elements
from two different arrays of integers of different sizes
e.g. a[-3, 1, 999], b[-1, 2, 3]
Edit: Please dont forget the min delta can also be from b-a not just a-b"""

def minDelta(arr1, arr2):

    for x in arr1:
        for y in arr2:

            minVal = divNum(x,y)

            if x == arr1[0] and y == arr2[0]:
                result = minVal
            elif minVal < result:
                result = minVal

            minVal = divNum(y,x)

            if minVal < result:
                result = minVal

    return result

def divNum(x, y):
    return abs(x-y)


arr1 = [-3, 1, 999]
arr2 = [-1, 2, 3]
result = 0

print(minDelta(arr1, arr2))
