"""Given an array , find the element (say X) that has
all the elements less that it to its left side
and all the elements greater to it on its right side.
The left and right elements of X need not be in sorted form.
"""
def standElement(x, arr1):

    if x in arr1:
        result.insert(0, x)

        for i in arr1:
            if x < i:
                result.append(i)
            elif x > i:
                result.insert(0, i)

    return result

arr1 = [20,59,48,1,7,3,9,-100,0]
x = 9
result = []

print (standElement(x, arr1))
