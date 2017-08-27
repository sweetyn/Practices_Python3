"""There are 2 arrays of integers.
You have to add the those integers and keep it in 3rd array.
There is one condition, if the sum is a 2 digit number, split that number into single digiit
and other condition is if any of the array integer is left then print that number
I/P:
int[] a = {1,2,3,4,5,6}
int[] b = {2,3,4,5,6,7,8}
o/p:
{3,5,7,9,1,1,1,3,8}"""


def mergeArr(arr1, arr2):

    result = []
    arrLen = 0
    restNum = 0

    if len(arr1) <= len(arr2):
        arrLen = len(arr1)
        restNum = len(arr2) - len(arr1)
    else:
        arrLen = len(arr2)
        restNum = len(arr1) - len(arr2)

    for i in range(arrLen):
        sum = arr1[i] + arr2[i]
        if sum > 10:
            result.append(1)
            result.append(sum%10)
        else:
            result.append(sum)

    for j in range(restNum):

        if len(arr1) <= len(arr2):
            result.append(arr2[arrLen+j])
        else:
            result.append(arr1[arrLen+j])

    return result

arr1 = [1,2,3,4,5,6]
arr2 = [2,3,4,5,6,7,8]

print (mergeArr(arr1, arr2))
