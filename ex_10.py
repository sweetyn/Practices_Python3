"""Write a program to display numbers having sum
of left side numbers equal to right side numbers. 
{2,0,-11,1,12}=>0 {Left side number 2+0=2, Right side number -11+1+12=2}"""

def equalSum(arr):

    i = 0
    while i < len(arr):

        leftSum = 0
        rightSum = 0
        #leftside sum
        for x in arr[:i]:
            leftSum += x

        #rightside sum
        for y in arr[i+1:]:
            rightSum += y

        if leftSum == rightSum:
            break

        i += 1

    if leftSum == rightSum:
        result = "leftSide = ", arr[:i+1], "rightSide = ", arr[i+1:]
    else:
        result = "It is impossible to make equal number"

    return result


arr = [2,0,-11,1,12]
result = []

print(equalSum(arr))
