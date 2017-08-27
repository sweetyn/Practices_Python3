"""Print the first and final occurrence of a number in a sorted array of integers.
e.g. int[] list = {1,2,3,4,5,5,7,8}
"""

def occNum(arr):

    firstNum = 0
    finalNum = 0
    result = ""

    for i in range(len(arr)-1):

        if arr[i] == arr[i+1] and firstNum == 0:
            firstNum = arr[i]

        if arr[i] == arr[i+1]:
            finalNum = arr[i]

    result = "first occurrence number is " + str(firstNum) + " and final occurrence number is " + str(finalNum)

    return result

arr = [1,2,3,4,5,5,7,8]

print (occNum(arr))
