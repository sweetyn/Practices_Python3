"""Given two sorted arrays A and B that may have repeated elements.
Form a new sorted array C that contains the elements of A and B
[Condition : You are not allowed to merge the two arrays and then sort.]
"""

def merSorted (arr1, arr2):

    if arr1[0] <= arr2[0]:
        minV = arr1[0]
    else:
        minV = arr2[0]

    if arr1[len(arr1)-1] >= arr2[len(arr2)-1]:
        maxV = arr1[len(arr1)-1]
    else:
        maxV = arr2[len(arr2)-1]

    #x=0
    #total = len(arr1)+len(arr2)
    while minV <= maxV:
        if minV in arr1:
            result.append(minV)
        if minV in arr2:
            result.append(minV)
        minV += 1

    return result

arr1 = [0,1,3,5,8,10]
arr2 = [1,5,8,21,45,67]
result = []

print (merSorted (arr1, arr2))
