"""Given two sorted arrays A and B that may have repeated elements.
Form a new sorted array C that contains the elements of A and B
[Condition : You are not allowed to merge the two arrays and then sort.]
"""
def merSorted (arr1, arr2):
    result = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        elif arr1[i] == arr2[j]:
            result.append(arr1[i])
            result.append(arr2[j])
            i += 1
            j += 1
        elif arr1[i] > arr2[j]:
            result.append(arr2[j])
            j += 1

    if len(arr1) > len(arr2):
        result += arr1[i:]
    elif len(arr1) < len(arr2):
        result += arr2[j:]

    return result

arr1 = [1,3,5,8,10]
arr2 = [0,1,5,8,21,45,67]


print (merSorted (arr1, arr2))
# Completed
