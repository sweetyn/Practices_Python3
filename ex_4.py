"""Reverse an array in subset of N. Example:
input: Array = [1,2,3,4,5,6,7,8,9], N = 3
output: [3,2,1,6,5,4,9,8,7]"""

def reverArr(arr,n):

    result = []

    divMod = []
    i=0

    divMod = divmod(len(arr), n)

    while i < len(arr)-divMod[1]:
        tempArr = arr[i:i+n]
        tempArr.reverse()
        result += tempArr
        i += n

    if divMod[1] > 0:
        tempArr = arr[divMod[0]*n:]
        tempArr.reverse()
        result += tempArr

    return result


arr = [1,2,3,4,5,6,7,8,9]
n = 3

print(reverArr(arr,n))
# Completed
